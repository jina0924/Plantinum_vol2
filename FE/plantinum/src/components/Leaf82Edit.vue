<template>
  <div class="leaf82-new-form row">
    <div class="col-md-3 col-0"></div>
    <div class="main col-md-6 py-5 my-5">
      <div class="title-box col-12 d-flex justify-content-center py-3">
        <p class="title">잎팔이 수정하기</p>
      </div>
      <div class="left">
        <div class="img-box d-flex justify-content-center">
          <img :src="preview" alt="등록될 사진입니다.">
        </div>
        <div class="img-add-box d-flex justify-content-center pt-2">
          <label for="pic-file" class="img-add">
            <span class="material-symbols-outlined img-add-icon">photo_camera</span>
            <span>사진 변경하기</span>
          </label>
          <input type="file" id="pic-file" @change="onInputImage" accept="image/*" ref="leaf82Image">
          <span class="px-2">|</span>
          <label for="photo-delete">
            <span @click="onDeleteImage" class="img-delete-btn img-add">
              <span class="material-symbols-outlined img-add-icon">imagesmode</span>
              <span>기본 이미지로</span>
            </span>
          </label>
        </div>
      </div>
      <div class="right mt-3 row">
        <div class="col-md-2"></div>
        <div class="col-md-8 col-">
          <div class="title d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.plantname">
          </div>
          <div class="price d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.price">
          </div>
          <div class="addr d-flex justify-content-start py-2">
            <select name="sido" id="" @change="beforeFetchSigungu($event)" class="mr-1">
              <option selected>지역을 선택해주세요</option>
              <option v-for="(loc) in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
            </select>
            <select name="sigungu" id="" @change="selectSigungu($event)" v-if="this.credentials.sido" class="mr-1">
              <option selected>동네를 선택해주세요</option>
              <option v-for="(loc2) in sigungu" :key="loc2.pk" :value="loc2.sigungu">{{ loc2.sigungu }}</option>
            </select>
            <select name="sigungu" id="" v-if="!this.credentials.sido" disabled class="mr-1">
              <option selected>동네를 선택해주세요</option>
            </select>
            <select name="category_class" id="category_class" @change="selectCategory($event)" class="mr-1">
              <option value="분양해요">분양해요</option>
              <option value="분양받아요">분앙받아요</option>
            </select>
            <select name="status_class" id="status_class" @change="selectStatus($event)" class="mr-1">
              <option value="분양대기">분양대기</option>
              <option value="분양예약">분양예약</option>
              <option value="분양완료">분양완료</option>
            </select>
          </div>
          <div class="content d-flex justify-content-start py-">
            <textarea name="content" id="content" cols="30" rows="10" v-model="credentials.content" placeholder="회원님의 식물을 소개해주세요"></textarea>
          </div>
          <div class="btns row d-flex justify-content-end py-3">
            <div class="submit col-2 d-flex justify-content-end">
              <button @click="beforeUpdateLeaf82(credentials)">등록</button>
            </div>
            <div class="cancel col-2">
              <router-link :to="{ name : 'leaf82Detail' , params : { username: info.username , posting_addr: info.posting_addr } }" class="d-flex justify-content-end">
                <button>취소</button>
              </router-link>
            </div>
          </div>
          <div class="col-md-2"></div>
        </div>
      </div>
    </div>
    <div class="col-md-3 col-0"></div>
  </div>
</template>

<script>
import router from '@/router'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Leaf82Edit',
  data() {
    return {
      info: {
        username: this.$route.params.username,
        posting_addr: this.$route.params.posting_addr
      },
      credentials: {
        sido: '',
        sigungu: '',
        plantname: '',
        content: '',
        price: '',
        category_class: '',
        status_class: '',
        photo: '',
      },
      preview: ''
    }
  },
  methods: {
    ...mapActions(['updateLeaf82', 'fetchSido', 'fetchSigungu',]),

    fillCredentials() {
      this.credentials.sido = this.leaf82Detail.addr.sido
      this.credentials.sigungu = this.leaf82Detail.addr.sigungu
      this.credentials.plantname = this.leaf82Detail.plantname
      this.credentials.content = this.leaf82Detail.content
      this.credentials.price = this.leaf82Detail.price
      this.credentials.category_class = '분양해요'
      this.credentials.status_class = '분양대기'
      this.credentials.photo = this.leaf82Detail.photo
    },

    makeImgUrl() {
      this.preview = this.credentials.photo
    },

    beforeFetchSigungu(event) {
      let tmp = event.target.value
      this.credentials.sido = tmp
      this.fetchSigungu(this.credentials.sido)
    },

    selectSigungu(event) {
      let tmp = event.target.value
      this.credentials.sigungu = tmp
    },

    selectCategory(event) {
      let tmp = event.target.value
      this.credentials.category_class = tmp
    },

    selectStatus(event) {
      let tmp = event.target.value
      this.credentials.status_class = tmp
    },

    beforeUpdateLeaf82(credentials) {
      if (!credentials.plantname) {
        alert('이름을 입력해주세요.')
      } else if (!credentials.price || !Number.isInteger(parseInt(credentials.price))) {
        alert('가격을 확인해주세요.')
      } else if (!credentials.sigungu) {
        alert('주소를 선택해주세요.')
      } else if (!credentials.content) {
        alert('식물을 소개해주세요')
      } else {
        if (!!credentials.photo && typeof credentials.photo == 'string' || credentials.photo instanceof String) {
          credentials.photo = 'same'
        }
        const updateInfo = {
          credentials,
          info: this.info
        }
        this.updateLeaf82(updateInfo)
      }
    },

    onInputImage() {
      if (this.$refs.leaf82Image.files[0].size > 31457280) {
        alert('사진이 너무 큽니다. 30MB보다 작은 사진을 선택해주세요.')
      } else {
        this.credentials.photo = this.$refs.leaf82Image.files[0]
        const url = URL.createObjectURL(this.credentials.photo)
        this.preview = url
      }
    },

    onDeleteImage() {
      this.credentials.photo = ''
      this.preview = 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg'
    },

    isMine() {
      if (this.$route.params.username !== this.username) {
        alert('잘못된 접근입니다.')
        router.push({ name: 'leaf82'})
      }
    }
  },
  computed: {
    ...mapGetters(['leaf82Detail', 'sido', 'sigungu', 'username']),
  },
  created() {
    this.isMine()
    this.fetchSido()
  },
  watch: {
    leaf82Detail() {
      this.fillCredentials()
      this.makeImgUrl()
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

.title {
  font-size: 2.5rem;
  font-weight: bold;
}

.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
  object-fit: cover;
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

.right select {
  padding-left: 0.5rem;
  border-radius: 0.5rem;
  display: block;
  width: 100%;
  height: 2.5rem;
  font-size: 1rem;
  line-height: 1.5;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.right select:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

input {
  padding-left: 0.5rem;
  border-radius: 0.5rem;
  height: 2.5rem;
  display: block;
  width: 100%;
  font-size: 1rem;
  line-height: 1.5;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

input:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

textarea {
  padding-left: 0.5rem;
  display: block;
  width: 100%;
  font-size: 1rem;
  line-height: 1.5;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #efefef;
  border-radius: 0.25rem;
  box-shadow: 0.5rem 0.5rem 0.5rem #efefef;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
  resize: none;
}

textarea:focus {
  outline: none;
  border-color: rgba(178, 201, 171, 20% ) ;
  box-shadow: 0.5rem 0.3rem 0.5rem rgba(178, 201, 171, 50% ); 
}

.content {
  height: 10rem;
}

.submit {
  width: 100%;
}

.submit button{
  width: 80%;
  background-color: #b2c9ab;
  border-radius: 0.5rem;
  color: white;
  border: none;
  font-size: 1rem;
  height: 2rem;
}

.submit button:hover {
  background-color: #65805d;
  transition: all 0.5s;
}

.cancel {
  width: 100%;
}

.cancel a {
  width: 100%;
  text-decoration: none;
}

.cancel a button {
  width: 80%;
  background-color: white;
  border-radius: 0.5rem;
  color: gray;
  border-width: 1px;
  border-color: rgb(170, 170, 170);
  font-size: 1rem;
  height: 2rem;
  border-style: solid;
}

button:hover {
  cursor: pointer;
}

.cancel a button:hover{
  background-color: #d2d2d2;
  transition: all 0.5s;
}

</style>