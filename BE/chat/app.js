const express = require("express");
const { Server } = require("socket.io");
const { createServer } = require("http");
const { pool } = require("./db");
const fs = require('fs')
const cors=require('cors');

// express 초기화
const app = express()
// socket.io 지원을 위해 http 모듈에서 제공하는 메서드로 서버를 초기화한다.
const http = createServer(app)

app.use(express.json())
//app.use(cors());


let corsOptions={
	origin:'http://plantinum.co.kr',
	credentials:true
}

app.use(cors(corsOptions))


// 웹 소켓 서버를 초기화한다. 두번째로 서버를 초기화할 때 여러 옵션을 줄 수 있다.
const io = new Server(http, {
  cors: {
	  origin: ['http://plantinum.co.kr']
	  //origin: "*"
  }
})



let rooms_count = 0;
//const messages_send = [];
// 방번호, 채팅 내역만
const chattingRooms = {};
// 각각 어느 채팅방에 존재하는지
let user_rooms={A:{},B:{},C:{}};
//연결된 소켓 관리, {id,uid}
const connected_sockets={A:null,B:null,C:null};

// 방번호, 채팅내역
class ChatInfo{
  constructor(num){
    this.room_number = num;
    this.messages = [];
  }
}


//저장된 채팅 내역 불러오기
const remain_datas = fs.readFileSync('./stored_data/chatrooms.json').toString();
const chat_datas = JSON.parse(remain_datas);


for (data in chat_datas){
    if(data == "rooms_count"){
      rooms_count = chat_datas.rooms_count;
    };
    chattingRooms[data]=new ChatInfo(data);
    chattingRooms[data]["messages"]= chat_datas[data]["messages"];
}

//저장된 방정보 불러오기

const remain_rooms = fs.readFileSync('./stored_data/user_rooms.json').toString();
const room_datas = JSON.parse(remain_rooms);

user_rooms = room_datas;


function nowDate(){
  const date = new Date(+new Date() + 3240 * 10000).toISOString().split("T")[0];
  const time = new Date().toTimeString().split(" ")[0];

  return date+' '+time;
}

async function geturl(data){
  try{
    const req = await pool.query( `select nickname,photo from accounts_user where username="${data}"`);
   
    return [req[0][0]['nickname'], req[0][0]['photo']];
  }catch (err){
    return ["there is no nickname" ,"static/profile.jpg"]
  }
}



// 앞단에서 요청이 오고 소켓이 생성되면 이벤트를 발생시킨다.
// 두번째 인자인 콜백함수에 생성된 소켓이 담겨져온다.
// 소켓에는 해당 소켓에 연결된 모든 클라이언트들에게 broadcast를 하거나,
// 이벤트를 발생 혹은 수신할 수 있는 메서드가 있다.
io.on('connection', socket => {

  //소켓이랑 이름 매칭
  //나중에 db로 저장필요
  socket.on('makeSocketName',data=>{
    // 정보 입력
    connected_sockets[data] = socket;
    socket.user_name = data;
    
  });

  socket.on('startchat',async (data,plant)=>{

    // 만약 두사람의 채팅이 존재 할 때 따로 만들지 않고 원래 방으로 이어줌
    if((socket.user_name in user_rooms) == true){
      if((data in user_rooms[socket.user_name]) === true){
        const chat={"person": "PLANT" , "datetime":nowDate(),"msg": plant};
        chattingRooms[user_rooms[socket.user_name][data]].messages.push(chat);
        const newchatdata=JSON.stringify(chat_datas);
        fs.writeFileSync('./stored_data/chatrooms.json',newchatdata);
        socket.emit("roomIsExist",user_rooms[socket.user_name][data]);
        return;
      }
    }

    //처음 채팅방이 만들어짐
    chattingRooms[rooms_count]=new ChatInfo(rooms_count);
    
    //user_rooms에 채팅방 저장
    
    //보낸사람
    if((socket.user_name in user_rooms) === true){
      user_rooms[socket.user_name][data]=rooms_count;
    }else{
      user_rooms[socket.user_name]={};
      user_rooms[socket.user_name][data]=rooms_count;
    }
   

    //받는 사람
    if((data in user_rooms) === true){
      user_rooms[data][socket.user_name]=rooms_count;
    }else{
      user_rooms[data]={};
      user_rooms[data][socket.user_name]=rooms_count;
    }
    
    //받은 유저 탐색후 그 소켓 채팅방 참여

    //보낸 소켓 채팅방 참여
    socket.join(String(rooms_count));
	  const sql_info = await geturl(data);
    // 상대, 방번호, 사진url, 닉네임
    socket.emit('sendRooms',{with_who:data, room_num:rooms_count, photo_url: sql_info[1], nickname:sql_info[0]});
    //상대 채팅방 참여(현재 접속시)
    if((connected_sockets[data] in io.sockets.sockets) == true){
      connected_sockets[data].join(String(rooms_count));
      connected_sockets[data].emit('sendRooms',{with_who:socket.user_name, room_num:rooms_count});

    }

    // 채팅 시작 시 식물 정보 저장
    const chat={"person": "PLANT" , "datetime":nowDate(),"msg": plant};
    chattingRooms[rooms_count].messages.push(chat);
    //해당 채팅 시작알림 메세지 보내기
    io.to(String(rooms_count)).emit('message', chat);
    //만들어진 룸넘버 제공

    //json 저장
    chat_datas[String(rooms_count)]=chattingRooms[rooms_count];
    
    rooms_count++;
    
    chat_datas["rooms_count"] = rooms_count;

    const newchatdata=JSON.stringify(chat_datas);
    fs.writeFileSync('./stored_data/chatrooms.json',newchatdata);

    const newroomdata=JSON.stringify(user_rooms);
    fs.writeFileSync('./stored_data/user_rooms.json',newroomdata);

  });

  socket.on('getRooms', async data=>{

    if(data in user_rooms === true){   
      for ( who in user_rooms[data]){
        // 채팅방 반환 및 참여.
        const num = user_rooms[data][who]
        socket.join(String(num));
		const sql_info= await geturl(who);
        socket.emit('sendRooms',{with_who:who , room_num:num, photo_url: sql_info[1],nickname:sql_info[0]});
      }
    }

  });

  socket.on('joinInChat',()=>{
    //현재 소켓이 참여한 채팅방 정보 불러오기
    for (chatroom of user_rooms[socket.user_name]){
      // 0 : 상대 정보, 1: 채팅방 번호
      socket.join(String(chatroom[1]));
    }

  });

  socket.on('getMessages', data =>{
    socket.emit('messages',chattingRooms[data].messages);
  });

  socket.on('send', data => {
  
    message = "["+socket.user_name+"] "+data.msg;

    const chat={"person": socket.user_name, "datetime":nowDate(),"msg":data.msg};
    chattingRooms[data.room_num].messages.push(chat);

    io.to(String(data.room_num)).emit('message', chat, socket.user_name);

    //채팅 저장
    
    const newchatdata=JSON.stringify(chat_datas);
    fs.writeFileSync('./stored_data/chatrooms.json',newchatdata);
  });

  
  socket.on('disconnect', () => {
    // 채팅 room에서 소켓 제거 필요
    if((socket.user_name in user_rooms) == true){
      for ( partner in user_rooms[socket.user_name]){
        socket.leave(String(user_rooms[socket.user_name][partner]));
      }
    }
  });
})

/*
app.get("/", async (req,res) => {
  res.send("Hello World");
})
*/
// app.listen이 아닌 http.listen를 사용한다.
http.listen(3000, () => {
  //console.log('started server')
})






