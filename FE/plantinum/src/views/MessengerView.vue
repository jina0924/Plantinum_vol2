<template>
  <nav-bar></nav-bar>
  <section>
    <div class="container py-4">

      <div class="row">
        <div class="col-md-12">

          <div class="card" id="chat3">
            <div class="card-body">

              <div class="row">

                <div class="col-md-6 col-lg-5 col-xl-4 mb-4 mb-md-0">

                  <div class="p-2">

                    <div class="chat-list-title mb-3 d-flex justify-content-center">
                      <span>채팅 목록</span>
                    </div>

                    <div class="chat-list-view">
                      <ul class="m-0 list-unstyled">
                        <li class="m-0 border-bottom chat-list-item" @click="changeReceiver(key)" v-for=" (val,key) in rooms" :key="val" :class="{'list-item-active': key===now_receiver}">
                          <div class="d-flex justify-content-between">
                            <div class="d-flex flex-row">
                              <div>
                                <img
                                  :src="baseURL + urls[key]"
                                  alt="상대방 프로필 사진" class="d-flex align-self-center chat-list-img">
                              </div>
                              <div class="pt-3">
                                <p class="your-name">{{ nicknames[key] }}</p>
                              </div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                    <hr class="d-md-none">

                  </div>

                </div>
                <hr class="d-md-none">

                <div class="col-md-6 col-lg-7 col-xl-8">
                  <div class="you-username" v-if="now_receiver!==-1">{{ nicknames[now_receiver] }}</div>
                  <div class="chat-view" ref="now_messages">

                    <div v-if="now_receiver===-1" class="leaf82-chat-start">
                      <span class="material-symbols-outlined leaf82-chat-icon">nest_found_savings</span>
                      <div>잎팔이 채팅</div>
                    </div>

                    <div v-for="msg in now_messages" :key="msg">

                      <div class="d-flex flex-row justify-content-center" v-if="msg.person==='PLANT'">
                        <div>
                          <p class="plant-name">---- {{ msg.msg }} 채팅 시작 ----</p>
                        </div>
                      </div>

                      <div class="d-flex flex-row justify-content-start" v-if="msg.person!==username && msg.person!=='PLANT'">
                        <img :src="baseURL + urls[now_receiver]"
                          alt="avatar 1" class="chat-profile-img" v-if="now_receiver !== -1">
                        <div class="message-section">
                          <pre class="your-message chat-message">{{ msg.msg }}</pre>
                          <p class="message-time">{{ msg.datetime.substr(5, 11) }}</p>
                        </div>
                      </div>

                      <div class="d-flex flex-row justify-content-end" v-if="msg.person===username">
                        <div class="message-section">
                          <pre class="my-message chat-message">{{ msg.msg }}</pre>
                          <p class="message-time">{{ msg.datetime.substr(5, 11) }}</p>
                        </div>
                      </div>
                    </div>
                    </div>

                  <div class="d-flex justify-content-start align-items-center" v-if="now_receiver!==-1">
                    <textarea v-model="message" type="text" class="form-input" id="exampleFormControlInput2"
                      placeholder="Type message" @keyup.enter="sendMessage" rows="1" autofocus></textarea>
                    <span @click="sendMessage" class="material-symbols-outlined send-btn">send</span>
                  </div>

                </div>
              </div>

            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions, mapGetters } from "vuex"
import { io } from 'socket.io-client'

export default {
  name: 'MessengerView',
  components:{
    NavBar,
  },
  data(){
    return {
      socket: null,
      id: -1,
      message: '',
      now_messages: [],
      now_receiver: -1,
      rooms: {},
      urls: {},
      baseURL: "https://plantinum.s3.ap-northeast-2.amazonaws.com/",
      nicknames: {},
    }
  },
  computed: {
    ...mapGetters(['receiver','username', 'leaf82_plant', 'nickname']),
  },
  async created() {
    this.id = this.username

    if( this.receiver !== -1 ){
      this.now_receiver=this.receiver;
    }
    
    if ( this.leaf82_plant !== -1) {
      this.now_plant = this.leaf82_plant
    }

    this.socket = io('http://i7a109.p.ssafy.io:3000')
    this.socket.on('connect', () => {
    })
    this.socket.emit('makeSocketName',this.id);
    this.socket.emit('getRooms',this.id);

    if(this.now_receiver !== -1){
      if( (this.now_receiver in this.rooms) == false ){
        this.socket.emit('startchat',this.now_receiver, this.leaf82_plant);
      }else{
        this.socket.emit("getMessages",this.rooms[this.now_receiver]);
      }
    }
    this.socket.on("roomIsExist",(room_num) => {
      this.socket.emit("getMessages",room_num);
    })


    this.socket.on('messages', (messages) => {
      this.now_messages = messages
    })
    this.socket.on('message', (message, sender) => {
      if(sender === this.now_receiver || sender == this.username){
        this.now_messages.push(message)
      }
    })

    this.socket.on('sendRooms',(data)=>{
      this.rooms[data.with_who] = data.room_num;
      this.urls[data.with_who] = data.photo_url;
      this.nicknames[data.with_who] = data.nickname;
    })
    

    
  },
  methods : {
    ...mapActions(['setReceiver',]),

    changeReceiver(data){
      if(this.now_receiver === data){
        return;
      }else{
        this.now_receiver=data;
        this.socket.emit("getMessages",this.rooms[this.now_receiver]);
      }
    },

    sendMessage() {
      if(this.now_receiver == -1){
        return;
      }
      const check_msg = this.message.trim()
      if (check_msg !== '') {
        this.socket.emit('send', {receiver:this.now_receiver , msg: this.message, room_num:this.rooms[this.now_receiver]});
        this.message = ''
      }
    },

    start(){
      if( (this.receiver in this.rooms) == false ){
        this.socket.emit('startchat',{receiver:this.receiver});
      }else{
        
        this.socket.emit("getMessages",this.rooms[this.receiver]);
      }
    },

  },

  beforeRouteLeave(to,from,next){
    this.socket.disconnect();
    this.now_receiver=-1;
    this.rooms={};
    this.setReceiver(-1);
    next();
  },

  watch: {
    now_messages() {
      this.$nextTick(() => {
        let now_messages = this.$refs.now_messages;
        now_messages.scrollTo({ top : now_messages.scrollHeight, behavior: 'smooth' })
      })
    }
  },

  updated() {
    let now_messages = this.$refs.now_messages;
    now_messages.scrollTo({ top : now_messages.scrollHeight, behavior: 'smooth' })
  }
  
}
</script>


<style scoped>
section {
  min-height: 87vh;
}

.card {
  border-radius: 15px;
  border: 1px solid white;
  box-shadow: 0 0 .5rem #edeae2;
}

.chat-list-title {
  font-weight: 600;
  font-size: 1.15rem;
}

.chat-list-view {
  position: relative;
  height: 500px;
  overflow-y: scroll;
  overflow-x: hidden;
  padding: 0 1rem 0 0;
}

.chat-list-view::-webkit-scrollbar {
  width: 10px;
}
.chat-list-view::-webkit-scrollbar-thumb {
  background-color: #EFEFEF;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.chat-list-view::-webkit-scrollbar-track {
  background-color: white;
  border-radius: 10px;
}

.chat-list-img {
  width: 60px;
  height: 60px;
  margin-right: .5rem;
  border-radius: 50%;
}

.chat-list-item {
  padding: .8rem;
}

.chat-list-item:hover {
  cursor: pointer;
  background-color: #EFEFEF;
}

.list-item-active {
  background-color: #EFEFEF;
}

.chat-view {
  position: relative; 
  height: 500px;
  padding: 1rem 2rem 0 1rem;
  overflow-y: scroll;
  overflow-x: hidden;
}

.leaf82-chat-start {
  color: #D9D9D9;
  text-align: center;
  font-size: 1.2rem;
  height: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.leaf82-chat-icon {
  font-size: 13rem;
  margin-bottom: .5rem;
}

.you-username {
  margin: .5rem;
  text-align: center;
  font-size: 1.3rem;
  font-weight: 600;
}

.chat-view::-webkit-scrollbar {
  width: 10px;
}
.chat-view::-webkit-scrollbar-thumb {
  background-color: #EFEFEF;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.chat-view::-webkit-scrollbar-track {
  background-color: white;
  border-radius: 10px;
}

.chat-profile-img {
  width: 45px;
  height: 45px;
  margin-right: .5rem;
  border-radius: 50%;
}

.your-name {
  font-weight: 500;
  margin-bottom: 0;
}

.wish-leaf {
  font-size: .8rem;
  font-weight: 400;
  color: rgb(73, 73, 73);
  margin-top: .2rem;
}

.time-cnt{
  font-size: .8rem;
  font-weight: 400;
  color: rgb(73, 73, 73);
}

.plant-name {
  padding: .2rem;
  color: #845A49  ;
}

.message-section {
  max-width: 50%;
}

.chat-message {
  font-family: 'SUIT';
  white-space: pre-wrap;
  /* width: 90%; */
}

.your-message {
  background-color: #f5f6f7;
  border-radius: 10px;
  margin-bottom: .3rem;
  padding: .8rem 1rem;
}

.my-message {
  background-color: #b2c9ab;
  border-radius: 10px;
  margin-bottom: .3rem;
  padding: .8rem 1rem;
}

.message-time {
  font-size: .9rem;
  font-weight: 200;
  color: rgb(73, 73, 73);
  float: inline-end;
  margin: 0 1rem;
}

.form-input {
  display: block;
  width: 93%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.75rem;
  margin: 1.3rem .5rem 1.5rem 0;
  background-color: #fff;
  background-clip: padding-box;
  border-color: rgba(178, 201, 171, 20% ) ;
  border: none;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
  resize: none;
}

.form-input:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

.form-input::-webkit-scrollbar {
  width: 10px;
}
.form-input::-webkit-scrollbar-thumb {
  background-color: #EFEFEF;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
}
.form-input::-webkit-scrollbar-track {
  background-color: white;
  border-radius: 10px;
}

.send-btn:hover {
  color: #65805d;
  cursor: pointer;
}
</style>