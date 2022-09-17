<template>
	<div class="section background">
		<div class="container my-0">
			<div class="row full-height justify-content-center">
				<div class="col-12 text-center align-self-center py-5">
					<div class="section pb-5 pt-5 pt-sm-2 text-center">
						<h5 class="mb-0 pb-3"><span>로그인</span><span>회원가입</span></h5>
            <input class="checkbox" type="checkbox" id="reg-log" name="reg-log" @click="fetchAuthError(null)">
            <label for="reg-log"></label>
						<div class="card-3d-wrap mx-auto">
							<div class="card-3d-wrapper">
								<div class="card-front">
									<div class="center-wrap">
										<div class="section text-center">
											<h4 class="mb-4 pb-3">로그인</h4>
                      <form @submit.prevent="login(login_credentials)">
                        <div class="form-group">
                          <input v-model="login_credentials.username" type="text" name="login-username" class="form-style" placeholder="Your ID" id="login-username" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">person</span>
                        </div>
                        <div class="form-group mt-2">
                          <input v-model="login_credentials.password" type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">lock</span>
                        </div>
                        <button class="mt-4 btn" type=submit>로그인</button>
                      </form>
                      <p class="mb-0 mt-4 text-center">
                        <router-link :to="{ name: 'home'}" class="link">메인 화면으로 돌아가기</router-link>
                      </p>
                    </div>
                  </div>
                </div>
								<div class="card-back">
									<div class="center-wrap">
										<div class="section text-center">
											<h4 class="mb-4">회원가입</h4>
                      <form @submit.prevent="signup(signup_credentials)">
                        <div class="form-group">
                          <input v-model="signup_credentials.username" type="text" name="username" class="form-style" placeholder="Your ID" id="username" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">person</span>
                        </div>	
                        <div class="form-group mt-2">
                          <input v-model="signup_credentials.email" type="email" name="signup-email" class="form-style" placeholder="Your Email" id="signup-email" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">alternate_email</span>
                        </div>	
                        <div class="form-group mt-2">
                          <input v-model="signup_credentials.password1" type="password" name="signuppass1" class="form-style" placeholder="Your Password" id="signuppass1" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">lock</span>
                        </div>
                        <div class="form-group mt-2">
                          <input v-model="signup_credentials.password2" type="password" name="signuppass2" class="form-style" placeholder="Confirm Password" id="signuppass2" autocomplete="off">
                          <span class="material-symbols-outlined input-icon">lock</span>
                        </div>
                        <button class="mt-4 btn" type=submit>회원가입</button>
                      </form>
                    </div>
                  </div>
                </div>
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
  name: 'LoginView',

  data() {
    return {
      login_credentials: {
        username: '',
        password: '',
      },
      signup_credentials: {
        username: '',
        email: '',
        password1: '',
        password2 : '',
      },
      emailerror : ''
    }
  },

  computed: {
    ...mapGetters(['authError',]),
  },
  
  methods: {
    ...mapActions(['login', 'signup', 'fetchAuthError'])
  },
}
</script>

<style scoped>
.background {
  background-image: url('@/assets/Login/login_bg.jpg');
}

body{
	font-weight: 300;
	font-size: 15px;
	line-height: 1.7;
	color: #a17c6b;
	background-color: #ece4ce;
	overflow-x: hidden;
}
a {
	cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
	text-decoration: none;
}
.link {
  color: #c4c3ca;
}
.link:hover {
  color: #f7d489;
}
p {
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  font-weight: 600;
}
h5 span{
  padding: 0 20px;
  text-transform: uppercase;
  font-weight: 500;
}
.section{
  position: relative;
  width: 100%;
  display: block;
}
.full-height{
  min-height: 100vh;
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: absolute;
  left: -9999px;
}
.checkbox:checked + label,
.checkbox:not(:checked) + label{
  position: relative;
  display: block;
  text-align: center;
  width: 60px;
  height: 16px;
  border-radius: 8px;
  padding: 0;
  margin: 10px auto;
  cursor: pointer;
  background-color: #65805d;
}
.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before{
  position: absolute;
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  color: #ffffff;
  background-color: #b2c9ab;
  content: '\2196';
  z-index: 20;
  top: -10px;
  left: -10px;
  line-height: 36px;
  text-align: center;
  font-size: 1rem;
  font-weight: 800;
  transition: all 0.5s ease;
}
.checkbox:checked + label:before {
  transform: translateX(44px) rotate(-270deg);
}

.card-3d-wrap {
  position: relative;
  width: 440px;
  max-width: 100%;
  height: 400px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}
.card-3d-wrapper {
  width: 100%;
  height: 100%;
  position:absolute;    
  top: 0;
  left: 0;  
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out; 
}
.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 300%;
  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}
.center-wrap{
  position: absolute;
  width: 100%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}

.form-group{ 
  position: relative;
  display: block;
    margin: 0;
    padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: rgb(91, 91, 91);
  background-color: #ffffff;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}

.form-style::placeholder {
  color: #c4c3ca;
}

.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #b2c9ab;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.btn{  
  border-radius: 5px;
  height: 44px;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #b2c9ab;
  color: #ffffff;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #65805d;
  color: #ffffff;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #65805d;
  color: #ffffff;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}

</style>