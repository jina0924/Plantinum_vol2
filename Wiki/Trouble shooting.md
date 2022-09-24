## Trouble shooting

[TOC]

**목차**

[1. FE](#1-fe)
[2. BE](#2-be)
[3. HW](#3-hw)
[4. server](#4-server)
[5. 기타](#5-기타)



### 1. FE

#### div 태그에 span태그를 수평 중앙정렬🎈

```html
<template>
  <div class="boxes">
    <!-- first box -->
    <div class=first-box>
      <div class="row">
        <div class="col-md-3 home-logo">
          <router-link :to="{ name: 'home' }">
            <span>
              Plantinum
            </span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
  ...
</template>
```

```css
  .home-logo {
    text-align: center;
    padding-top: 1rem;
    padding-bottom: 1rem;
    text-decoration: none;
  }
```

- 포인트
  - 스타일에도 넣을 수 있고,
  - 클래스에 d-flex justify-content-center로도 가능!



---

#### 버튼에 스타일 주기🎆

```html
<template>
  <div class="boxes">
    <div class="first-box">
      ...
      <div class="btnbox row" v-if="!isLoggedIn">
        <!-- <div class="btnbox row"> -->
          <div class="btn-border col-6">
            <div class="login d-flex justify-content-center">
              <router-link :to="{ name: login }">
                <button class="btn">로그인</button>
              </router-link>
            </div>
          </div>
        </div>
      ...
    </div>
  </div>  
</template>
```

```css
  .btn{
    border-radius: 5px;
    height: 44px;
    font-size: 1rem;
    background-color: #b2c9ab;
    color: white;
    width: 100%;
  }

  .btnbox a {
    width: 50%;
  }
```

- 기능

  1. 버튼 클릭하면 해당 링크로 이동

- 포인트

  1. 버튼 생성 후 위치를 정하기 위해 justify-content-center

  2. 높이(height) 조절

  3. border-radius를 통해 버튼 둥글기 조절

  4. 부모  div인 btn-border가 가지고 있는 col-6에서 버튼의 너비(width)를 100%로 꽉 채운 후, 그 속에 있는 a 태그 역할을 하는 router-link의 너비(width)는  50%로 채움



---

#### 배경 이미지 투명도 조절🧨

```css
<style scoped>
.profile {
  background-image: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
  height: 1117px;
}
</style>
```

- 기능
  - 배경 `이미지만` 투명으로 설정하고 싶다!
  - **opacity로 조절하면 글자도 투명해짐...ㅠㅠ**



---

#### input[type="file"] 커스터마이징🎉

```vue
<template>
  ...
  <div class="profile-pic d-flex justify-content-center">
    <label for="pic-file">
      <span class="material-symbols-outlined">
        photo_camera
   	  </span>
      <span>
        사진 변경하기
      </span>
    </label>
      <input type="file" id="pic-file">
    </div>
  ...
</template>
```

- 기능
  - 기존 멋없는 input 태그가 없어지고,
  - label로 묶인 항목이 표시됨



---

#### search-bar 검색버튼 input tag 안에 들어간 것 같은 효과 주기🎐

```vue
<template>
...
  <div class="search-box col-sm-8 col-md-4 col-12 d-flex justify-content-center">
    <input class="search-input" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="beforeSearch()">        
    <button class="search-btn" type="submit" @click="beforeSearch()">
      <span class="material-symbols-outlined d-flex align-items-center justify-content-center">search</span>
    </button>
  </div>
...
</template>

<style>
.search-box {
  position: relative;
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
}

.search-input {
  width: 90%;
  height: 2.5rem;
  border: 0;
  border-top-left-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
  font-size: 1.2rem;
}

.search-btn {
  width: 10%;
  border: 0;
  background-color: white;
  border-top-right-radius: 0.5rem;
  border-bottom-right-radius: 0.5rem;
  color: black;
}
</style>
```

- 효과
  - 서치바에 그림자를 두어 입체감 주기
    - 최상단 div에 주고 싶은 border-radius와 box-shadow  입력
  - 인풋 좌측만 border-radius
  - 버튼 우측만 border-radius
  - 버튼 배경 색 white로 변경


---

#### v-on click을 활용해 렌더링되는 화면 교체하기🎇

```vue
<template>
  ...
  <span @click="changeMyleaf82">
      내 잎팔이 글
  </span>
  ...
</template>
<script>
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
  }
}    
</script>
```

- 기능
  - 버튼 클릭시 관련 정보 보여주기
    - 로그인 및 회원정보 수정 | 내가 등록한 게시글 

- 포인트
  1. 보여줄 화면을 인식하는 값(myleaf82)을 데이터에 저장
  2. methods에 그 값을 변경해주는 changeMyleaf82() 함수 지정
     - ~~method~~ --> methods...
  3. 클릭시 이동시켜줄 span 태그 지정



---

#### vuex 관리하기(로그인 , 로그아웃 사이클)🎃

```js
import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export const Account = {
  // state: {
  // },
  // getters: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    authError: null,
    profile: {},
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    profile: state => state.profile,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => state.profile = profile,
  },

  actions: {
      
    // mutations을 호출할 actions
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')
    },

    resetCurrentUser({ commit }) {
      commit('SET_CURRENT_USER', {})
    },

    resetProfile({ commit }) {
      commit('SET_PROFILE', {})
    },

    // 홈페이지에서 로그인이나 로그아웃 버튼이 눌릴 때 시행될  actions
    login({ commit, dispatch }, credentials) {
      axios ({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        dispatch('fetchProfile')
        router.push({ name: 'home' })
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(() => {
        dispatch('removeToken')
        dispatch('resetCurrentUser')
        dispatch('resetProfile')
        alert('logout 되었습니다')
        router.push({ name: 'home' })
      })
      // 에러 발생 시 어떻게 할 지 고민해야 함
      .catch(err => {
        alert('잘못된 접근입니다.')
        console.log(err.response)
      })
    },

      
    // 로그인시 내부적으로 작동할 actions 
    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => commit('SET_CURRENT_USER', res.data))
        .catch(err => {
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    fetchProfile({ commit, getters },) {
      axios({
        url: drf.accounts.profile(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_PROFILE', res.data)
      })
      .catch(err => {
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },
  }
}
```

- 기능
  - 로그인 시 사용자 정보 및 프로필 페이지에 활용될 정보 받아옴
  - 로그아웃 시 토큰, 사용자 정보, 프로필 정보를 지워서 해당 페이지에 접근해도 띄어주는 정보가 없어짐
    - 1차적으로 접근을 못하게 막아야함



- 포인트

  1. 로그인 클릭했을 때, 백엔드로 credentials로 묶어 로그인 정보와 함께 axios 요청을 보냄

  2. 백엔드에서 response를 보내줌
  3. 받아온 토큰 값을 saveToken actions를 호출해 state의 token에저장해주고,
     1. saveToken actions는 SET_TOKEN mutations를 호출해 state의 token 값을 수정
  4.  fetchCurrentUser actions를 실행함
     1. 로그인이 되어있다면 백엔드에 유저 정보를 요청함
     2. 받아온 유저정보를 SET_CURRENT_USER mutations를 호출해 state의 currentUser 값을 수정
  5. fetchProfile actions를 실행함
     1. 위와 같은 형태
  6. router.push를 통해 home이름을 가진 라우터로 이동시킴(로그인 후 홈화면 이동)
  7. 에러가 발생했다면 어스에러 실행...

---

#### 로그인시 로그인, 회원 정보 vuex store에 저장하여 유지하고 로그아웃시 삭제🎊

- App.vue(가장 상위항목에서 실행)
  - 하위항목에서 항상 차있음
- logout actions를 실행하면서 resetToken과 resetCurrentUser, resetProfile을 실행하여 store에서 삭제



---

#### Vue.js에서 다음 주소찾기 api 활용하기🎄

```vue
<template>
...
  <div class="card-text pb-5">
    <input type="text" class="card-input mx-4" v-model="info.addr" id="sample6_address">
    <input type="text" class="card-input mx-4" v-model="info.zip_code" id="sample6_postcode">
    <input type="button" @click="findAddr" value="주소찾기">
  </div>
...
</template>

<script>
...

  methods: {
    findAddr() {
      new window.daum.Postcode({
          oncomplete: (data) => {
                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

                //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
              if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                  this.info.addr = data.roadAddress;
              } else { // 사용자가 지번 주소를 선택했을 경우(J)
                  this.info.addr = data.jibunAddress;
              }
              this.info.zip_code = data.zonecode

                // 우편번호와 주소 정보를 해당 필드에 넣는다.
              document.getElementById('sample6_postcode').value = data.zonecode;
              document.getElementById("sample6_address").value = this.info.addr;
          }
      }).open();
  }

...
</script>
```

- 기능
  - 주소찾기 버튼 클릭시 주소 검색 팝업창 오픈
  - 검색 후 선택한 주소 input 태그로 불러오기
  - v-model로 연동하여 연결



- 포인트
  - [다음 주소 검색 api](https://postcode.map.daum.net/guide) ... 친절하게 설명 됨
  - this. 을 사용하기 위해
    - `oncomplete: function(data) {...}`을 `oncomplete:(data) => {...}`으로 변경



---

#### vue router에 params 적용시 발생하는 `Uncaught (in promise) Error: Missing required param "username"` 해결하기🎋

- 문제 발생 포인트

  - router-link를 사용할 때 params로 getters에 저장된 currentUser.username을 전송하려 했음
    - 개발자 도구 vue-devtools에는 currentUser가 채워져있음...
  - 하지만 DOM이 그려질 때 이를 받아오는 것보다 탭이 먼저 렌더링되어 에러 발생
  - created, mounted, watch 등 여러 수단을 써보았지만 해결 안됨
  - `console.log() 찍으면 2회가 찍히는데 처음엔 undefined 다음엔 username이 정확하게 찍힘`
    - 이를 통해 '두 번' 불러와지고 그 사이에 오류가 뜨는구나 유추
  
- 해결 방법

  - v-if 문을 걸어서 username이 존재하는지 여부를 판단하고 router-link를 렌더링하는 방식을 채택

    ```vue
    <template>
      ...
        <div class="new-box" v-if="!!username">
          <router-link :to="{ name: 'myplant', params: { username } }">
              <button class="btn">내 식물</button>
          </router-link>
        </div>
      ...
    </template>
    ```

- **해결방법(추가, 쉬움)**

  - currentUser를 불러올 수는 있으나 특정 깊이 이상으로 가면 불러오지 못함
  - state나 getters에 원하는 값을 얕게 작성

  ```js
  import router from '@/router'
  import axios from 'axios'
  import drf from '@/api/drf'
  
  export const Account = {
    state: {
  	...
      currentUser: {},
      username: '',
      ...
    },
  
    getters: {
  	...
      currentUser: state => state.currentUser,
      username: state => state.username,
      ...
    },
  
    mutations: {
      ...
      SET_CURRENT_USER: (state, user) => {
        state.currentUser = user
        state.username = user.username
      },
      ...
    },
  
    actions: {
      ...
  }
  ```

  




---

#### select tag에서 값(option)이 선택되었을 때 서버로 요청보내기(@change 핸들러 사용)🎍

```vue
<template>
  <select class="sido mr-1" @change="beforeFetchSigungu($event)">
    <option selected>지역을 선택해주세요</option>
    <option v-for="(loc) in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
  </select>
</template>

<script>
...    
  data() {
    return {
      info: {
          sido = ''
      }  
    }
  } 
...
  methods: {
    beforeFetchSigungu(event) {
      const sido = event.target.value
      this.info.sido = sido
    },      
  },
...      
</script>
```

- 기능
  - 주소를 검색할 때 드랍박스에서 지역(시, 도)을 선택하고, 동네(시, 군, 구)를 고르는 형식
  - 고를 때마다 data의 info에 담아주어 나중에 요청을 보낼 예정
- 포인트
  - select 태그의 option은 @click이 먹히지 않는다...
    - 처음에 이 방식으로 시도했으나 함수자체가 실행이 되지않아 당황
  - change 핸들러를 통해 event를 받아오고
  - console.log를 찍어가며 어디에 원하는 데이터가 있는지 파악해야 함



---

#### script에서 store로 dispatch(함수) 실행 시 데이터 넘길 때 주의사항🎎

- 데이터는 객체 형태로 넘겨야 한다!

  - 파이썬처럼 중괄호로 감싸면 객체로 인식하지 않음
  - 따로 변수에 할당하기

- 잘못된 예시들

  ```vue
  <script>
  export default {
    data() {
      retrun {
        info: {
          ...블라블라
        }
      }
    }
    ...
    methods: {
      ...
      beforeUpdateLeaf82(credentials) {
          ...
          this.updateLeaf82(credentials, this.info)
      // credentials는 template에서 받는 값, this.info는 data 에 저장된 값
      }
    },
  </script>
  ```

  ```vue
  <script>
  export default {
    data() {
      retrun {
        info: {
          ...블라블라
        }
      }
    }
    ...
    methods: {
      ...
      beforeUpdateLeaf82(credentials) {
          ...
          this.updateLeaf82({credentials, this.info})
      // credentials는 template에서 받는 값, this.info는 data 에 저장된 값
      // 중괄호 해봤자 넘어가서 어차피 객체로 인식못함  
      }
    },
  </script>
  ```

- 좋은 예시

  ```vue
  <script>
  export default {
    ...
    methods: {
      ...
      beforeUpdateLeaf82(credentials) {
          ...
          const updateInfo = {
            credentials,
            info: this.info
          }
          this.updateLeaf82(updateInfo)
      }
    },
  </script>
  ```



---

#### vuex를 사용할 때 created를해도 getters를 받아오지 못할 때 해결법(`watch 사용`)🎑

```vue
<script>
import { mapGetters , mapActions } from 'vuex'

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
    ...mapActions(['deleteLeaf82']),
    fillData() {
      this.user = this.leaf82Detail.user
      this.addr = this.leaf82Detail.addr
      this.info = this.leaf82Detail
      this.info.price = this.info.price.toLocaleString('ko-KR')
    }
  },
  computed: {
    ...mapGetters(['leaf82Detail', 'currentUser']),
  },
  watch: {
    leaf82Detail() {
      this.fillData()
    }
  }
}
</script>
```

- 발생한 에러
  - created때 상위components에서 fetchLeaf82Detail actions를 호출해 getters의  leaf82Detail을 채워줬으나, 받지 못함..
  - 콘솔창에 오류 발생, 렌더링 하면 데이터 날라감
- 해결책
  - `watch`
    - getters의 leaf82Detail값을 쳐다보고 있다가 변화가 발생하면,
    - data에 준비한 값을 채우고 그 값을 이용해 template에 띄어주는 방식



---

#### socket.io를 활용해서 채팅 구현하기🧧(미완성)



---

#### 이미지 업로드 시 보내고 받는 방법🎀

- 기능
  
  - 사진 선택 시 이미지를 우선적으로 보여줌
    - 사용자가 접근 후 모든 파일로 이동 가능(이미지가 아니라면 alert로 막아야 함)
  
  - 사진이 업로드 되기 전에는 기본이미지 보여주기
    - 최초에는 S3에서 생성된 url을 초기값으로 설정
  - 사진이 업로드 되면서 blob url 생성 후 대체 이미지 보여주기
    - 이미지와 글 클릭하면 파일 첨부 기능(라벨로 묶자)
    - 미리보기 변수가 필요하겠다!
  - 사진 백엔드로 보내기
    - 백엔드에서 S3로 파일 변환 후 이미지 url 저장
  
- 코드

  ```vue
  <template>
  ...
    <div class="left">
      <div class="img-box d-flex justify-content-center">
        <img :src="preview" alt="등록될 사진입니다.">
      </div>
      <div class="img-add-box d-flex justify-content-center pt-2">
        <label for="pic-file" class="img-add mb-0">
          <span class="material-symbols-outlined">
            photo_camera
          </span>
          <span>
            사진 변경하기
          </span>
        </label>
        <input type="file" id="pic-file" @change="onInputImage()" accept="image/*" ref="leaf82Image">
      </div>
    </div>
  </template>
  
  <script>
  import { mapActions , mapGetters } from 'vuex'
  
  export default {
    name: 'Leaf82NewForm',
    data() {
      return {
        credentials: {
          // 사진을 담아 보낼 변수 photo
          photo: '',
          ...
        },
        // 이미지 미리보기를 위한 변수
        // 디폴트는 백에서 S3로 생성한 이미지 url
        // 밑에서 첨부된 사진이 바뀔 때 이미지 url을 만들어 바꿔줄 예정
        preview: 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg'
      }
    },
    methods: {
      ...mapActions(['fetchSido', 'fetchSigungu', 'createLeaf82']),
      ...
      beforecreateLeaf82(credentials) {
        if (credentials.plantname === '') {
          alert('이름을 입력해주세요.')
        } else if (credentials.price === '' || !Number.isInteger(parseInt(credentials.price))) {
          alert('가격을 확인해주세요.')
        } else if (credentials.sigungu === '') {
          alert('주소를 선택해주세요.')
        } else if (credentials.content === '') {
          alert('식물을 소개해주세요')
        } else {
          this.createLeaf82(credentials)
        }
      },
      onInputImage() {
        // data 값에 있는 photo 변수를 ref를 통해 이미지 파일에 접근
        this.credentials.photo = this.$refs.leaf82Image.files[0]
        // 임시 이미지 url 생성 (blob으로 없어지는 임시 데이터)
        const url = URL.createObjectURL(this.credentials.photo)
        // 이미지를 로드해주는 preview 변수에 담아줌
        this.preview = url
      },
    },
    ...
  }
  </script>
  ```

- 포인트

  - 이미지 미리보기 url 만들기 : `URL.createObjectURL(사진 파일)`
  - 이미지 미리보기를 위한 data 값 지정 : `preview`
  - 사진 선택 시 우선적으로 이미지 파일 선택하게 하기 : `accept="image/*"`



---

#### router-link로 이동할 때 스크롤 위치 최상단으로 이동하기(기본값으로는 스크롤 위치로 이동)🎞

```js
// src/router/index.js

// 함수 추가 전
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});


// 함수 추가 후
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(){
    return { top: 0 }
  },
});
```

- 문제점
  - 스크롤이 내려가 있는 상태에서 라우터를 통해 다른 페이지로 이동
    - 스크롤 위치가 그대로 페이지가 바뀜
- 해결
  - 페이지 이동 시 스크롤이 최상단으로 올라감



---

#### viewport 너비를 기준으로 화면 스타일 적용🎟

- 기능
  - 휴대폰 사이즈일때 배경 이미지 변경

```vue
<template>
<div class="boxes">
    <!-- first box를 바인딩해서 조건에따라 값을 변경 -->
    <div :class="firstBox">
      ...
    </div>
    ...
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      // 초기 너비는 윈도우의 이너 너비
      width: window.innerWidth,
      // 기본값으로는 'first-box' 설정
      firstBox: 'first-box',
    }
  },
  methods: {
    // 현재 너비를 수정해줄 함수
    handleResize() {
      this.width = window.innerWidth;
    },
    // 너비값이 바뀔 때마다 실행시켜줄 함수
    mobileOrPc() {
      if (this.width <= 576) {
        this.firstBox = 'first-box-mobile'
      } else {
        this.firstBox = 'first-box'
      }
    },
  },
  // 시작화면이 모바일인지 피씨인지 판별하기위해 초기 설정
  created() {
    this.mobileOrPc()
  },
  // 마운티드에 설정
  mounted() {
    window.addEventListener('resize', this.handleResize);
	},
  // 비포언마운트에 설정
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize);
  },
  //width 값이 바뀔 때마다 모바일인지 피씨인지 판별하는 함수 실행
  watch: {
    width() {
      this.mobileOrPc()
    }
  }
}
</script>

<style>
.first-box {
  height: 1117px;
  background: url("../assets/HomeView/background_img.jpg") bottom left;
  background-size: cover;
}

.first-box-mobile {
  height: 800px;
  background: linear-gradient(rgba(255, 255, 255, 0.6), rgba(255, 255, 255, 0.6)), url('../assets/HomeView/main_pic_1.jpg') bottom left;
  background-size: cover;
}
</style>
```

#### 더보기 클릭시 추가 데이터 받아오기🎢

- 흐름
  - `더보기` 버튼 클릭
  - 서버로 파라미터를 담아 요청(`page(몇번쨰 페이지인지), limit(몇개씩 받아올 건지)`)
  - 받아온 데이터  `vuex`에 담아주기
  - `watch`를 통해 vuex가 변경되면 `.vue`파일에 `data`채워주기

```vue
src/components/Leaf82Search.vue

<template>
...
	<!-- sellObject로 데이터를 받는데 next 값이 존재한다면(더 받을 데이터가 있는지 백엔드에서 검사) -->
    <div class="d-flex justify-content-center pb-5" v-if="isSell">
      <button class="more-btn" v-if="!!sellObject.next" @click="more()">- 더보기 -</button>
    </div>
    <div class="d-flex justify-content-center pb-5" v-if="!isSell">
      <button class="more-btn" v-if="!!buyObject.next" @click="more()">- 더보기 -</button>
    </div>
...
</template>

<script>

    
    
</script>
<script>
import { mapActions , mapGetters } from 'vuex'
import router from '@/router'


export default {
  name: 'Leaf82SearchList',

  //bList, sList를 채워서 v-for문으로 사용자에게 보여줌
  data () {
    return {
      isSell: true,
      info: {
        plantname: '',
        sido: '',
        sigungu: '',
        limit: 20,
        page: 1,
        category_class: '분양해요',
      },
      bList: [],
      sList: [],
      searchBox: '',
      create: '',
      title: '',
    }
  },

  methods: {
    ...mapActions(['fetchSigungu', 'search',]),

    fillList() {
      this.sList = this.sellList
      this.bList = this.buyList
      for (let item of this.sList) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
      for (let item of this.bList) {
        const price = Number(item.price)
        item.price = price.toLocaleString('ko-KR')
        if (item.plantname.length > 7) {
          const plantname = item.plantname.substr(0, 7) + '...'
          item.plantname = plantname
        }
      }
    },
	
    // 더보기 버튼 클릭시 호출할 api
    more() {
      this.info.page += 1
      const params = this.info
      if (!this.info.plantname) {
        delete params.plantname
      }
      if (!this.info.sigungu) {
        delete params.sigungu,
        delete params.sido
      }
      this.search(params)
    },

	...
  },

  // sellObject, sellList, buyObject, buyList 값이 변화될 예정
  computed: {
    ...mapGetters(['sido', 'sigungu', 'isLoggedIn', 'sellObject', 'sellList', 'buyObject', 'buyList', 'device'])
  },

  created() {
    this.fetchSearch()
    this.changeDevice()
  },

  // 와치를 통해 값이 바뀔 때마다 데이터 값을 추가해줄 예정
  watch: {
    sellList() {
      this.fillList()
    },
    buyList() {
      this.fillList()
    },
    device() {
      this.changeDevice()
    }
  }
}
</script>

<style>

</style>
```

```js
import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export const Leaf82 = {
  state: {
	...
    sellObject: {},
    sellList: [],
    buyObject: {},
    buyList: [],
    ...
  },

  getters: {
    ...
    sellObject: state => state.sellObject,
    sellList: state => state.sellList,
    buyObject: state => state.buyObject,
    buyList: state => state.buyList,
    ...
  },

  mutations: {
    ...
    // set은 첫 불러오기 add는 추가하기
    // count는 데이터 총 개수
    // next는 불러온 데이터들 뒤에 데이터를 더 불러올 수 있는지, 개수와 page 변수로 판단
    // previous는 이전 데이터가 있는지
    SET_SELLOBJECT: (state, sellObject) => {
      state.sellObject = {
        count: sellObject.count,
        next: sellObject.next,
        previous: sellObject.previous
      }
      state.sellList = sellObject.results
    },
    // sellList에 데이터들 for 문으로 돌려주기
    ADD_SELLOBJECT: (state, sellObject) => {
      state.sellObject = {
        count: sellObject.count,
        next: sellObject.next,
        previous: sellObject.previous
      }
      for (let result of sellObject.results) {
        const price = Number(result.price)
        result.price = price.toLocaleString('ko-KR')
        if (result.plantname.length > 7) {
          const plantname = result.plantname.substr(0, 7) + '...'
          result.plantname = plantname
        }
        state.sellList.push(result)
      }
    },
    SET_BUYOBJECT: (state, buyObject) => {
      state.buyObject = {
        count: buyObject.count,
        next: buyObject.next,
        previous: buyObject.previous
      }
      state.buyList = buyObject.results
    },
    ADD_BUYOBJECT: (state, buyObject) => {
      state.buyObject = {
        count: buyObject.count,
        next: buyObject.next,
        previous: buyObject.previous
      }
      for (let result of buyObject.results) {
        const price = Number(result.price)
        result.price = price.toLocaleString('ko-KR')
        if (result.plantname.length > 7) {
          const plantname = result.plantname.substr(0, 7) + '...'
          result.plantname = plantname
        }
        state.buyList.push(result)
      }
    },
    ...
  },

  actions: {
    // 서치로 axios 요청
    // params로 데이터를 보내줄 예정
    // page가 1이라면 초기 요청이기에 set, 그게 아니라면 add
    search({ commit }, params) {
      axios({
        url: drf.leaf82.search(),
        method: 'get',
        params
      })
      .then(res => {
        if (params.category_class === '분양해요' && params.page === 1) {
          commit('SET_SELLOBJECT', res.data)
        } else if (params.category_class === '분양해요' && params.page !== 1) {
          commit('ADD_SELLOBJECT', res.data)
        } else if (params.category_class === '분양받아요' && params.page === 1) {
          commit('SET_BUYOBJECT', res.data)
        } else {
          commit('ADD_BUYOBJECT', res.data)
        }
      })
      .catch(err => {
        console.log(err)
      })
    },

    ...
}
```




#### 배너 이미지 비율 고정🏞

```vue
<template>
  ...
    <!-- 배경 화면 -->
    <div class="container my-0">
      <div class="banner-img">
      </div>
    </div>
    ...
</template>
```

```css
.container {
  height: 50vh;
  margin: 0;
  padding: 0;
  max-width: 1920px;
}

.banner-img {
  background-image: url('../assets/MyplantView/banner_img-02.svg');
  height: 100%;
  width: 100%;
  margin: 0;
  background-size: cover;
}
```

- 기능
  - 화면이 줄어들 때 배너 이미지의 비율이 망가지지 않고 자리 차지하게 함
- 포인트
  1. 이미지 바깥 태그의 `heignt`값을 `vh`로 설정함
     - `vh` : 뷰포트의 초기 컨테이닝 블록 높이 1%와 같음
  2. `background-size: cover` 
     - 이미지가 찌그러지지 않는 한도 내에서 제일 크게 설정함
     - 이미지의 가로 세로 비율이 요소와 다르다면 이미지를 세로 또는 가로 방향으로 잘라내어 빈 공간이 생기지 않도록 설정함
  3. 이미지가 잘라질 것을 고려하여 가로로 긴 이미지를 준비해서 적용함



#### 모달창 띄우기☁

```vue
...
<div class="row plant-btn-group">
  <button class="btn plant-info-btn" type="button" @click="changeModal(1)">계절별 식물 관리 정보</button>
    ...
  <div class="black-bg" @click="close($event)" v-if="modal===1 || modal===2 ">
    <div class="modal-bg myplant-modal">
      <!-- 계절별 식물 관리 정보 모달 -->
      <div v-if="modal===1">
        <h5>계절별 식물 관리 정보</h5>
        <div class="season">봄</div>{{ myplant.plant_info?.watercycle_spring_nm }}
        <div class="season">여름</div>{{ myplant.plant_info?.watercycle_summer_nm }}
        <div class="season">가을</div>{{ myplant.plant_info?.watercycle_autumn_nm }}
        <div class="season">겨울</div>{{ myplant.plant_info?.watercycle_winter_nm }}
      </div>
      ...
      <button class="modal-close-btn">닫기</button>
    </div>
  </div>
    ...
```

```vue
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  ...
  methods: {
    ...
    close(event) {
      if (event.target.classList.contains('black-bg') || event.target.classList.contains('modal-close-btn')) {
        this.modal = 0
      }
    },
    changeModal(num) {
      this.modal = num
    }, 
    ...
  },
  ...
}
</script>
```

```css
.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  position: fixed;
  top: 0px;
  left: 0px;
}

.myplant-modal {
  position: relative;
  top: 150px;
}

.modal-bg {
  width: 80vw;
  ...
}

.modal-close-btn {
  ...
  margin-left: auto;
  display: block;
  ...
}
```

- 기능
  - 버튼 클릭하면 모달창 띄움
- 포인트
  1. 모달은 새 페이지가 아니라 `<div>`의 위치값을 지정하는 것
  2. 모달이 띄워질 때 뒷 배경이 어둡게 처리되는 것 = `<div>` 태그 배경 색을 약간 투명한 검은색으로 처리
  3. 모달창 위치를 잡기 위해 `black-bg` 태그가 최상단에 위치
     - `modal`태그는 `black-bg` 안에 위치함
     - `modal`태그 위치값은 `black-bg`를 기준으로 `relative`
  4. `black-bg`가 뷰 화면 전체를 덮기 위해 `width: 100%`, `height: 100%`, `position: fixed`로 하여 좌상단 꼭지점이 뷰 화면의 좌상단과 일치하게 만듦
  5. 모달이 띄워졌을 때 모달 창을 내리는 방법 = 모달 밖 배경을 클릭 or  모달 내의 닫기 버튼 클릭
     1. 모달 밖 배경을 클릭
        - `event.target.classList.contains('black-bg')`
     2. 모달 내의 닫기 버튼 클릭
        - `event.target.classList.contains('modal-close-btn')`
  6. 서로 다른 내용의 모달 띄우는 방법
     - 모달 마다 번호를 매겨 클릭할 때 `changeModal`함수를 일으킴



#### 오른쪽 하단에 등록 버튼 고정시키기🎯

```vue
<template>
  ...
    <!-- 추가 버튼 (스티키 바텀) -->
    <div class="create-btn" v-if="mypage">
      <router-link class="add px-5 mx-5 pb-5" :to="{ name: 'myplantNew' }">
        <button class="btn">
          <span class="material-symbols-outlined">add</span>
        </button>
      </router-link>
    </div>
  ...
</template>
```

```css
.create-btn {
  position: sticky;
  bottom: 15px;
  text-align: end;
  }
```

- 기능
  - 스크롤로 화면을 이동해도 항상 오른쪽 하단에 정해진 위치에 등록 버튼이 따라 다님
- 포인트
  1. `position: sticky` : 위치를 고정시키기 위해
  2. `bottom: 15px` : 뷰 화면 맨 밑에서 약간 떨어진 곳에 위치
  3. `text-align: end` : 오른쪽 정렬로 버튼 위치를 오른쪽에 위치 시킴



#### 마우스 오버시 활성화 효과✨

```vue
<template>
  ...
        <button class="btn">
          <span class="material-symbols-outlined">add</span>
        </button>
  ...
</template>
```

```css
.btn{
  border-radius: 100%;
  height: 60px;
  width: 60px;
  background-color: #b2c9ab;
  color: white;
}

.btn:hover {
  background-color: #65805d;
  transition: all 0.5s;
}
```

- 기능
  - 마우스 오버 시 색상이 바뀌도록하여 사용자에게 클릭할 수 있는 버튼임을 인식하게 함
- 포인트
  1. `:hover` : 마우스 오버시 적용할 css를 담을 수 있음
  2. transition
     - 엘리먼트의 두 가지 상태 사이에 변화를 줄 수 있음
     - 엘리먼트의 상태란, `:hover`나 `:active` 또는 자바스크립트를 사용해 동적으로 만들어진 것
     - `transition: property name | timing function | duration | delay`의 형태로 작성됨
       - property name : 1개 이상의 속성 값을 적용할 수 있음
       - 순서 중요함 : 시간으로 해석될 수 있는 값이 첫 번째면 duration으로, 두 번째면 delay로 적용됨
     - `transition: all 0.5s` : 모든 요소를 0.5초 delay 후 바꿈



#### 객체 안의 객체의 값을 사용하는 방법🧪

###### 1. 객채 안에 값이 있는지 확인하고 그 안에서 값 가져오기

```vue
<div v-if="myplant.plant_info?.name!=='직접 입력하기'" class="myplant-data botanical-name">{{ myplant.plant_info?.name }}</div>
```

- `?.` 
  - `myplant`라는 객체 안에 `plant_info`라는 값이 있는지 먼저 확인함
  - 만약 값을 받아오는 과정에서 `plant_info`값이 있으면 그 안에 있는 `name`을 받아옴

###### 2. 자주 쓰는 값이라면 최초 1회에 받아올 때 다른 곳에 저장함

```vue
<router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username } }" :style="[isMyplant ? {fontWeight: 700} : {fontWeight: 400}]" v-if="!!username">내 식물</router-link>
```

- 상황 설명

  - `username`은 `currentUser`라는 객체 안에 있는 값
    - `created`때 `currentUser`는 받아오지만 아직 그 안에 있는 `username`에 접근하지는 못함
      => 값에 접근하지 못하므로 콘솔창에 에러를 먼저 띄움
      => 에러를 띄운 뒤에 값에 접근해서 동작하는 데에는 문제 없음

- 해결 방법

  - `currentUser`를 저장할 때 `username` 변수를 vuex의 `state`에 저장해두는 방식으로 변경

    ```js
    export const Account = {
      state: {
        ...
        currentUser: {},
        username: localStorage.getItem('username') || '',
        ...
      },
        ...
        fetchCurrentUser({ commit, getters, dispatch }) {
          if (getters.isLoggedIn) {
            axios({
              url: drf.accounts.currentUserInfo(),
              method: 'get',
              headers: getters.authHeader,
            })
            .then(res => {
              commit('SET_CURRENT_USER', res.data)
              localStorage.setItem('username', res.data.username)
            })
            .catch(err => {
              if (err.response.status === 401) {
                dispatch('removeToken')
                router.push({ name: 'login' })
              }
            })
          }
        },
    ```

    - `username`을 `localStorage`에 저장한 이유 : vuex는 새로고침하면 값을 모두 날림
      -> 자주 접근해서 쓰는 값이라면 `localStorage`에 저장해서 쓰는 방식이 경제적

  - 그럼에도 값에 접근하지 못하는 상황 종종 발생

    ```vue
    <router-link class="nav-link pb-0 mx-2" :to="{ name: 'myplant', params: { username: username } }" :style="[isMyplant ? {fontWeight: 700} : {fontWeight: 400}]" v-if="!!username">내 식물</router-link>
    ```

    - `v-if="!!username"` 이라는 조건문을 달아 `username`이라는 값이 존재할 때에만 router-link가 동작하게 만듦
    - 조건문이 없어도 동작하는 데에는 문제가 없지만 에러를 제거하기 위한 시도



#### progress bar📈

```vue
<progress :value=otpTimer max="60" class="progress-bar"></progress>
```

```css
.progress-bar {
  appearance: none;
  background-color: white;
  text-align: center;
  width: 80%;
  margin: 1rem 0;
}
.progress-bar::-webkit-progress-bar {
  background:#e9e9e9;
  border-radius:10px;
}
.progress-bar::-webkit-progress-value {
  border-radius:10px;
  background: #B2C9AB;
  transition: width 1s linear;
}
```

- 기능
  - 바인딩한 수치값에 따라 상태바 형태로 값을 표현함
- 포인트
  1. 원하는 수치값을 바인딩
     - `:value=otpTimer`
       - 타이머가 카운트다운하면 변하는 값을 progress bar의 value값으로 연결함
  2. `-webkit-`
     - 웹 브라우저를 만드는 데 기반을 제공하는 오픈 소스 응용 프로그램 프레임워크
     - `-webkit-` : 구글, 사파리
     - `-mox-` : 파이어폭스



#### OTP 타이머⏱

```vue
<div v-if="!myplant.is_connected && !!temp_OTP" class="otp-timer">
    <div>다음 숫자를 화분에 입력해주세요</div>
    <div class="otp-number">{{ temp_OTP }}</div>
    <div v-if="otpTimer > 0">{{ otpTimer }}초</div>
    <div v-if="otpTimer <= 0">0</div>
    <div class="d-flex justify-content-center">
        <progress :value=otpTimer max="60" class="progress-bar"></progress>
    </div>
</div>
```

```vue
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  ...
  computed: {
    ...mapGetters(['myplant', 'isOwner', 'temp_OTP', 'otpTimer']),
    ...
  },

  methods: {
    ...mapActions(['fetchMyplant', 'fetchOTP', 'checkOTP', 'disconnectMyplant', 'countTime', 'deleteMyplant', 'removeOTP']),
    ... 
    startTimer() {
      const interval = setInterval(() => {
        this.checkOTP(this.myplantPk)
        this.countTime(this.otpTimer - 1)
        if (this.otpTimer <= 55 && this.temp_OTP === null) {
          this.stopTimer(interval)
          this.fetchMyplant(this.myplantPk)
          this.modal = 0
        } else if (this.myplant.is_connected===true) {
          this.stopTimer(interval)
          this.temp_OTP = null
          this.modal = 0
        }
      }, 1000)
      return interval},
    stopTimer(Timer) {
      clearInterval(Timer)
      this.countTime(60)
      this.modal = 0
    }
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
    if (this.temp_OTP) {
      this.startTimer()
    }
  },
}
</script>
```

- 기능
  - OTP를 입력할 수 있는 60초를 카운트다운

- 포인트
  1. `setInterval` : 일정 시간 간격으로 반복해서 함수를 실행함
     - 첫 번째 인자 : 실행할 코드 혹은 함수
     - 두 번째 인자 : 반복 주기(ms)
     - Interval ID를 반환함 (함수를 호출할 때마다 내부적으로 생성되는 타이머 객체)
     - 이 값을 인자로 `clearInterval()`함수를 호출하면 코드가 주기적으로 실행되는 것을 중단시킬 수 있음
  2. `clearInterval()` : `Interval ID`를 인자로 받아 `setInverval`함수를 중단시킴
- 해결해야 될 점:warning:
  - OTP 타이머가 카운트다운 되는 도중 뒤로가기 혹은 다른 페이지로 이동하는 경우 타이머가 끝나지 않음
  - DB에서 otp_code를 `null`값으로 받아와도 타이머가 계속 실행됨
  - 새로고침하면 타이머가 초기화됨

###### OTP 오류 해결

```vue
<script>

export default {
  name: 'MyplantDetailView',
  data() {
    return {
      ...
      interval: 0,
    }
  },
  ...
  computed: {
    ...mapGetters(['myplant', 'isOwner', 'temp_OTP', 'otpTimer']),
    ...
  methods: {
    ...mapActions(['fetchMyplant', 'fetchOTP', 'checkOTP', 'disconnectMyplant', 'countTime', 'deleteMyplant', 'removeOTP']),
    close(event) {
      if (event.target.classList.contains('black-bg') || event.target.classList.contains('modal-close-btn')) {
        if (this.modal === 3) {
          this.stopTimer(this.interval)
          this.countTime(60)
          this.removeOTP(this.myplantPk)
          this.interval = 0
        }
        this.modal = 0
      }
    },
    changeModal(num) {
      this.modal = num
    },
    startTimer() {
      this.interval = setInterval(() => {
        this.checkOTP(this.myplantPk)
        this.countTime(this.otpTimer - 1)
        if (this.otpTimer <= 55 && this.temp_OTP === null) {
          this.stopTimer(this.interval)
          this.fetchMyplant(this.myplantPk)
          this.modal = 0
        } else if (this.myplant.is_connected===true) {
          this.stopTimer(this.interval)
          this.temp_OTP = null
          this.modal = 0
        }
      }, 1000)
      return this.interval},

    stopTimer(Timer) {
      clearInterval(Timer)
      this.countTime(60)
      this.modal = 0
    },
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
    if (this.temp_OTP) {
      this.removeOTP(this.myplantPk)
      this.countTime(60)
    }
  },

  beforeUnmount() {
    if (this.temp_OTP !== null) {
      this.stopTimer(this.interval)
      this.countTime(60)
      this.removeOTP(this.myplantPk)
    }
  },

}
</script>
```

- 기능
  - 모달창 닫기 버튼 클릭 시, 페이지 새로고침 시, 다른 페이지로 이동 시 연결 시도 중단
- 포인트
  1. `setInterval` 함수가 반환하는 `Interval ID`를 data에 선언해서 변경해 사용함
     - 페이지 이동 시 `Interval ID`를 인자로 받아 타이머를 중단하기 위해
  2. `beforeUnmount()` 사용
     - 페이지 이동, 페이지 새로고침 시 연결 시도 중단하기 위해
  3. `created()` 에서도 OTP코드가 남아있다면 초기화

#### form 하나로 create, update 다루기🖍

NewView

```vue
<template>
  <div class="new-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="create" class="mt-3"></myplant-form>
  </div>
</template>

<script>
...
import MyplantForm from '@/components/MyplantForm.vue'

export default {
  name: 'MyplantNewView',
  components: { NavBar, MyplantForm },
  data() {
    return {
      myplant: {
        nickname: '',
        photo: '',
        plantname: '',
        tmp: '',
      }
    }
  }
}
</script>
```

EditView

```vue
<template>
  <div class="edit-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="update" class="mt-3"></myplant-form>
  </div>
</template>

<script>
...
import MyplantForm from '@/components/MyplantForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MyplantEdit',
  components: { NavBar, MyplantForm },
  computed: {
    ...mapGetters(['myplant'])
  },
  methods: {
    ...mapActions(['fetchMyplant'])
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
  }
}
</script>
```

Form

```vue
<template>
  ...
      <form @submit.prevent="onSubmit">
        ...
                <input @change="onInputImage" accept="image/*" ref="newMyplantImage" type="file" class="form-input" id="myplantPhoto">
              ...
        ...
            <input v-model="newMyplant.nickname" type="text" class="form-input" id="myplantNickname" placeholder="식물 닉네임을 입력해주세요.">
          ...
      </form>
    ...
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MyplantForm',
  props: {
    myplant: Object,
    action: String,
  },
  data() {
    return {
      newMyplant: {
        nickname: this.myplant.nickname,
        photo: this.myplant.photo,
        plantname: this.myplant.plant_info?.name,
        tmp: this.myplant.tmp,
      },
      newMyplantImage: this.action==='create' ? 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg' : this.myplant.photo,
    }
  },
  ...
  methods: {
    ...mapActions(['createMyplant', 'searchPlant', 'updateMyplant']),
    ...
    onSubmit() {
      ...
      if (this.action === 'create') {
        this.createMyplant(this.newMyplant)
      } else if (this.action === 'update') {
        if (this.newMyplant.photo === this.myplant.photo) {
          this.newMyplant.photo = 'same'
        }
        const payload ={
          plantPk: this.myplant.id,
          ...this.newMyplant,
        }
        this.updateMyplant(payload)
      }
    },
  },
  ...
}
</script>
```

- 기능
  - 각 페이지에서 데이터와 action 값을 보내어 form에서 받은 값을 토대로 새로운 등록 값을 만듦
- 포인트
  1. 각 페이지에서 form으로 데이터를 prop
  2. `action`을 구분하기 위해 string으로 prop
  3. `create`일 때는 빈 값을, `update`일 때는 해당 데이터를 넘겨주어 입력창을 채워 넣음



#### form에 이미지 넣기📷

```vue
...
<form>
    <div class="mb-3 img-section">
          <div class="preview-section">
            <label for="myplantPhoto" class="img-add">
              <img :src="newMyplantImage" alt="내식물 등록 이미지" class="preview-myplant-image">
            </label>
          </div>
            <div class="img-add-div">
              <label for="myplantPhoto" class="img-add">
                <span class="material-symbols-outlined img-add-icon">photo_camera</span>
                <span>사진 등록하기</span>
                <input @change="onInputImage" accept="image/*" ref="newMyplantImage" type="file" class="form-input" id="myplantPhoto">
              </label>
              <span class="px-2">|</span>
              <label for="photo-delete">
                <span @click="onDeleteImage" class="img-delete-btn img-add">
                  <span class="material-symbols-outlined img-add-icon">imagesmode</span>
                  <span>기본 이미지로</span>
                </span>
              </label>
            </div>
        </div>
</form>
```

```vue
<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  ...
  data() {
    return {
      newMyplant: {
        nickname: this.myplant.nickname,
        photo: this.myplant.photo,
        plantname: this.myplant.plant_info?.name,
        tmp: this.myplant.tmp,
      },
      newMyplantImage: this.action==='create' ? 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg' : this.myplant.photo,
    }
  },
  ...
  },
  methods: {
    ...
    onInputImage() {
      this.newMyplant.photo = this.$refs.newMyplantImage.files[0]
      const url = URL.createObjectURL(this.newMyplant.photo)
      this.newMyplantImage = url
    },
    onDeleteImage() {
      this.newMyplant.photo = ''
      this.newMyplantImage = 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg'
    },
    onSubmit() {
      ...
      if (this.action === 'create') {
        this.createMyplant(this.newMyplant)
      } else if (this.action === 'update') {
        if (this.newMyplant.photo === this.myplant.photo) {
          this.newMyplant.photo = 'same'
        }
        const payload ={
          plantPk: this.myplant.id,
          ...this.newMyplant,
        }
        this.updateMyplant(payload)
      }
    },
  },
  created() {
    this.searchPlant()
  },
}
</script>
```

- 기능
  - 이미지를 file값으로 form에 넣어서 전공
  - DB에서 받아서 쓰는 이미지는 string(정확히는 url 주소)
- 포인트
  1. `<input>`태그의 `type=file`로 하여 유저의 로컬 파일을 입력 받음
     - `accept="image/*"` 조건을 걸어 이미지 파일만 먼저 필터링해서 볼 수 있게끔 함
  2. 이미지를 입력받고 미리보기 사진을 띄우기 위해 `onInputImage`함수를 만들어서 사용함
     - 입력받은 이미지 `file`을 `url`로 바꾸는 과정
     - `ref="newMyplantImage"` : ref 속성을 부여한 자식 태그를 호출하기 위해 사용
       - `this.newMyplant.photo = this.$refs.newMyplantImage.files[0]`와 같이 입력값을 가공하기 위해 사용함
     - 입력받은 파일 값을 `URL.createObjectURL`을 통해 url 주소값으로 변경하여 사용
  3. 이미지 태그에 `src`를 바인딩해 변하는 값을 띄울 수 있도록 함
  4. 미리보기 이미지와 `input` 태그 모두 같은 id를 가진 `label`로 감싸주어 이미지를 클릭해도, 등록하기를 클릭해도 이미지 파일을 입력받을 수 있도록 함
  5. 사진을 기본 이미지로 변경 시, django에는 빈 문자열을 보내주고, 미리보기는 디폴트 값으로 변경해줌
  6. `update`시에는 넘겨받은 이미지 값은 `string`이고 form에 넣는 값은 `file`이므로 `submit`하기 전에 이전값과 같은 값인지 확인해줌
     - 같은 값이라면 `'same'`이라는 문자열을 담아 전송하고 django에서 처리해줌



#### 검색을 통해 option 리스트 필터링🔍

```vue
<template>
	....
          <div class="select-plant mb-3" v-if="action==='create'">
            <input type="text" id="plant" list="search-plant-list" placeholder="식물 종류를 검색하세요." class="form-input" v-model="newMyplant.plantname">
            <datalist id="search-plant-list">
              <option v-for="(plant) in plant_list" :key="plant.pk">{{ plant.name }}</option>
            </datalist>
            <input v-if="newMyplant.plantname==='직접 입력하기'" type="text" id="tmp-plant" placeholder="식물 종류를 직접 입력해주세요." class="form-input mt-3" v-model="newMyplant.tmp">
          </div>
          <div class="select-plant mb-3" v-if="action==='update'">
            <input v-if="newMyplant.plantname!=='직접 입력하기'" type="text" id="plant" :placeholder="myplant.plant_info.name" class="form-input disabled-input" disabled>
            <input v-if="newMyplant.plantname==='직접 입력하기'" type="text" id="plant" :placeholder="myplant.tmp" class="form-input disabled-input" disabled>
          </div>
        </div>
</template>
```

- 기능
  - `input`태그에 검색어를 입력하면 해당 검색어로 필터링된 데이터 리스트를 띄워줌
- 포인트
  - `input` 태그의 `type`은 `text`
  - `input`태그에 `list="search-plant-list"`를 넣고 `datalist` 태그에 `id`를 동일한 값으로 넣어 검색어로 필터링된 리스트를 띄울 수 있게 함
  - `select` vs. `datalist`
    - `select`는 정해진 데이터만 받아서 쓸 수 있음
    - `datalist`는 미리 정해진 값 이외에도 사용자가 임의로 입력한 변수값도 데이터 입력을 받음
- 문제점:warning:
  - 안드로이드에서는 datalist를 보여주지 못함



#### 내비게이션 바에서 현재 탭일 때 활성화 표시🚩

```vue
<template>
  <nav class="navbar navbar-expand-lg navbar-light px-4">
    ...
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        ...
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle pb-0 mx-2" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" :style="[isLeaf82 ? {fontWeight: 700} : {fontWeight: 400}]">
            잎팔이
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <div>
              <router-link class="dropdown-item" :to="{ name: 'leaf82' }">거래</router-link>
            </div>
            <div class="dropdown-divider"></div>
            <router-link class="dropdown-item" :to="{ name: 'messenger' }" v-if="isLoggedIn">채팅</router-link>
            <router-link class="dropdown-item" :to="{ name: 'login' }" v-if="!isLoggedIn">채팅</router-link>
          </div>
        </li>
        ...
  </nav>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'NavBar',

  data() {
    return {
      ...
      leaf82Group: ['leaf82', 'leaf82New', 'leaf82Detail', 'leaf82Edit', 'messenger'],
      ...
  },

  computed: {
    ...
    isLeaf82() {
      return this.leaf82Group.includes(this.$route.name)
    },
  ...
}
</script>
```

- 기능
  - 하나의 탭에 연결된 페이지가 많을 때 해당 페이지에서 모두 같은 탭을 활성화 표시하기
- 포인트
  1. leaf82의 하위 페이지들을 모두 리스트로 만들어둠
  2. `isLeaf82()`에서 현재 route 페이지의 이름이 `leaf82Group`에 포함되어 있다면 `true`값을 반환함
  3. `li`태그의 `style`을 바인딩하여 활성화 표시 여부를 결정함
     - 삼항 연산자를 사용하여 `true`값이면 굵은 글씨를, `false`값이면 얇은 글씨를 적용하도록 함



#### vuex-persistedstate💾

```js
import { createStore } from 'vuex'
import { Account } from './modules/accounts'
import { Myplant } from './modules/myplant'
import { Leaf82 } from './modules/leaf82'
import { Timer } from './modules/timer'
import { Messenger } from './modules/messenger'
import createPersistedState from "vuex-persistedstate"

export default createStore({
  modules: { 
    Account, Myplant, Leaf82, Timer, Messenger,
  },
  plugins: [createPersistedState({
    paths: ['Timer',]
  })],
})
```

- 기능
  - 새로고침하면 vuex의 데이터가 모두 날아가는 것을 방지
- 포인트
  - vuex에 있는 모든 데이터를 저장해서 쓰면 성능 저하 발생함
  - 유지시킬 데이터만 따로 모듈화해서 지정해줌
  - `Timer`의 경우 새로고침을 해도 카운트다운이 멈추지 않도록 하기 위해 설정해놓음



#### 정해진 url이 아닐 때 404페이지로 이동🏃‍♂️

```js
import { createRouter, createWebHistory } from 'vue-router'
...
import NotFound404 from '@/views/NotFound404.vue'

import store from '../store'

const routes = [
  ...
  //404
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: "/:catchAll(.*)",
    name: 'catch-all',
    redirect: '/404'
  },
]
...
```

- 기능
  - 지정해놓은 url이 아닌 주소로 사용자가 접근할 경우 자동으로 404 페이지로 이동시킴
- 포인트
  1. 이전 버전 : `path: '*'`
     `vue-router@next` 버전 : `path: "/:catchAll(.*)"`



#### 채팅창의 스크롤을 최근 채팅에 고정시키기💬

```vue
<template>
  ...
                <!-- 채팅 내용 -->
                <div class="col-md-6 col-lg-7 col-xl-8">
                  <div class="you-username" v-if="now_receiver!==-1">{{ nicknames[now_receiver] }}</div>
                  <div class="chat-view" ref="now_messages">
                    ...
                      <!-- 채팅방 클릭 후 -->
                    <div v-for="msg in now_messages" :key="msg">
                      ...
                  <!-- 채팅 메시지 적는 부분 -->
                  <div class="d-flex justify-content-start align-items-center" v-if="now_receiver!==-1">
                    <input v-model="message" type="text" class="form-input" id="exampleFormControlInput2"
                      placeholder="Type message" @keyup.enter="sendMessage">
                    <span @click="sendMessage" class="material-symbols-outlined send-btn">send</span>
                  </div>
</template>
```

```vue
<script>
...
import { mapActions, mapGetters } from "vuex"
import { io } from 'socket.io-client'

export default {
  ...
  data(){
    return {
      socket: null,
      id: -1,
      message: '',
      now_messages: [],
      now_receiver: -1, // 새로고침 했거나, 거래탭에서 채팅하기로 넘어오지 않았을 경우
      rooms: {},
      urls: {},
      baseURL: "https://plantinum.s3.ap-northeast-2.amazonaws.com/",
      nicknames: {},
    }
  },
  ...
  methods : {
    ...
    sendMessage() {
      // 소켓을 통해 서버로 메세지를 보낸다.
      if(this.now_receiver == -1){
        return;
      }
      this.socket.emit('send', {receiver:this.now_receiver , msg: this.message, room_num:this.rooms[this.now_receiver]});
      this.message = ''
    },
  ...
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
```

- 기능
  - 채팅 메시지가 새로 입력되었다면(혹은 메시지를 새로 받았다면) 최신 메시지에 맞춰 스크롤이 자동으로 내려가게 함
- 포인트
  1. `watch` : 내가 메시지를 입력했을 때 now_messages의 변화를 감지함
  2. `updated` : 상대방이 메시지를 입력하여 now_messages가 변화하는 것을 감지함
  3. `scrollTo()` : 지정된 위치로 스크롤
     - `scrollTo(x좌표, y좌표)`
     - `scrollTo({ top, left, behavior})`
       - `behavior` : 스크롤 효과 속성
         - `auto` : 기본값, 바로 위치로 이동
         - `smooth` : 부드럽게 이동
     - `scrollHeight` : 스크롤되는 부분을 포함한 실제 요소의 높이값
       - 0이 상단이므로 `scrollHeight`로 하게되면 최하단에 위치하게 됨
  4. `$nextTick()` : 다음 렌더링 사이클 이후 실행될 콜백 함수를 등록할 수 있는 기능을 제공하는 메서드
     - 데이터의 상태가 변경되었으나 화면에 변경된 상태가 반영되지 않는 경우 이 메서드를 사용하여 다시 렌더링하며 반영시킬 수 있음



#### 스크롤바 커스텀🖌

```css
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
```

- 포인트
  - `::-webkit-scrollbar` : 스크롤바 영역에 대한 설정
  - `::-webkit-scrollbar-thumb` : 스크롤바 막대에 대한 설정
  - `::-webkit-scrollbar-track` : 스크롤바 뒷 배경에 대한 설정
- 문제점:warning:
  - 크롬, 사파리를 제외한 브라우저에서는 지원하지 않음

#### 띄어쓰기, 줄바꿈 그대로 입력하기✏

```vue
<template>
  ...
                  <div class="d-flex justify-content-start align-items-center" v-if="now_receiver!==-1">
                    <textarea v-model="message" type="text" class="form-input" id="exampleFormControlInput2"
                      placeholder="Type message" @keyup.enter="sendMessage" rows="1" autofocus></textarea>
                    <span @click="sendMessage" class="material-symbols-outlined send-btn">send</span>
                  </div>
  ...
</template>
```

```css
.form-input {
  ...
  resize: none;
}
```

- 기능
  - 사용자가 입력한 문자 그대로 입력폼에 담아 보내기
  - 띄어쓰기, 줄바꿈 그대로 적용
- 포인트
  - `<textarea>` : `input`보다 긴 텍스트를 입력받고 싶을 때 사용
    - `rows` : 보이는 영역의 라인 수
    - `autofocus` : 페이지가 로드될 때 자동으로 포커스가 텍스트 입력 영역으로 이동함
    - `resize`
      - `<textarea>`의 박스크기를 임의로 수정할 수 있음
      - 막기 위해선 `style`에 `none`으로 지정해야 함



#### 띄어쓰기, 줄바꿈 그대로 보여주기📄

```vue
<template>
                        <div class="message-section">
                          <pre class="your-message chat-message">{{ msg.msg }}</pre>
                          <p class="message-time">{{ msg.datetime.substr(5, 11) }}</p>
                        </div>
</template>
```

```css
.chat-message {
  font-family: 'SUIT';
  white-space: pre-wrap;
}
```

- 기능
  - 데이터로 넘겨받은 텍스트 그대로를 보여주는 것
- 포인트
  - `<pre>` : 작성한 내용 그대로를 표현
    - CSS가 날아가므로 새로 지정해주어야 함	
  - `white-space` : 요소의 공백을 어떻게 처리할 것인지 정의함
    - `normal` : 연속된 공백과 줄 바꿈을 메꿔 하나의 공백으로 표시
    - `nowrap` : 공백을 채우지만 가로로 긴 줄을 줄 바꿈하지 않고 표시함
    - `pre` : 연속된 공백을 그대로 표시
    - `pre-wrap` : 연속된 공백을 그대로 표시  & 행의 줄바꿈은 행의 박스를 채우기 위해 필요한 경우 실행
    - `pre-line` : 연속된 공백을 메꿔 하나의 공백으로 표시 & 행의 줄바꿈은 행의 박스를 채우기 위해 필요한 경우 실행
---

### 2. BE

#### Django 한국어, 한국시간 설정

문제상황
- 모델 설계 중 created_at = models.DateTimeField(auto_now_add=True)를 작성하면 한국 시간이 아니라 국제 표준 시간으로 저장됨
- 시간을 저장할 때 한국 시간으로 저장하고자 함

해결방안
- 기본 설정
```
# project/settings.py

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```

- 한국어, 한국시간 설정
    - 반드시 USE_TZ = False 설정
```
# project/settings.py

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = False
```

auto_now_add와 auto_now
- auto_now_add
    - 데이터 최초 저장 시 현재 날짜와 시간을 저장
    - 생성 당시의 날짜와 시간
- auto_now
    - 데이터가 저장될 때마다 현재 날짜와 시간을 저장
    - 수정 당시의 날짜와 시간


#### Django allauth signup
allauth를 통한 signup시 오류 발생
- User model
```
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
```
    - settings.py에 AUTH_USER_MODEL = 'accounts.User' 등록 완료한 상태
- signup에 요청을 보낼 때 body에 필수값인 username, password1, password2를 기본으로 작성하고, 선택값인 email까지 작성하면 예상하지 못한 오류 발생
- 발생한 오류
```
ConnectionRefusedError: [WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다
```
    - 예상 결과는 로그인 상태로 전환되어 토큰 리턴, DB에 email을 포함하여 데이터 저장
    - 실제 결과는 비로그인 상태로 토큰 발행 X, DB에 email을 포함하여 데이터 저장, 500 상태와 함께 에러 발생


해결방안
- 참고문서
    - [공식문서](https://django-allauth.readthedocs.io/en/latest/configuration.html)
    - [깃허브](https://github.com/pennersr/django-allauth/blob/master/allauth/account/app_settings.py#L7)


- 코드 (settings.py)
```
ACCOUNT_EMAIL_VERIFICATION = 'none'
```
또는
```
# 개발단계에서 사용
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
````

- ACCOUNT_EMAIL_VERIFICATION = 'none'
```
ACCOUNT_EMAIL_VERIFICATION (=”optional”)
Determines the e-mail verification method during signup – choose one of "mandatory", "optional", or "none".

Setting this to “mandatory” requires ACCOUNT_EMAIL_REQUIRED to be True

When set to “mandatory” the user is blocked from logging in until the email address is verified. Choose “optional” or “none” to allow logins with an unverified e-mail address. In case of “optional”, the e-mail verification mail is still sent, whereas in case of “none” no e-mail verification mails are sent.
```
    - email verification이 기본 설정으로 'optional'이 적용되었기 때문에 회원가입시 email을 작성하면 인증 이메일이 보내짐
    - 'none'으로 설정을 변경하면 메일이 보내지지 않고 바로 회원가입이 완료되며 로그인 상태로 전환됨
- EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    - 실제로 회원가입 확인 인증 메일을 보내는 대신에, 터미널창에 이메일 내용을 보여줌
    - 터미널에 이메일 내용을 보여주기 때문에 개발단계에서 사용
- 두 가지 방법 모두 오류 발생 X


#### Django allauth signup
allauth를 통한 signup시 오류 발생
- 자동으로 닉네임을 중복없이 생성하는 기능에 오류 발생
- 상황
    - DB를 새로 만들기 위해 기존의 스키마를 삭제하고 새로 생성
    - 기존의 migrations들을 모두 삭제하고 새롭게 생성하고자 함
    - python manage.py makemigrations를 실행하려 했으나 오류 발생
```
django.db.utils.ProgrammingError: (1146, "Table '<db이름>.accounts_user' doesn't exist")
```

- 기존 model
```
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    phone_number = models.CharField(max_length=11, blank=True)
    addr = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    nickname = models.CharField(max_length=15, unique=True)
```
- 기존 serializer
```
# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
import random
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):

    full_nickname = ''

    while full_nickname == '':
        nick1_lst = ['촉촉한', '싱싱한', '늘푸른', '건강한', '새내기']
        nick2_lst = ['참나무', '소나무', '올리브나무', '야자나무', '귤나무']
        nick1 = random.choice(nick1_lst)
        nick2 = random.choice(nick2_lst)
        nick3 = str(random.randint(0, 9999))
    
        full_nickname = nick1+nick2+nick3

        if User.objects.filter(nickname=full_nickname).exists():
            full_nickname = ''

    nickname = serializers.CharField(max_length=15, default=full_nickname)
    email = serializers.EmailField()

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self._validated_data.get('nickname', '')
        data['email'] = self._validated_data.get('email', '')
        return data
```
- 오류 발생 원인
    - 닉네임 default 값을 줄 때 if User.objects.filter(nickname=full_nickname).exists(): 코드를 통해 이미 존재하는 닉네임인지 확인하려 함

→ 아직 존재하지 않는 User 테이블에서 찾아보라는 지시였던 것

    - 이미 db와 테이블이 생성된 뒤에는 동작하였으나 생성되기 전에는 오류 발생

해결방안
- 수정한 serializer
```
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
import random
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField()

    def get_cleaned_data(self):
        full_nickname = ''

        while full_nickname == '':
            nick1_lst = ['촉촉한', '싱싱한', '늘푸른', '건강한', '새내기']
            nick2_lst = ['참나무', '소나무', '올리브나무', '야자나무', '귤나무']
            nick1 = random.choice(nick1_lst)
            nick2 = random.choice(nick2_lst)
            nick3 = str(random.randint(0, 9999))
        
            full_nickname = nick1+nick2+nick3
            if User.objects.filter(nickname=full_nickname).exists():
                full_nickname = ''

        data = super().get_cleaned_data()
        data['nickname'] = self._validated_data.get('nickname', full_nickname)
        data['email'] = self._validated_data.get('email', '')
        return data
```
- nickname default 값을 data['nickname'] = self._validated_data.get('nickname', full_nickname)에서 설정해야함
- get_cleaned_data함수 밖 클래스 내에서 User 모델에 접근시 User 테이블이 생성되기 전이기 때문에 인식 불가능
- 기존의 nickname = serializers.CharField(max_length=15, default=full_nickname) 코드에서 default= 인자는 오류 발생


#### Django Redis
Django 설정
- django-redis 설치
```
$ pip install django-redis
```
- 설정
```
# <프로젝트>/settings.py

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # 1번 DB 사용
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```
- 테스트 함수 작성
```
# views.py

from django.core.cache import cache
from rest_framework.response import Response


def test(request):
    cache.set('key', 'value', timeout=30)  # 지속시간 30초. 30초 뒤 삭제됨
    result = cache.get('key')
    return Response({'result': result})
```
- 주소 설정
```
# urls.py

urlpatterns = [
    path('test/', views.test),
]
```

문제상황 및 원인
- 위 설정까지만 하고 될 것이라 생각했지만 오류 발생
```
redis.exceptions.ConnectionError: Error 10061 connecting to 127.0.0.1:6379. 대상 컴퓨터 
에서 연결을 거부했으므로 연결하지 못했습니다.
[14/Aug/2022 01:41:39] "GET /api/v1/test/ HTTP/1.1" 500 119551  
```
- redis를 설치해야 django-redis 사용 가능

Redis 설치 (해결방안)
Window 설치
- Github에서 파일 다운 & 설치
```
https://github.com/microsoftarchive/redis/releases
```
- 3.0.504 (Latest)
- Redis-x64-3.0.504.msi 다운
- 파일 실행하여 설치
- 정상적으로 설치되었는지 확인
- redis-cli 로 실행, select <number>로 DB 선택 가능
```
# cmd

C:\Users\LJS>netstat -an|findstr 6379
  TCP    0.0.0.0:6379           0.0.0.0:0              LISTENING
  TCP    [::]:6379              [::]:0                 LISTENING
  
C:\Users\LJS>redis-cli  # redis 실행
127.0.0.1:6379> PING
PONG  # 정상 설치
```

Linux 설치 (Ubuntu)
- 설치에 앞서 apt-get 업데이트, 업그레이드
```
$ sudo apt-get update
$ sudo apt-get upgrade
```
- redis-server 설치
```
$ sudo apt-get install redis-server
```
- 버전 확인
```
$ redis-server --version

Redis server v=5.0.7 sha=00000000:0 malloc=jemalloc-5.2.1 bits=64 build=66bd629f924ac924
```
- 메모리 설정에 앞서 서버의 메모리 확인
```
$ vmstat

procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 9256552 214776 6114212    0    0     0     9    6    2  0  0 100  0  0
```
- maxmemory 설정을 위해 redis.conf 파일 편집
```
$ sudo vim /etc/redis/redis.conf
```
- 수정해야하는 부분
    - maxmemory: redis가 최대로 사용할 메모리
    - maxmemory-policy: redis가 최대로 사용할 메모리를 초과했을 때 데이터를 삭제하는 방식 정의
- 일반모드에서 /<검색할 단어>를 입력하고 엔터
    - 아래 방향으로 검색 (위→아래)
    ?<검색할 단어>: 위 방향으로 검색 (아래→위)
    - n을 누르면 다음 검색 결과로 이동
    shift + n: 이전 검색 결과로 이동
- maxmemory와 maxmemory-policy의 주석 부분을 편집
    - i를 누르면 입력 가능
    ```
    maxmemory 1g  # 최대 메모리 사용량 1G	
    maxmemory-policy allkeys-lru  # 초과시 오래된 데이터를 지워서 메모리 확보
    ```
    - 편집이 끝나면 Esc + :wq
- Redis 재시작
```
$ sudo systemctl restart redis-server.service
```


### 3. HW

#### LCD

1. 화면 해상도
   
    - 제공 받은 LCD가 잘 안쓰이는 해상도였다
    - **해결방안** : 직접 픽셀 수정해가면서 알아냈다. 

<br>

2. 작업표시줄

    - 프로그램이 구동될 때 보이는 작업표시줄이 신경쓰였다.
    - **해결방안** : 
        1. 마우스가 필요하다.
        2. 마우스로 작업표시줄에서 우클릭후 마우스 오버시에만 활성화 할 수 있다. 


#### 라즈베리파이
1. DHT11 : Adafruit_DHT
        
    - adafruit 측에서 더 이상 새로운 업데이트를 내놓지 않고 있다.
    - 즉, 공식적으로 라즈베리파이 4b를 위한 온습도 센서의 라이브러리가 없다.
    - **해결 방안** : 
        1. 기존 것을 쓰되 깃허브에서 직접 다운받는다.
        2. 다운 후 폴더에서 setup 전 직접 파일 수정을 하여 라즈베리파이 4b 모델을 추가해준다 그 이후 setup.py 실행

<br>  

2. NeoPixel LED
   
    - sudo로만 작동 가능하다.
    - 즉, 직접 코드 안에서 쓰는 것이 불가능하다.
    - **해결방안** : 외부 파일을 만든 후 안에서 쓰는 방법 채택하였다. 

<br>

3. subprocess
    - os.system 대신에 쓰인다.
    - subprocess.run("명령어") 구조이지만 에러가 난다. 쉘에서 쓰일 것인데 안된다고 한다.
    - **해결방안** : 
    ```python
        subprocess.run("명령어" , shell = true)
    ```
    로 작성해야 제대로 돌아간다. 


### 4. server


#### Django install 오류

<div markdown="1">

- pip 업데이트 확인 필요
- wheel 이나 다른것 설치가 필요하다.
```console
    pip install wheel
```
- settings.py에서 데이터베이스 명시가 필요하긴 하다.

- mysql-client 오류 시 해당 설치 후 다시 설치하면 잘된다.
```console
    sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

</div>

---

<br>
<br>
<br>

#### UWSGI
모듈이 존재하지 않아요!
<div markdown="1">

- 몇시간을 고민하도록 한 문제이다.
- uwsgi를 실행했는데 모듈이 없는 문제이다.
```
    module = back.wsgi:application
```
- 이 부분에서 manage.py 가 있는 경로가 아닌 다른 파일에 wsgi.py가 있다 그 폴더 명을 써줘야한다.

</div>

#### 400 Bad Request
- ALLOWED_HOSTS
```
# 로컬호스트에서만 접속 허용
ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# 모든 곳에서의 접속 허용
ALLOWED_HOSTS = ['*']

# 특정 호스트에서 접속 허용
ALLOWED_HOSTS = ['서비스를 제공할 도메인 주소']
```


#### 500 Internal Server Error
(1) uwsgi 경로 설정 오류
- 프론트에서 백엔드로 보내는 요청 주소 설정
```
# 기존 설정값
const HOST = 'http://127.0.0.1:8000/api/v1/'

# 배포시 설정값
# 포트번호 넣지 않기
const HOST = 'http://<배포주소>/api/v1/'
```

- django uwsgi ini 설정
    - 경로 정확히 작성
```
[uwsgi]
# django 프로젝트 폴더 경로
chdir = /home/ubuntu/back/
# wsgi가 존재하는 경로
module = <프로젝트이름>.wsgi:application
# 가상환경 경로
home = /home/ubuntu/venv/
...

```

- 코드 수정 후 reload, restart
```
$ sudo systemctl restart uwsgi
$ sudo systemctl restart nginx
```

(2) 이미지 파일 최대 크기 설정 오류
- 오류 메시지
```
TypeError: cannot pickle '_io.bufferedrandom' object
```

- 오류 상황
    - POST 요청으로 새로 사진을 업로드할 때는 nginx에 설정한 최대 크기까지 가능
    - PUT 요청으로 사진을 수정할 때 nginx에 설정한 최대 크기가 아닌, django의 이미지필드 기본 최대 크기인 2.5MB까지만 가능

- 오류 해결
```
# <프로젝트>/settings.py
# 30MB까지 업로드 가능하도록 설정
# 프론트에서 파일 크기가 30MB가 넘으면 경고창 띄우기 추가

FILE_UPLOAD_MAX_MEMORY_SIZE = 30 * 1024 * 1024  
```

#### 도메인 연결 오류
- 도메인 구매 후, DNS 연결
    - 레코드 추가
    - 타입: A, 호스트: @, 값: IP주소 xxx.xxx.xxx.xxx, TTL: 600

- IP 찾는 방법
    - CMD 실행
    - tracert <주소>
        - 주소 첫 부분에 http:// 입력하지 않음, 마지막 부분에 / 입력하지 않음
        - 예) tracert naver.com

- nginx 설정
```
# 경로
$ /etc/nginx/site-available/dafault
```
```
# defalut
server {
        listen 80 default_server;
        listen [::]:80 default_server;
		server_name <도메인주소> <www.도메인주소>
		...
}

# 예시
server {
        listen 80 default_server;
        listen [::]:80 default_server;
		server_name abc.com www.abc.com
		...
}
```

- 재시작
```
$ sudo systemctl daemon-reload
$ sudo systemctl restart uwsgi
$ sudo systemctl restart nginx
```


### 5. 기타
#### 성능 검사 dev tool `Lighthouse`🎠

- performance 높이기 위해 필요한 것

  - 요청 수 줄이기
  - 이미지 최적화
  - CDN 사용
  - 모바일 코드 먼저 짜기
  - CSS, JS, HTML 파일 줄이기
  - 비동기 처리
  - 플러그인 줄이기
  - 웹사이트 캐시 사용하기

  ...



---

#### vue cli 사용시 font는 app.vue에 걸어서 사용하는 것 보다 각 .vue파일에 적용하는 것이 성능적으로 더 좋음🎡

app.vue => 31%

HomeView.vue => 58%



---

#### performance 고려 사항 우선순위🎠

1. 이미지, 동영상 등 파일 크기 조절
2. CSR 보다는 SSR로 페이지 구성하기
3. 사용하지 않는 데이터는 사용할 때 받아오기
   - props 등 데이터 간소화
   - components 이용시 적절한 배분 고려 필요

4. 웹팩 공부해서 적용하기



---
#### 등록버튼은 우측하단이 국룰!🎢

#### 검색 및 필터 활용시 🎪

- 로직 명확하게(오류 없이)
- 검색 및 필터는 한곳에 모아서 모듈화(유저는 자기가 어떤 필터를 걸었는지 기억하지 않는다)
- reset 버튼 추가 고려!

  - 변경 전

    ```vue
    <template>
      <!-- 서치배너 -->
      <div class="search row">
        <div class="col-sm-2 col-md-4 col-0"></div>
        <div class="search-box col-sm-8 col-md-4 col-12 d-flex justify-content-center">
          <input class="search-input pl-3" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="beforeSearch()">        
          <button class="search-btn" type="submit" @click="beforeSearch()">
            <span class="material-symbols-outlined d-flex align-items-center justify-content-center">search</span>
          </button>
        </div>
        <div class="col-sm-2 col-md-4 col-0"></div>
      </div>
      <div class="select-box row mt-5 mb-3">
        <div class="col-sm-2 col-0"></div>
        <div class="select row d-flex justify-content-between col-sm-8 col-12">
          <div class="create">
            <!-- 생성버튼 -->
            <router-link :to="{ name : 'leaf82New' }" v-if="isLoggedIn">
              <button class="create-btn">
                등록
              </button>
            </router-link>
          </div>
          <div class="filter d-flex justify-content-center">
            <!-- 검색버튼 -->
            <select class="sido mr-1" @change="beforeFetchSigungu($event)">
              <option value="null">지역을 선택해주세요</option>
              <option v-for="loc in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
            </select>
            <!-- 시도가 선택되면 활성화 -->
            <select class="sigungu" @change="beforeFetchSearch($event)" v-if="this.info.sido">
              <option selected>동네를 선택해주세요</option>
              <option v-for="loc in sigungu" :key="loc.pk" :value="loc.sigungu">{{ loc.sigungu }}</option>
            </select>
            <select class="sigungu" v-if="!this.info.sido" disabled>
              <option selected>동네를 선택해주세요</option>
            </select>
          </div>
        </div>
        <div class="col-sm-2 col-0"></div>
      </div>
    ...
    </template>
    ```

    ![image-20220818090742128-16607812723571](Trouble%20shooting.assets/image-20220818090742128-16607812723571.png)
  - 변경 후

    ```vue
    <template>
      <!-- 서치 배너 -->
      <div class="search row">
        <div class="col-sm-2 col-md-4 col-0"></div>
        <div class="search-box col-sm-8 col-md-4 col-12">
          <div class="d-flex justify-content-center">
            <input class="search-input pl-3" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="beforeSearch()">        
            <button class="search-btn" type="submit" @click="beforeSearch()">
              <span class="material-symbols-outlined d-flex align-items-center justify-content-center">search</span>
            </button>
          </div>
          <!-- 필터링 파트 -->
          <div class="d-flex justify-content-center">
            <select class="sido pl-3 active" @change="beforeFetchSigungu($event)">
              <option value="null">지역을 선택해주세요</option>
              <option v-for="loc in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
            </select>
            <!-- 시도가 선택되면 활성화 -->
            <select class="sigungu pl-3 active" @change="beforeFetchSearch($event)" v-if="this.info.sido">
              <option selected>동네를 선택해주세요</option>
              <option v-for="loc in sigungu" :key="loc.pk" :value="loc.sigungu">{{ loc.sigungu }}</option>
            </select>
            <select class="sigungu pl-3" v-if="!this.info.sido" disabled>
              <option selected>동네를 선택해주세요</option>
            </select>
            <!-- 리셋버튼 -->
            <button class="reset d-flex align-items-center justify-content-center" @click="reset">
              <span class="material-symbols-outlined">autorenew</span>
            </button>
          </div>
        </div>
        <div class="col-sm-2 col-md-4 col-0"></div>
      </div>
    ...
    </template>
    ```

    ![image-20220818091229813-16607815513283](Trouble%20shooting.assets/image-20220818091229813-16607815513283.png)



---