//import express from 'express'
//import { Server } from 'socket.io'
//import { createServer } from 'http'
const express = require("express");
const { Server } = require("socket.io");
const { createServer } = require("http");
const { pool } = require("./db");
const fs = require('fs')
const cors=require('cors');
//const { networkInterfaces } = require("os");
//const { profile } = require("console");

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
//let sockets_count = 0;
// pk : socket(list)

const connected_sockets={A:null,B:null,C:null};

// 방번호, 채팅내역
class ChatInfo{
  constructor(num){
    this.room_number = num;
    this.messages = [];
    // this.messages=[{"person":"A","datetime":"YYYYMMDDHHMM","msg":"Lorem"}];
  }
}


//저장된 채팅 내역 불러오기
const remain_datas = fs.readFileSync('./stored_data/chatrooms.json').toString();
const chat_datas = JSON.parse(remain_datas);

//console.log("----- for ------");
for (data in chat_datas){
    if(data == "rooms_count"){
      rooms_count = chat_datas.rooms_count;
    };
    //console.log(data);
    chattingRooms[data]=new ChatInfo(data);
    //console.log(chat_datas[data]["messages"]);
    //console.log()
    chattingRooms[data]["messages"]= chat_datas[data]["messages"];
}

//저장된 방정보 불러오기

const remain_rooms = fs.readFileSync('./stored_data/user_rooms.json').toString();
const room_datas = JSON.parse(remain_rooms);

//console.log(room_datas);
user_rooms = room_datas;


function nowDate(){
  const date = new Date(+new Date() + 3240 * 10000).toISOString().split("T")[0];
  const time = new Date().toTimeString().split(" ")[0];

  return date+' '+time;
}

async function geturl(data){
  try{
    const req = await pool.query( `select photo from accounts_user where username="${data}"`);
    //console.log(req[0][0]['photo']);
    return req[0][0]['photo'];
  }catch (err){
    console.log(err)
    return "static/profile.jpg"
  }
}



// 앞단에서 요청이 오고 소켓이 생성되면 이벤트를 발생시킨다.
// 두번째 인자인 콜백함수에 생성된 소켓이 담겨져온다.
// 소켓에는 해당 소켓에 연결된 모든 클라이언트들에게 broadcast를 하거나,
// 이벤트를 발생 혹은 수신할 수 있는 메서드가 있다.
io.on('connection', socket => {
  console.log("Socket is connect!! : " ,socket.id);
  //console.log(socket);

  //소켓이랑 이름 매칭
  //나중에 db로 저장필요
  socket.on('makeSocketName',data=>{
    //let isexist = 0;
    // pk - socket 형태
    // 만약 참여하는 방이 존재한다.
    // 기존 채팅룸이 존재하는가? => 찾아내서 보내줌
    /*
    if(data in user_rooms === true){  
      console.log(user_rooms[data]);  
      for ( chatroom of user_rooms[data]){
        console.log(chatroom)
        socket.join(String(chatroom[1]));
        socket.emit('sendRooms',{with_who:chatroom[0] , room_num:chatroom[1]});
      }
    }
*/
    // 정보 입력
    connected_sockets[data] = socket;
    socket.user_name = data;
    console.log(data);
    

    //기존 소켓 존재 
    /*
    for (let i=0;i<sockets_count;i++){
    
      if(connected_sockets[i].user_name === data){
        isexist = 1;
        socket.user_name = data;
        connected_sockets[i] = socket;
        break;
      }
    }
    
    //새거일때
    if(isexist == 0){
      socket.user_name = data;
      connected_sockets.push(socket);
      sockets_count++;
    }
    */
  });

  socket.on('startchat',async (data,plant)=>{

    if((socket.user_name in user_rooms) == true){
      if((data in user_rooms[socket.user_name]) === true){
        console.log("it is exist!!")
        const chat={"person": "PLANT" , "datetime":nowDate(),"msg": plant};
        chattingRooms[user_rooms[socket.user_name][data]].messages.push(chat);
        const newchatdata=JSON.stringify(chat_datas);
        fs.writeFileSync('./stored_data/chatrooms.json',newchatdata);
        socket.emit("roomIsExist",user_rooms[socket.user_name][data]);
        return;
      }
    }

    console.log("make chattingrooms");
    console.log(socket.user_name,data)
    //처음 채팅방이 만들어짐
    chattingRooms[rooms_count]=new ChatInfo(rooms_count);
    
    //user_rooms에 채팅방 저장
    //console.log(user_rooms[socket.user_name]);
    //user_rooms[socket.user_name].setAttribute(data,rooms_count);
    //console.log(user_rooms);
    //user_rooms[socket.user_name][data]=rooms_count;
    //user_rooms[data][socket.user_name]=rooms_count;
    
    //보낸사람
    if((socket.user_name in user_rooms) === true){
      //console.log(socket.user_name ,"is here");
      user_rooms[socket.user_name][data]=rooms_count;
      //user_rooms[socket.user_name].push([data.receiver,rooms_count]);
    }else{
      //console.log(socket.user_name ,"is not here");
      user_rooms[socket.user_name]={};
      user_rooms[socket.user_name][data]=rooms_count;
      //user_rooms[socket.user_name]=[[data.receiver,rooms_count]];
    }
    //console.log(user_rooms);

    
    //console.log(socket.user_name)

    //받는 사람도
    if((data in user_rooms) === true){
      user_rooms[data][socket.user_name]=rooms_count;
    }else{
      user_rooms[data]={};
      user_rooms[data][socket.user_name]=rooms_count;
    }
    
    //받은 유저 탐색후 그 소켓 채팅방 참여

    //보낸 소켓 채팅방 참여
    socket.join(String(rooms_count));
    socket.emit('sendRooms',{with_who:data, room_num:rooms_count,photo_url: await geturl(data)});
    //상대 채팅방 참여(현재 접속시)
    if((connected_sockets[data] in io.sockets.sockets) == true){
      connected_sockets[data].join(String(rooms_count));
      connected_sockets[data].emit('sendRooms',{with_who:socket.user_name, room_num:rooms_count});

    }
    //connected_sockets[data.receiver].join(String(rooms_count));
    //connected_sockets[data.receiver].emit('sendRooms',{with_who:socket.user_name, room_num:rooms_count});
    
    /*
    for (let i=0 ; i<sockets_count;i++){
      if(connected_sockets[i].user_name == data.receiver){
        connected_sockets[i].join(String(rooms_count));
        connected_sockets[i].emit('getRooms',{with_who : socket.user_name, room_num:rooms_count});
        break;
      }
    }*/

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
      //console.log(user_rooms[data]);  
      for ( who in user_rooms[data]){
        //console.log(who)
        // 채팅방 반환 및 참여.
        const num = user_rooms[data][who]
        socket.join(String(num));
        socket.emit('sendRooms',{with_who:who , room_num:num,photo_url:await geturl(who)});
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
    //"datetime [user_name] msg"
    //"datetime [Plant] url"
    message = "["+socket.user_name+"] "+data.msg;
    //console.log(message);
    //console.log(data.room_num, chattingRooms[data.room_num]);
    const chat={"person": socket.user_name, "datetime":nowDate(),"msg":data.msg};
    chattingRooms[data.room_num].messages.push(chat);
    //console.log(chattingRooms[data.room_num].messages);
    //chattingRooms[data.room_num].messages.push(message);
    //messages_send.push(message);
    io.to(String(data.room_num)).emit('message', chat, socket.user_name);

    //채팅 저장
    //chat_datas[data.room_num].messages.push(chat);
    
    const newchatdata=JSON.stringify(chat_datas);
    fs.writeFileSync('./stored_data/chatrooms.json',newchatdata);
  });

  
  socket.on('disconnect', () => {
    console.log("socket disconnect : ",socket.id,socket.user_name);
    //console.log(user_rooms);
    //console.log(user_rooms[socket.user_name]);
    // 채팅 room에서 소켓 제거 필요
    if((socket.user_name in user_rooms) == true){
      for ( partner in user_rooms[socket.user_name]){
        socket.leave(String(user_rooms[socket.user_name][partner]));
      }
    }
  });
})


app.get("/", async (req,res) => {
  //const data = await geturl("plantinum_test2");
  //console.log(data);
  res.send("Hello world");
})
// app.listen이 아닌 http.listen를 사용한다.
http.listen(3000, () => {
  console.log('started server')
})






