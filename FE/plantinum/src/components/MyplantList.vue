<template>
  <div>
    <!-- 리스트가 있을 때 -->
    <!-- 정렬 버튼 -->
    <div class="row mx-0">
      <div class="col-1"></div>
      <div class="col-10 jsutify-content-center">
        <div class="sort-btn-div mt-4 d-flex flex-row-reverse" v-if="myplant_list[0]">
          <button class="sort-btn btn" @click="myplantSort()">{{ sort_by }}</button>
        </div>
      </div>
    </div>
    <!-- 내 식물 카드 목록 -->
    <div class="yesplant" v-if="myplant_list[0]">
      <div class="col-1"></div>
      <div class="col-10 row px-0 card-section">
        <div class="card" v-for="plant in myplant_list" :key="plant.pk">
          <router-link class="" :to="{ name: 'myplantDetail', params: { username: username, plantPk: plant.pk } }">
            <div class="plant-img">
              <img :src="plant.photo" :alt="`${plant.nickanme} 사진 입니다.`" class="img-fluid">
            </div>
            <div class="d-flex justify-content-between plant-info">
              <div class="col-7">
                <span class="plant-name">
                  {{ plant.nickname }}
                </span>
              </div>
              <div class="col-5 d-flex justify-content-end align-items-center">
                <span class="material-symbols-outlined no-humidity" v-if="!plant.is_connected">water_drop</span>
                <span class="material-symbols-outlined humidity" v-if="plant.is_connected">water_drop</span>
                <span class="humidity" v-if="plant.is_connected">{{ plant.sensing.moisture_level }} %</span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col-1"></div>
    </div>
    <div class="container">
      <div class="noplant" v-if="!myplants[0]">
        <span class="material-symbols-outlined noplant-icon">
          macro_off
        </span>
        <p>등록된 식물이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script scoped>
import { mapGetters } from 'vuex'

export default {
  name : 'MyplantList',
  data() {
    return {
      sort_by : '등록순↓',
      myplant_list : [],
    }
  },
  props : {
    myplants: Array,
  },
  computed : {
    ...mapGetters(['username']),
  },
  watch: {
    myplants() {
      this.myplant_list = this.myplants
    }
  },
  methods : {
    myplantSort() {
      if (this.sort_by === '등록순↓') {
        this.sort_by = '이름순↓'
        this.myplant_list.sort(function(a, b){
          return a.nickname.localeCompare(b.nickname)
        })
      } else if (this.sort_by === '이름순↓') {
        this.sort_by = '등록순↓'
        this.myplant_list.sort(function(a, b){
          return b.pk - a.pk
        })
      }
    },
  },
}
</script>

<style scoped>
.yesplant {
  position: flex;
  justify-content: center;
  margin: auto;
}

.sort-btn {
  background-color: white;
  color: #B2C9AB;
  border-color: #B2C9AB;
}

.sort-btn:focus {
  background-color: white;
  color: #B2C9AB;
  border-color: white;
  box-shadow: 0 0 .5rem #B2C9AB;
  transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}

.card-section {
  margin: auto;
  display: flex;
  justify-content: center;
}

.card {
  border-radius: 10px;
  border-style: none;
  width: 16rem;
  margin: 1rem;
  padding: 0 auto;
  box-shadow: 0 0 .5rem #edeae2;
}

.card a {
  text-decoration-line: none;
  color: black;
}

.plant-img {
  position: relative; 
  width: 250px;
  height: 250px;
  margin: auto;
}

.plant-img img {
  padding: 0.5rem;
  border-radius: 20px;
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.plant-info {
  font-size: 1rem;
  margin: 1rem 0;
}

.diary-count {
  font-size: 0.5rem;
  color: #A17C6B;
}

.humidity {
  font-size: 1rem;
  color: #18A7DB;
}

.no-humidity {
  font-size: 1rem;
  color: gray;
}

.material-symbols-outlined {
  font-size: 1.5rem;
}

.noplant-icon {
  font-size: 14rem;
}

.container {
  margin: 3rem auto;
}

.noplant {
  color: #A6A6A6;
  margin: 5rem, auto;
  text-align: center;
  font-size: 1.5rem;
}
</style>