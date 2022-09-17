<template>
  <div class="profile-detail mt-5 row">
    <div class="profile-head pt-5 col-lg-4 row">
      <div class="col-2"></div>
      <div class="profile-head-content col-8">
        <div class="profile-img-box">
          <div>
            <img :src="preview" alt="회원님의 사진입니다." class="profile-img">
          </div>
        </div>
        <div class="profile-pic d-flex justify-content-center pt-1">
          <label for="pic-file" class="img-add">
            <span class="material-symbols-outlined img-add-icon">photo_camera</span>
            <span>사진변경</span>
          </label>
          <input type="file" id="pic-file" @change="onInputImage()" accept="image/*" ref="profileImage">
          <span class="px-2">|</span>
          <label for="photo-delete" class="mb-0">
            <span @click="onDeleteImage" class="img-delete-btn img-add">
              <span class="material-symbols-outlined img-add-icon">imagesmode</span>
              <span>초기화</span>
            </span>
          </label>          
        </div>
        <div class="profile-nickname">
          <p class="mb-0">{{ info.nickname }}</p>
        </div>
        <div class="profile-email">
          <p class="">{{ info.email }}</p>
        </div>
        <div class="btns row">
          <div class="profile-update-btn px-0 col-md-3 col-sm-6 d-flex justify-content-center mr-2">
              <button type="submit" class="btn" @click="beforeUpdateProfile(info)">
                저장
              </button>
          </div>
          <div class="profile-cancel-btn px-0 col-md-3 col-sm-6 d-flex justify-content-center">
            <router-link :to="{ name : 'profile' }">
              <button class="btn">
                취소
              </button>
            </router-link>
          </div>
        </div>
      </div>
      <div class="col-2"></div>
    </div>
    <div class="profile-body col-lg-8">
      <div class="profile-info-on mt-5 offset-0 offset-md-3 offset-lg-0">
        <span class="info pr-2">로그인 및 프로필</span>
      </div>
      <div class="comment mt-1">
        <p>계정 보안 및 로그인하는데 문제가 있을 경우 설정을 변경하고 프로필을 관리합니다.</p>
      </div>
      <div class="profile-list row mt-5">
        <div class="profile-list-left d-flex-justify-content-center col-md-6 mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">닉네임</span>
                <span class="material-symbols-outlined icon pr-4">spa</span>
              </div>
              <div class="card-text row pb-5 mx-0">
                <input type="text" class="card-input mx-4" v-model="info.nickname">
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">이메일</span>
                <span class="material-symbols-outlined icon pr-4">email</span>
              </div>
              <div class="card-text row pb-5 mx-0">
                <input type="email" class="card-input mx-4" v-model="info.email">
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
                <input type="text" class="card-input mx-4" v-model="info.phone_number" placeholder="'-'을 제외한 숫자만 입력해주세요.">
              </div>
            </div>
          </div>
        </div>
        <div class="profile-list-right d-flex-justify-content-center col-md-6 row mx-0">
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">비밀번호</span>
                <span class="material-symbols-outlined icon pr-4">lock</span>
              </div>
              <div class="card-text pb-5">
                <router-link :to="{ name : 'updatepassword' }">
                  <span class="card-content pl-4">비밀번호 변경</span>
                </router-link>
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card email">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">주소</span>
                <span class="material-symbols-outlined icon pr-4">home</span>
              </div>
              <div class="card-text pb-5 d-flex justify-content center">
                <input type="text" class="card-addr ml-4" v-model="info.addr" id="sample6_address">
                <input type="hidden" class="card-input mx-4" v-model="info.zip_code" id="sample6_postcode">
                <input type="button" class="find-addr" @click="findAddr" value="주소찾기">
              </div>
            </div>
          </div>
          <div class="container p-0 pb-2">
            <div class="card nickname">
              <div class="card-head d-flex justify-content-between pt-3">
                <span class="kind pl-4">회원탈퇴</span>
                <span class="material-symbols-outlined icon pr-4">potted_plant</span>
              </div>
              <div class="card-text pb-5">
                <button class="signout card-content ml-3" @click="signout()"> 탈퇴하기</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'UpdateProfileDetail',

  data() {
    return {
      info: {
        nickname: '',
        email: '',
        addr: '',
        zip_code: '',
        phone_number: null,

      },
      preview: '',
    }
  },

  methods: {
    ...mapActions(['updateProfile', 'fetchCurrentUser', 'fetchProfile', 'signout']),

    fillOldInfo() {
      this.info = this.profile
    },

    makeImgUrl() {
      this.preview = this.profile.photo
    },

    findAddr() {
      new window.daum.Postcode({
        oncomplete: (data) => {
          if (data.userSelectedType === 'R') {
              this.info.addr = data.roadAddress;
          } else {
              this.info.addr = data.jibunAddress;
          }
          this.info.zip_code = data.zonecode
          document.getElementById('sample6_postcode').value = data.zonecode;
          document.getElementById("sample6_address").value = this.info.addr;
        }
      }).open();
    },

    onInputImage() {
      if (this.$refs.profileImage.files[0].size > 31457280) {
        alert('사진이 너무 큽니다. 30MB보다 작은 사진을 선택해주세요.')
        this.val = this.$refs.profileImage.files[0]
      } else {
        this.info.photo = this.$refs.profileImage.files[0]
        const url = URL.createObjectURL(this.info.photo)
        this.preview = url
      }
    },

    onDeleteImage() {
      this.info.photo = ''
      this.preview = 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/profile.jpg'
    },

    beforeUpdateProfile(info) {
      if (info.nickname.length > 15) {
        alert('닉네임은 최대 15글자입니다.')
      } else if (!info.nickname) {
        alert('닉네임을 입력해주세요.')
      } else if (!info.email) {
        alert('이메일을 입력해주세요')
      } else if (info.phone_number !== null) {
        if (info.phone_number === '') {
          this.info.phone_number = null
          if (!!info.photo && typeof info.photo == 'string' || info.photo instanceof String) {
              info.photo = 'same'
          }
          this.updateProfile(info)
        } else if (info.phone_number.length < 10 || info.phone_number.length > 11) {
          alert('열자리나 열한자리의 휴대전화 번호를 입력해주세요.')
        } else if (
          info.phone_number.slice(0,3) !== '010' && 
          info.phone_number.slice(0,3) !== '011' &&
          info.phone_number.slice(0,3) !== '016' &&
          info.phone_number.slice(0,3) !== '017' &&
          info.phone_number.slice(0,3) !== '018' &&
          info.phone_number.slice(0,3) !== '019'
        ) {
          alert(`연락처 양식을 확인해주세요.`)
        } else {
          for (let num of info.phone_number) {
            if (!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(num)) {
              alert('연락처에 숫자만 입력해주세요.')
            }
          }
          if (!!info.photo && typeof info.photo == 'string' || info.photo instanceof String) {
              info.photo = 'same'
          }
          this.updateProfile(info)
        }
      } else {
        if (!!info.photo && typeof info.photo == 'string' || info.photo instanceof String) {
            info.photo = 'same'
        }
        this.updateProfile(info)
      }
    },
  },

  computed: {
    ...mapGetters(['profile'])
  },

  created() {
    this.fetchProfile()
    this.fillOldInfo()
    this.makeImgUrl()
  },

  watch: {
    profile() {
      this.fillOldInfo()
      this.makeImgUrl()
    }
  }
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

.profile-pic span {
  font-size: 1rem;
  cursor: pointer;
}

.img-add {
  display: flex;
  align-items: center;
}

.img-add-icon {
  font-size: 1.2rem;
  margin-right: .3rem;
}

.img-add:hover {
  cursor: pointer;
  color: #65805d;
  transition: all .2s;
}


input[type="file"] {
  position: absolute;
  width: 0;
  height: 0;
  padding: 0;
  overflow: hidden;
  border: 0;
}

.profile-update-btn .btn{
  border-radius: 15px;
  height: 44px;
  font-size: 1rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.profile-update-btn .btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}

.profile-update-btn .btn:focus {
  outline: none;
}

.profile-cancel-btn a {
  width: 100%;
}

.profile-cancel-btn .btn{
  border-radius: 15px;
  height: 44px;
  font-size: 1rem;
  color: black;
  width: 100%;
}

.profile-cancel-btn .btn:hover {
  cursor: pointer;
  background-color: #d2d2d2;
  transition: all 0.5s;
}

.profile-cancel-btn .btn:focus {
  outline: none;
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

.profile-info-on .info {
  font-size: 2rem;
  font-weight: bold;
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

.card-text .card-input {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 80%;
}

.card-input:focus {
  outline: none;
  color: black;
}

.card-text .card-addr {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.find-addr {

}

.card-text .card-input-nickname {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.card-text .card-input-email {
  color: #7E7E7E;
  font-size: 0.9rem;
  width: 50%;
}

.myleaf-pic {
  padding: 0;
}

.myleaf-pic img {
  width: 10rem;
  height: 10rem;
  border-radius: 5%;
}

.card-content {
  color: #7E7E7E;
  font-size: 0.9rem;
  background: none;
  border: none;
}

.card-content:hover {
  cursor: pointer;
  color: #65805d;
}

.card-content:focus {
  outline: none;
}

.card-text a {
  text-decoration: none;
}
</style>