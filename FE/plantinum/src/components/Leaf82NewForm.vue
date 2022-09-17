<template>
  <div class="leaf82-new-form row">
    <div class="col-md-3 col-0"></div>
    <div class="main col-md-6 py-5 my-5">
      <div class="title-box col-12 d-flex justify-content-center py-3">
        <p class="title">잎팔이 등록하기</p>
      </div>
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
      <div class="right mt-3 row">
        <div class="col-md-2"></div>
        <div class="col-md-8 col-12">
          <div class="plantname d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.plantname" placeholder="식물명을 입력해주세요">
          </div>
          <div class="price d-flex justify-content-start py-2">
            <input type="text" v-model="credentials.price" placeholder="가격">
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
          </div>
          <div class="content d-flex justify-content-start py-2">
            <textarea name="content" id="content" cols="30" rows="10" v-model="credentials.content" placeholder="회원님의 식물을 소개해주세요"></textarea>
          </div>
          <div class="btns row d-flex justify-content-end py-3">
            <div class="submit col-2 d-flex justify-content-end">
              <button @click="beforecreateLeaf82(credentials)">등록</button>
            </div>
            <div class="cancel col-2">
              <router-link :to="{ name : 'leaf82' }" class="d-flex justify-content-end">
                <button>취소</button>
              </router-link>
            </div>
          </div>
        </div>
        <div class="col-md-2"></div>
      </div>
    </div>
    <div class="col-md-3 col-0"></div>
  </div>
</template>

<script>
import { mapActions , mapGetters } from 'vuex'

export default {
  name: 'Leaf82NewForm',
  data() {
    return {
      credentials: {
        photo: '',
        plantname: '',
        price: '',
        sido: '',
        sigungu: '',
        category_class: '분양해요',
        content: '',
      },
      preview: 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg'
    }
  },

  methods: {
    ...mapActions(['fetchSido', 'fetchSigungu', 'createLeaf82']),

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

    beforecreateLeaf82(credentials) {
      if (!credentials.plantname) {
        alert('식물이름을 입력해주세요')
      } else if (credentials.plantname.length > 20) {
        alert('식물이름은 최대 20글자입니다.')
      } else if (parseInt(credentials.price) > 10000000) {
        alert('최대 등록 금액은 10,000,000원입니다.')
      } else if (!credentials.price || !Number.isInteger(parseInt(credentials.price))) {
        alert('가격은 숫자만 입력이 가능합니다.')
      } else if (!credentials.sigungu) {
        alert('지역 및 동네를 선택해주세요.')
      } else if (!credentials.content) {
        alert('식물 소개글을 작성해주세요')
      } else {
        if (typeof credentials.photo == 'string' || credentials.photo instanceof String) {
          credentials.photo = ''
        }
        this.createLeaf82(credentials)
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
  },

  computed: {
    ...mapGetters(['sido', 'sigungu'])
  },

  created() {
    this.fetchSido()
  },
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

.title{
  font-size: 2rem;
  font-weight: bold;
}

.img-box img{
  height: 300px;
  width: 300px;
  border-radius: 1rem;
  object-fit: cover;
}

.img-add span {
  font-size: 1rem;
}

.img-add:hover {
  cursor: pointer;
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
  border-radius: 0.5rem;
  padding-left: 0.5rem;
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

select:focus {
  outline: none;
}

input {
  display: block;
  border-radius: 0.5rem;
  height: 2.5rem;
  padding-left: 0.5rem;
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
  display: block;
  padding-left: 0.5rem;
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

button:focus {
  outline: none;
}

.cancel a button:hover{
  background-color: #d2d2d2;
  transition: all 0.5s;
}
</style>