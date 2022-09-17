<template>
  <div class="pw-detail mt-5">
    <div class="title d-flex justify-content-center pb-5">
      비밀번호 변경
    </div>
    <form class="pw-content" @submit.prevent="changePassword(update_credentials)">
      <div class="row">
        <div class="col-md-4"></div>
        <div class="col-md-4">
          <div class="new1">
            <div class="new1-text">
              <p>새 비밀번호</p>
            </div>
            <div class="new1-input">
              <input type="password" v-model="update_credentials.new_password1">
            </div>
          </div>
          <div class="new2">
            <div class="new2-text">
              <p>비밀번호 확인</p>
            </div>
            <div class="new2-input">
              <input type="password" v-model="update_credentials.new_password2">
            </div>
          </div>
          <div class="submit row mt-5">
            <div class="submit-yes col-6 d-flex justify-content-center">
              <button class="btn" type="submit"> 수정</button>
            </div>
            <div class="submit-no col-6 d-flex justify-content-center">
              <router-link :to="{ name : 'updateprofile' }" class="d-flex justify-content-center">
                <button class="btn">취소</button>
              </router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4"></div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'UpdatePasswordDetail',
  data() {
    return {
      update_credentials: {
        new_password1: '',
        new_password2: '',
      }
    }
  },
  methods: {
    ...mapActions(['changePassword'])
  }
}
</script>

<style scoped>
.pw-detail {
  font-family: 'SUIT' sans-serif;
  background-color: #FFFFFFCC;
  padding-top: 7rem;
  box-shadow: 0rem 0rem 0.2rem #d2d2d2;
  border-radius: 15px;
}

div {
  margin: 0;
}

.title  {
  font-size: 2rem;
  font-weight: bold;
}

p {
  margin: 0%;
}

.new1 {
  margin-bottom: 1rem;
}

.new1-text {
  font-size: 0.9rem;
  color: #7E7E7E;
}

.new1-input input {
  width: 100%;
  box-shadow: 0.1rem 0.1rem 0.1rem #CDCDCD;
  border-style: solid;
  border-color: #7E7E7E;
  border-width: 1px;
}

.new2 {
  margin-bottom: 1rem;
}

.new2-text {
  font-size: 0.9rem;
  color: #7E7E7E;
}

.new2-input input {
  width: 100%;
  box-shadow: 0.1rem 0.1rem 0.1rem #CDCDCD;
  border-style: solid;
  border-color: #7E7E7E;
  border-width: 1px;
}

input:focus {
  outline: none;
}

.submit-yes .btn {
  background-color: #b2c9ab;
  color: white;
}

.submit-yes .btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}

.submit-no a {
  width: 100%;
  text-decoration: none;
}

.submit-no a .btn:hover {
  cursor: pointer;
  background-color: #d2d2d2;
  transition: all 0.5s;
}

.btn {
  width: 80%;
}
</style>