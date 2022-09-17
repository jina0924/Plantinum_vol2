<template>
  <div class="wrapper">
    <div class="form-bg col-md-6 p-5">
      <h3 class="form-title mb-4">내 식물 등록</h3>
      <form @submit.prevent="onSubmit">
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
        <div class="input-text-group">
          <div class="mb-3">
            <input v-model="newMyplant.nickname" type="text" class="form-input" id="myplantNickname" placeholder="식물 닉네임을 입력해주세요.">
          </div>
          <div class="select-plant mb-3" v-if="action==='create'">
            <input type="text" id="plant" list="search-plant-list" placeholder="식물 종류를 검색하세요." class="form-input" v-model="newMyplant.plantname">
            <datalist id="search-plant-list">
              <option v-for="(plant) in plant_list" :key="plant.pk">{{ plant.name }}</option>
            </datalist>
            <input v-if="newMyplant.plantname==='직접 입력하기'" type="text" id="tmp-plant" placeholder="식물 종류를 직접 입력해주세요." class="form-input mt-3" v-model="newMyplant.tmp">
          </div>
          <div class="select-plant mb-3" v-if="action==='update'">
            <input v-if="newMyplant.plantname!=='직접 입력하기'" type="text" id="plant" :placeholder="myplant.plant_info?.name" class="form-input disabled-input" disabled>
            <input v-if="newMyplant.plantname==='직접 입력하기'" type="text" id="plant" :placeholder="myplant.tmp" class="form-input disabled-input" disabled>
          </div>
        </div>
        <div class="myplant-create-submit">
          <router-link :to="{ name: 'myplant', params: { username: username } }" v-if="action==='create'">
            <button class="form-btn back-btn">뒤로가기</button>
          </router-link>
          <router-link :to="{ name: 'myplantDetail', params: { username: username, plantPk: $route.params.plantPk } }" v-if="action==='update'">
            <button class="form-btn back-btn">뒤로가기</button>
          </router-link>
          <button class="form-btn myplant-create-submit-btn">등록</button>
        </div>
      </form>
    </div>
  </div>
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
  computed: {
    ...mapGetters(['username', 'plant_list']),
  },
  methods: {
    ...mapActions(['createMyplant', 'searchPlant', 'updateMyplant']),
    onInputImage() {
      if (this.$refs.newMyplantImage.files[0].size > 31457280) {
        alert('사진이 너무 큽니다. 30MB보다 작은 사진을 선택해주세요.')
      } else {
        this.newMyplant.photo = this.$refs.newMyplantImage.files[0]
        const url = URL.createObjectURL(this.newMyplant.photo)
        this.newMyplantImage = url
      }
    },
    onDeleteImage() {
      this.newMyplant.photo = ''
      this.newMyplantImage = 'https://plantinum.s3.ap-northeast-2.amazonaws.com/static/monstera.jpg'
    },
    onSubmit() {
      if (!this.newMyplant.nickname) {
        alert('식물 닉네임을 입력해주세요.')
      } else if (this.newMyplant.nickname.length > 10) {
        alert('식물 닉네임을 10자 이하로 등록해주세요.')
      } else if (!this.newMyplant.plantname) {
        alert('식물 종류를 등록해주세요.')
      }
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

<style scoped>
.wrapper {
  display: flex;
  justify-content: center;
}

.form-bg {
  background-color: white;
  border-radius: 15px;
}

.form-title {
  text-align: center;
  font-weight: 700;
  color: #65805D;
}

.img-section {
  position: relative;
}

.preview-section {
  display: flex;
  justify-content: center;

}

.preview-myplant-image {
  border-radius: 15px;
  width: 20rem;
  height: 20rem;
  object-fit: cover;
}

.img-add-div {
  display: flex;
  font-size: 1rem;
  justify-content: center;
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

.input-text-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.form-input {
  display: block;
  width: 85%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  margin: auto;
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

.disabled-input {
  background-color: #f5f5f5;
}

.myplant-create-submit {
  display: flex;
  justify-content: flex-end;
}

.form-btn {
  cursor: pointer;
  border: none;
  margin: 0.5rem 1rem 0.5rem 0;
  font-weight: 500;
  padding: 0 1rem;
  border-radius: 12px;
  height: 45px;
}

.form-btn:focus {
  outline: none;
}

.back-btn:hover {
  background-color: #d2d2d2;
  transition: all 0.5s;
}

.myplant-create-submit-btn {
  background-color: #b2c9ab;
  color: white;
  font-size: 1rem;
}

.myplant-create-submit-btn:hover {
  background-color: #65805d;
  transition: all 0.5s;
}

</style>