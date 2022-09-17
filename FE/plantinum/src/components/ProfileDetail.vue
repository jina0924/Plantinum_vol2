<template>
  <div class="profile-detail mt-5 row">
    <div class="profile-head pt-5 col-lg-4 row">
      <div class="col-2"></div>
      <div class="profile-head-content col-8">
        <div class="profile-img-box">
          <img :src="profile.photo" alt="temporary img" class="profile-img">
        </div>
        <div class="profile-nickname">
          <p class="mb-0">{{ profile.nickname }}</p>
        </div>
        <div class="profile-email">
          <p class="">{{ profile.email }}</p>
        </div>
        <div class="profile-update-btn" v-if="!myleaf82">
          <router-link :to="{ name : 'updateprofile' }">
            <button class="btn">
              회원 정보 수정
            </button>
          </router-link>
        </div>
      </div>
      <div class="col-2"></div>
    </div>
    <div class="profile-body col-lg-8">
      <div class="px-3" v-if="!myleaf82">
        <div class="profile-info-on mt-5 offset-0 offset-md-3 offset-lg-0" v-if="!myleaf82">
          <span class="info pr-2">로그인 및 프로필</span>
          <span class="divider">|</span>
          <span class="myleaf82 pl-2" @click="changeMyleaf82">내 잎팔이 글</span>
        </div>

        <div class="comment mt-1 offset-0 offset-md-1 offset-lg-0" v-if="!myleaf82">
          <p>계정 보안 및 로그인하는데 문제가 있을 경우 설정을 변경하고 프로필을 관리합니다.</p>
        </div>
      </div>
      <div class="profile-list row mt-5" v-if="!myleaf82">
        <div class="profile-list-left d-flex-justify-content-center col-md-6 mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">닉네임</span>
                <span class="material-symbols-outlined icon pr-4">spa</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.nickname }}</span>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">이메일</span>
                <span class="material-symbols-outlined icon pr-4">email</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.email }}</span>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">연락처</span>
                <span class="material-symbols-outlined icon pr-4">phone</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.phone_number }}</span>
              </div>
            </div>
          </div>
        </div>
        <div class="profile-list-right d-flex-justify-content-center col-md-6 row mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">함께한 시간</span>
                <span class="material-symbols-outlined icon pr-4">calendar_month</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.dday }} 일 째</span>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">주소</span>
                <span class="material-symbols-outlined icon pr-4">home</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.addr }}</span>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">내 식물</span>
                <span class="material-symbols-outlined icon pr-4">potted_plant</span>
              </div>
              <div class="card-text pb-5">
                <span class="card-content pl-4">{{ profile.myplant_count }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class=" px-3" v-if="myleaf82">
        <div class="profile-myleaf82-on mt-5 offset-0 offset-md-3 offset-lg-0" v-if="myleaf82">
          <span class="info pr-2" @click="changeMyleaf82">로그인 및 프로필</span>
          <span class="divider">|</span>
          <span class="myleaf82 pl-2">내 잎팔이 글</span>
        </div>
        <div class="comment mt-1 offset-0 offset-md-4 offset-lg-0" v-if="myleaf82">
          <p>회원님이 등록한 잎팔이 글 목록입니다.</p>
        </div>
      </div>
      <div class="myleaf-list row mt-5 d-flex justify-content-center" v-if="myleaf82">
        <div class="myleaf-pic m-2 d-flex justify-content-center" v-for="leaf82 in leaf82Set" :key="leaf82.pk">
          <router-link :to="{ name: 'leaf82Detail' , params: { username: username ,posting_addr: leaf82.posting_addr } }">
            <img :src="leaf82.photo" :alt="`${leaf82.plantname} 잎팔이 게시글 사진입니다`">
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'ProfileDetail',

  data() {
    return {
      myleaf82: false,
    }
  },

  methods: {
    changeMyleaf82() {
      this.myleaf82 = !this.myleaf82
    },
  },

  computed: {
    ...mapGetters(['profile', 'leaf82Set', 'username'])
  },
}
</script>

<style scoped>
.profile-detail {
  font-family: 'SUIT' sans-serif;
  background-color: #FFFFFFCC;
  padding-top: 7rem;
  border-radius: 15px;
  box-shadow: 0rem 0rem 0.2rem #d2d2d2;
}

.profile-img-box {
  position: relative;
  width: 100%;
  padding-bottom: 100%;
}

.profile-img-box img {
  width: 100%;
  height: 100%;
  position: absolute;
  border-radius: 50%;
  object-fit: cover;
}

.btn{
  border-radius: 15px;
  height: 44px;
  font-size: 1rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.btn:hover{
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}

.profile-nickname {
  font-size: 1.2rem;
  font-weight: bold;
  padding-top: 2rem;
}

.profile-email {
  font-size: 1rem;
  color: #7E7E7E;
}

.divider {
  font-size: 2rem;
}

.profile-info-on .info {
  font-size: 2rem;
  font-weight: bold;
}

.profile-info-on .myleaf82 {
  font-size: 1.7rem;
}

.profile-info-on .myleaf82 {
  color: #7E7E7E;
}

.profile-info-on .myleaf82:hover {
  cursor: pointer;
  color:black
}

.profile-myleaf82-on .myleaf82 {
  font-size: 2rem;
  font-weight: bold;
}

.profile-myleaf82-on .info {
  font-size: 1.7rem;
}

.profile-myleaf82-on .info {
  color: #7E7E7E;
}

.profile-myleaf82-on .info:hover {
  cursor: pointer;
  color:black
}

.container {
  margin: 0;
}

.comment {
  color: #7E7E7E;
}

.card {
  border-radius: 15px;
  box-shadow: 0.2rem 0.2rem 0.2rem #CDCDCD;
  width: 100%;
}

.card-head .kind {
  font-weight: bold;
  font-size: 1.1rem;
}

.icon {
  font-size: 1.5rem;
  color: #b2c9ab;
}

.card-text .card-content {
  color: #7E7E7E;
  font-size: 0.9rem;
}

.myleaf-pic {
  padding: 0;
}

.myleaf-pic img {
  width: 10rem;
  height: 10rem;
  border-radius: 5%;
  object-fit: cover;
}
</style>