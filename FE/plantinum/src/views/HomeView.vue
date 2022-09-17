<template>
  <div class="boxes" v-if="device === 'PC'">
    <div class="first-box">
      <nav-bar></nav-bar>
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>반려식물 통합 관리 플랫폼</p>
            <p>플랜티넘</p>
          </div>
          <div class="text-detail">
            <p>반려식물 케어부터 분양정보까지,</p>
            <p>사람들과 함께 아름다운 집을 만들어요.</p>
          </div>
          <div class="text-hello" v-if="isLoggedIn">
            <p>안녕하세요, <b>{{ currentUser.nickname }}</b> 님</p>
          </div>
          <div class="btnbox" v-if="!isLoggedIn">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'login' }">
                  <button class="btn">로그인 / 회원가입</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="second-box row">
      <div class="col-md-6 col-sm col d-flex align-items-center">
        <img src="../assets/HomeView/main_pic_2_small.jpg" alt="">
      </div>
      <div class="row col-md-6 col-12 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>오늘은 상태가 어떠니?</p>
            <p>식물이 들려주는 이야기</p>
          </div>
          <div class="text-detail">
            <p>소중한 반려식물의 변화를</p>
            <p>놓치지 않을 수 있어요.</p>
            <br>
            <br>
            <p>언제 어디서든 반려 식물과 함께하세요.</p>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <div class="new-box" v-if="isLoggedIn">
                  <router-link :to="{ name: 'myplant', params: { username: username } }" v-if="!!username">
                    <button class="btn">내 식물</button>
                  </router-link>
                </div>
                <router-link :to="{ name: 'login' }" v-if="!isLoggedIn">
                  <button class="btn">내 식물</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="third-box">
      <div class="row col-md-6 d-flex justify-content-center">
        <div class="contentbox">
          <div class="text-main">
            <p>여러분의 식물을</p>
            <p>분양해주세요</p>
          </div>
          <div class="text-sub">
            <span>"보내는 마음은 아쉬웠지만,</span>
            <br>
            <span class="d-flex justify-content-end">좋은 분을 만난거 같았어요."</span>
          </div>
          <div class="text-detail">
            <p>서울에 거주하시는 진아님은</p>
            <p>얼마전 아비스를 유민님께 분양해주었답니다.</p>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'leaf82' }">
                  <button class="btn">잎팔이</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-sm col d-flex align-items-center justify-content-center">
        <img src="../assets/HomeView/main_pic_3.jpg" alt="잎팔이 소개 사진입니다.">
      </div>
    </div>

    <div class="fourth-box">
      <div class="title-supool d-flex justify-content-center align-items-center">
        <p>Supool</p>
      </div>
      <div class="row">
        <div class="col-md-6 col-sm col d-flex align-items-center justify-content-center">
          <img src="../assets/HomeView/main_pic_4.jpg" alt="Supool 소개 사진입니다.">
        </div>
        <div class="row col-md-6 d-flex justify-content-center">
          <div class="contentbox">
            <div class="text-main">
              <p>토양상태를 파악해</p>
              <p>자동으로 길러주는 나만의</p>
              <p>수풀</p>
            </div>
            <div class="text-detail">
              <p>수풀은 토양의 습도, 주변의 온도를 분석하여</p>
              <p>자동 급수하며 식집사들을 도와주고 있습니다.</p>
              <br>
              <br>
              <p>스마트한 반려식물 키우기</p>
              <span class="supool">수풀</span>
              <span class="extra">이 함께합니다.</span>
            </div>
            <div class="btnbox">
              <div class="btn-border">
                <div class="login d-flex justify-content-center">
                  <router-link :to="{ name: 'home' }">
                    <button class="btn">comming soon</button>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  <div class="boxes" v-if="device === 'Tablet'">
    <div class="first-box-tablet">
      <nav-bar></nav-bar>
      <div class="row d-flex justify-content-center">
        <div class="contentbox-tablet">
          <div class="text-main-tablet">
            <p>반려식물 통합 관리 플랫폼</p>
            <p>플랜티넘</p>
          </div>
          <div class="text-detail-tablet">
            <p>반려식물 케어부터 분양정보까지,</p>
            <p>사람들과 함께 아름다운 집을 만들어요.</p>
          </div>
          <div class="text-hello-tablet" v-if="isLoggedIn">
            <p>안녕하세요, <b>{{ currentUser.nickname }}</b> 님</p>
          </div>
          <div class="btnbox" v-if="!isLoggedIn">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'login' }">
                  <button class="btn-tablet">로그인 / 회원가입</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="second-box-tablet">
      <div class="col-md-6 d-flex align-items-center">
        <img src="../assets/HomeView/main_pic_2_tablet.jpg" alt="내 식물 소개 사진입니다.">
      </div>
      <div class="col-md-6 d-flex justify-content-center">
        <div class="contentbox-tablet">
          <div class="text-main-tablet">
            <p>오늘은 상태가 어떠니?</p>
            <p>식물이 들려주는 이야기</p>
          </div>
          <div class="text-detail-tablet">
            <p>소중한 반려식물의 변화를</p>
            <p>놓치지 않을 수 있어요.</p>
            <br>
            <br>
            <p>언제 어디서든 반려 식물과 함께하세요.</p>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <div class="new-box" v-if="isLoggedIn">
                  <router-link :to="{ name: 'myplant', params: { username: username } }" v-if="!!username">
                    <button class="btn-tablet">내 식물</button>
                  </router-link>
                </div>
                <router-link :to="{ name: 'login' }" v-if="!isLoggedIn">
                  <button class="btn-tablet">내 식물</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="third-box-tablet">
      <div class="row col-6 d-flex justify-content-center">
        <div class="contentbox-tablet">
          <div class="text-main-tablet">
            <p>여러분의 식물을</p>
            <p>분양해주세요</p>
          </div>
          <div class="text-sub-tablet">
            <span>"보내는 마음은 아쉬웠지만,</span>
            <br>
            <span class="d-flex justify-content-end">좋은 분을 만난거 같았어요."</span>
          </div>
          <div class="text-detail-tablet">
            <p>서울에 거주하시는 진아님은</p>
            <p>얼마전 아비스를 유민님께 분양해주었답니다.</p>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'leaf82' }">
                  <button class="btn-tablet">잎팔이</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-6 d-flex align-items-center justify-content-center">
        <img src="../assets/HomeView/main_pic_3.jpg" alt="잎팔이 소개 사진입니다.">
      </div>
    </div>

    <div class="fourth-box-tablet">
      <div class="title-supool d-flex justify-content-center align-items-center">
        <p>Supool</p>
      </div>
      <div class="row d-flex justify-content-center">
        <div class="contentbox-tablet">
          <div class="text-main-tablet">
            <p>토양상태를 파악해</p>
            <p>자동으로 길러주는 나만의</p>
            <p>수풀</p>
          </div>
          <div class="text-detail-tablet">
            <p>수풀은 토양의 습도, 주변의 온도를 분석하여</p>
            <p>자동 급수하며 식집사들을 도와주고 있습니다.</p>
            <br>
            <br>
            <p>스마트한 반려식물 키우기</p>
            <div class="d-flex justify-content-center">
              <span class="supool">수풀</span>
              <span class="extra">이 함께합니다.</span>
            </div>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'home' }">
                  <button class="btn-tablet">comming soon</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
  <div class="boxes" v-if="device === 'Mobile'">
    <div class="first-box-mobile">
      <nav-bar></nav-bar>
      <div class="row d-flex justify-content-center">
        <div class="contentbox-mobile">
          <div class="text-main-mobile">
            <p>반려식물 통합 관리 플랫폼</p>
            <p>플랜티넘</p>
          </div>
          <div class="text-detail-mobile">
            <p>반려식물 케어부터 분양정보까지,</p>
            <p>사람들과 함께 아름다운 집을 만들어요.</p>
          </div>
          <div class="text-hello-mobile" v-if="isLoggedIn">
            <p>안녕하세요, <b>{{ currentUser.nickname }}</b> 님</p>
          </div>
          <div class="btnbox" v-if="!isLoggedIn">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'login' }">
                  <button class="btn-mobile">로그인 / 회원가입</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="second-box-mobile">
      <div class="d-flex justify-content-center">
        <div class="contentbox-mobile">
          <div class="text-main-mobile">
            <p>오늘은 상태가 어떠니?</p>
            <p>식물이 들려주는 이야기</p>
          </div>
          <div class="text-detail-mobile">
            <p>소중한 반려식물의 변화를</p>
            <p>놓치지 않을 수 있어요.</p>
            <br>
            <br>
            <p>언제 어디서든 반려 식물과 함께하세요.</p>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <div class="new-box" v-if="isLoggedIn">
                  <router-link :to="{ name: 'myplant', params: { username: username } }" v-if="!!username">
                    <button class="btn-mobile">내 식물</button>
                  </router-link>
                </div>
                <router-link :to="{ name: 'login' }" v-if="!isLoggedIn">
                  <button class="btn-mobile">내 식물</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="third-box-mobile">
      <div class="contentbox-mobile">
        <div class="text-main-mobile">
          <p>여러분의 식물을</p>
          <p>분양해주세요</p>
        </div>
        <div class="text-sub-mobile pl-4">
          <span>"보내는 마음은 아쉬웠지만,</span>
          <br>
          <span class="d-flex justify-content-end pr-4">좋은 분을 만난거 같았어요."</span>
        </div>
        <div class="text-detail-mobile">
          <p>서울에 거주하시는 진아님은</p>
          <p>얼마전 아비스를 유민님께 분양해주었답니다.</p>
        </div>
        <div class="btnbox">
          <div class="btn-border">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: 'leaf82' }">
                <button class="btn-mobile">잎팔이</button>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="fourth-box-mobile">
      <div class="title-supool d-flex justify-content-center align-items-center">
        <p>Supool</p>
      </div>
      <div class="row d-flex justify-content-center">
        <div class="contentbox-mobile">
          <div class="text-main-mobile">
            <p>토양상태를 파악해</p>
            <p>자동으로 길러주는 나만의</p>
            <p>수풀</p>
          </div>
          <div class="text-detail-mobile">
            <p>수풀은 토양의 습도, 주변의 온도를 분석하여</p>
            <p>자동 급수하며 식집사들을 도와주고 있습니다.</p>
            <br>
            <br>
            <p>스마트한 반려식물 키우기</p>
            <div class="d-flex justify-content-center">
              <span class="supool">수풀</span>
              <span class="extra">이 함께합니다.</span>
            </div>
          </div>
          <div class="btnbox">
            <div class="btn-border">
              <div class="login d-flex justify-content-center">
                <router-link :to="{ name: 'home' }">
                  <button class="btn-mobile">comming soon</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'HomeView',

  components: {
    NavBar
  },

  computed: {
    ...mapGetters(['username', 'isLoggedIn', 'currentUser', 'device']),
  },
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.first-box {
  height: 1117px;
  background: url("../assets/HomeView/background_img.jpg") bottom left;
  background-size: cover;
}

.first-box-tablet {
  height: 800px;
  background: url('../assets/HomeView/main_pic_1.jpg') top left;
  background-size: cover;
}

.first-box-mobile {
  height: 600px;
  background: url('../assets/HomeView/main_pic_1.jpg') bottom left;
  background-size: cover;
}

.second-box {
  height: 1117px;
  background-color: white;
  display: flex;
  flex-direction: row;
}

.second-box-tablet {
  height: 800px;
  background-color: white;
  display: flex;
  flex-direction: row;
}

.second-box-tablet img {
  width: 100%;
}

.second-box-mobile {
  height: 600px;
  background-color: white;
}

.third-box {
  height: 1117px;
  background-color: #F3F3F3;
  display: flex;
  flex-direction: row;
}

.third-box-tablet {
  height: 800px;
  background-color: #F3F3F3;
  display: flex;
  flex-direction: row;
}

.third-box-tablet img {
  width: 100%;
}

.third-box-mobile {
  height: 599px;
  background-color: #F3F3F3;
  padding-top: 1px;
}

.fourth-box {
  height: 1117px;
  background-color: #F8F5EE;
  display: flex;
  flex-direction: column;
}

.fourth-box-tablet {
  height: 800px;
  background-color: #F8F5EE;
}

.fourth-box-mobile {
  height: 700px;
  background-color: #F8F5EE;
}

a {
  text-decoration-line: none;
}

.contentbox {
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.contentbox-tablet {
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.contentbox-mobile {
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.second-box .contentbox {
  margin-bottom: 3rem;
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.third-box .contentbox {
  margin-bottom: 3rem;
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.fourth-box .contentbox {
  margin-bottom: 3rem;
  font-family: 'SUIT', sans-serif;
  padding-left: 2rem;
  padding-right: 2rem;
}

.text-main {
  margin-top: 12rem;
  margin-bottom: 4rem;
}

.text-main-tablet {
  margin-top: 8rem;
  margin-bottom: 4rem;
}

.text-main-mobile {
  margin-top: 6rem;
  margin-bottom: 4rem;
}

.text-main p {
  margin-bottom: 0;
  font-size: 3rem;
  font-weight: bold;
}

.text-main-tablet p {
  margin-bottom: 0;
  font-size: 2rem;
  font-weight: bold;
  display: flex;
  justify-content: center;
}

.text-main-mobile p {
  margin-bottom: 0;
  font-size: 1.2rem;
  font-weight: bold;
  display: flex;
  justify-content: center;
}

.text-sub {
  margin-bottom: 5rem;
  font-size: 1.8rem;
  font-weight: bold;
}

.text-sub-tablet {
  margin-bottom: 5rem;
  font-size: 1.3rem;
  font-weight: bold;
}

.text-sub-mobile {
  margin-bottom: 5rem;
  font-size: 0.9rem;
  font-weight: bold;
}

.text-detail {
  margin-bottom: 7rem;
}

.text-detail p {
  margin-bottom: 0;
  font-size: 1.5rem;
}

.text-detail-tablet {
  margin-bottom: 7rem;
}

.text-detail-tablet p {
  margin-bottom: 0;
  font-size: 1.1rem;
  display: flex;
  justify-content: center;
}

.text-detail-mobile {
  margin-bottom: 7rem;
}

.text-detail-mobile p {
  margin-bottom: 0;
  font-size: 0.9rem;
  display: flex;
  justify-content: center;
}

.text-detail span {
  font-size: 1.5rem;
}

.text-detail-tablet span {
  font-size: 1.1rem;
}

.text-detail-mobile span {
  font-size: 1rem;
}

.text-detail .supool {
  font-weight: bold;
}

.text-detail-tablet .supool {
  font-weight: bold;
}

.text-detail-mobile .supool {
  font-weight: bold;
}


.text-hello {
  font-size: 1.5rem;
}

.text-hello-tablet {
  display: flex;
  justify-content: center;
  font-size: 1.3rem;
}

.text-hello-mobile {
  font-size: 0.9rem;
}

.new-box {
  width: 50%;
}

.btn {
  border-radius: 5px;
  height: 53px;
  font-size: 1.3rem;

  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.btn:hover {
  background-color: #65805d;
  color: #ffffff;
}

.btn-tablet {
  border: none;
  border-radius: 5px;
  height: 2.5rem;
  font-size: 0.8rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.btn-tablet:hover {
  background-color: #65805d;
  color: #ffffff;
}

.btn-mobile {
  border: none;
  border-radius: 5px;
  height: 2.5rem;
  font-size: 0.8rem;
  background-color: #b2c9ab;
  color: white;
  width: 100%;
}

.btn-mobile:hover {
  background-color: #65805d;
  color: #ffffff;
}

.btnbox a {
  width: 50%;
}

.fourth-box .btn a {
  width: 75%;
}

.second-box img {
  width: 100%;
  height: 50%;
  margin-left: 0;
}

.third-box img {
  width: 60%;
  height: 70%;
  margin: auto;
}

.fourth-box img {
  width: 70%;
  height: 50%;
  background-position: auto;
}

.title-supool {
  height: 5rem;
}

.title-supool p {
  margin-top: 5rem;
  margin-bottom: 0;
  font-size: 4rem;
  font-family: 'Dancing Script', cursive;
}
</style>>