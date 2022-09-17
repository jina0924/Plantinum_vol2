<template>
  <div class="leaf82-detail row">
    <div class="col-md-3 col-0"></div>
    <div class="main col-md-6 py-5 my-5">
      <div class="left">
        <div class="img-box d-flex justify-content-center">
          <img :src="leaf82Detail.photo" alt="화분 사진">
        </div>
      </div>
      <div class="row">
        <div class="col-sm-2 col-0"></div>
        <div class="col-sm-8 col-0">
          <div class="right mt-3">
            <div class="plantname d-flex justify-content-start align-items-center">
              <span class="category" v-if="leaf82Detail.category_class === '분양받아요'">{{ leaf82Detail.category_class }}</span>
              <span class="category-2" v-if="leaf82Detail.category_class === '분양해요'">{{ leaf82Detail.category_class }}</span>
              <span class="ml-3">{{ leaf82Detail.plantname }}</span>
            </div>
            <hr>
            <div class="nickname d-flex justify-content-start pb-3">
              <router-link :to="{ name: 'myplant' , params: { username: this.$route.params.username } }" class="nickname-route">
                <img :src="user.photo" :alt="`${ user.nickname }의 프로필 사진입니다.`" class="user-photo mr-1">
              </router-link>
              <router-link :to="{ name: 'myplant' , params: { username: this.$route.params.username } }" class="nickname-route">
                <p>{{ user.nickname }}</p>
                <p class="addr">{{ addr.sido }} {{ addr.sigungu }}</p>
              </router-link>
            </div>
            <div class="price d-flex justify-content-start pb-2">
              <p>{{ leaf82Detail.price }} 원</p>
            </div>
            <div class="created_at d-flex justify-content-start pb-2">
              <p>등록일 : {{ info.created_at }}</p>
            </div>
            <div class="status d-flex justify-content-start pb-2">
              <p>{{ leaf82Detail.status_class }}</p>
            </div>
            <div class="content d-flex justify-content-start py-1 my-3">
              <p>{{ leaf82Detail.content }}</p>
            </div>
            <div class="btns d-flex justify-content-center py-3" v-if="leaf82Detail.status_class === '분양대기'">
              <div class="message" v-if="isLoggedIn && username !== this.$route.params.username">
                <router-link :to="{ name : 'messenger' }" class="d-flex justify-content-center" @click = "goChat()">
                  <button class="py-2">채팅하러 가기</button>
                </router-link>
              </div>
              <div class="message" v-if="!isLoggedIn">
                <router-link :to="{}" class="d-flex justify-content-center" @click="loginRequired()">
                  <button class="py-2">채팅하러 가기</button>
                </router-link>
              </div>
            </div>
            <div class="update row d-flex justify-content-center" v-if="this.$route.params.username === username">
              <div class="update-box mx-3 my-2">
                <router-link class="update-a" :to="{ name: 'leaf82Edit' , params: { username: this.$route.params.username , posting_addr: this.$route.params.posting_addr } }">
                  <button class="update-btn">수정</button>
                </router-link>
              </div>
              <div class="delete-box mx-3 my-2">
                <button class="delete-btn" @click="deleteLeaf82(deleteInfo)">삭제</button>
              </div>
            </div>              
          </div>
        </div>
        <div class="col-sm-2 col-0"></div>
      </div>
    </div>
    <div class="col-md-3 col-0"></div>
  </div>
</template>

<script>
import { mapGetters , mapActions } from 'vuex'
import router from '@/router'

export default {
  name: 'Leaf82Detail',
  data() {
    return {
      user: {
      },
      addr: {
      },
      info: {
        id: null,
        user: {
          nickname: '',
          photo: '',
          pk: null,
          username: '',
        },
        addr: {
          id: null,
          sido: '',
          sigungu: '',
        },
        plantname: '',
        photo: '',
        created_at: '',
        content: '',
        price: '',
        category_class: '',
        status_class: '',
        posting_addr: null
      },
      deleteInfo: {
        username: this.$route.params.username,
        posting_addr: this.$route.params.posting_addr
      }
    }
  },
  methods: {
    ...mapActions(['deleteLeaf82', 'setReceiver', 'setLeaf82Plant']),

    fillData() {
      this.user = this.leaf82Detail.user
      this.addr = this.leaf82Detail.addr
      this.info = this.leaf82Detail
      this.info.price = this.info.price.toLocaleString('ko-KR')
      this.info.created_at = this.info.created_at.slice(0,10)
    },

    loginRequired() {
      alert('로그인이 필요한 서비스입니다.')
      router.push({ name: 'login' })
    },

    goChat(){
      this.setReceiver(this.user.username)
      this.setLeaf82Plant(this.info.plantname)
    }
  },

  computed: {
    ...mapGetters(['leaf82Detail', 'currentUser', 'isLoggedIn', 'username']),
  },

  watch: {
    leaf82Detail() {
      this.fillData()
    }
  }
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.main {
  background-color: white;
  border-radius: 15px;
  box-shadow: 0rem 0rem 0.2rem #d2d2d2;
}

.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
  object-fit: cover;
}

.update-btn {
  color: white;
  background-color: #b2c9ab;
  border-radius: 5px;
  border: none;
  width: 5rem;
  height: 1.8rem;
}

.update-btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}


.delete-btn {
  color: black;
  background-color: white;
  border-color: rgb(170, 170, 170);
  border-style: solid;
  color: gray;
  border-radius: 5px;
  border-width: 1px;
  width: 5rem;
  height: 1.8rem;
}

.delete-btn:hover {
  cursor: pointer;
  background-color: #d2d2d2;
  transition: all 0.5s;
}

p {
  margin: 0;
}

.plantname {
  font-size: 2rem;
  font-weight: bold;
}

.plantname .category {
  font-size: 0.8rem;
  background-color: #f7d489ff;
  border-radius: 0.4rem;
  padding: 0.3rem;
  color: white;
  font-weight: normal;
}

.plantname .category-2 {
  font-size: 0.8rem;
  background-color: #b2c9ab;
  border-radius: 0.4rem;
  padding: 0.3rem;
  color: white;
  font-weight: normal;
}

.nickname-route {
  text-decoration: none;
  color: black;
}

.user-photo {
  width: 2.7rem;
  height: 2.7rem;
  border-radius: 10rem;
}

.price p {
  font-weight: bold;
}

.status p {
  font-size: 0.8rem;
  color: gray;
}

.addr {
  font-size: 0.8rem;
  color: gray;
}

.created_at {
  font-size: 0.8rem;
  color: gray;
}

.content p {
  font-size: 0.9rem;
}

.message {
  width: 100%;
}

.message a {
  width: 100%;
  text-decoration: none;
}

.message a button {
  width: 80%;
  background-color: white;
  border-radius: 0.5rem;
  color: gray;
  border-width: 1px;
  border-color: gray;
  border-style: solid;
  font-size: 0.8rem;
}

.message a button:hover {
  cursor: pointer;
  background-color: rgb(206, 206, 206);
  transition: all 0.5s;
}
</style>