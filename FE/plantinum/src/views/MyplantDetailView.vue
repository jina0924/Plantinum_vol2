<template>
  <div class="detail-back">
    <nav-bar></nav-bar>
    <div class="container">
      <div class="plant-profile">
        <div class="profile-body row justify-content-center align-items-center">

          <div class="plant-profile-img">
            <img :src="myplant.photo" :alt="`${myplant.nickname} 사진`" class="myplant-img">
          </div>
          <div class="col-lg-5 col-xl-6 plant-profile-info">
            <h2 class="myplant-nickname">{{ myplant.nickname }}</h2>
            <!-- 수정/삭제 버튼 -->
            <div v-if="isOwner" class="owner-btn">
              <router-link :to="{ name: 'myplantEdit', params: { plantPk: myplantPk } }" class="edit-btn">
                <span class="material-symbols-outlined">drive_file_rename_outline</span>
              </router-link>
              <span @click="deleteMyplant(myplantPk)" class="material-symbols-outlined delete-btn">delete</span>
            </div>

            <div v-if="myplant.plant_info?.name!=='직접 입력하기'" class="myplant-data botanical-name">{{ myplant.plant_info?.name }}</div>
            <div v-if="myplant.plant_info?.name==='직접 입력하기'" class="myplant-data botanical-name tmp-name">{{ myplant.tmp }}</div>
            <div class="myplant-data row">
              <span class="col-md-5 col-xl-4 info-title">토양 습도</span>
              <progress v-if="myplant.is_connected" :value="myplant.sensing?.moisture_level" max="100" class="moisture-level col-md-7 col-xl-8"></progress>
              <progress v-if="!myplant.is_connected" value="0" max="100" class="moisture-level col-md-7 col-xl-8"></progress>
              <span class="moisture-level-percent" v-if="myplant.is_connected">{{ myplant.sensing?.moisture_level }}%</span>
            </div>
            <div class="myplant-data row">
              <span class="col-md-5 col-xl-4 info-title">등록 날짜</span>
              <span class="col-md-7 col-xl-8">{{ myplantCreatedAt }}</span>
            </div>
            <div class="myplant-data row">
              <span class="col-md-5 col-xl-4 info-title">최근 관수 날짜</span>
              <span class="col-md-7 col-xl-8" v-if="myplant.is_connected">{{ myplant.sensing?.last_watering }}</span>
              <span class="col-md-7 col-xl-8 not-connected" v-if="!myplant.is_connected">알 수 없음</span>
            </div>
            <div class="row plant-btn-group">

              <button class="btn plant-info-btn" type="button" @click="changeModal(1)">계절별 식물 관리 정보</button>
              <button v-if="myplant.plant_info?.specl_manage_info" class="btn plant-info-btn" @click="changeModal(2)">특별 관리 정보</button>
              <div class="otp">
                <!-- 연결 끊기 -->
                <button v-if="!!myplant.is_connected" @click="disconnectMyplant(myplantPk)" class="btn plant-info-btn plant-info-btn-end">{{ isConnected }}</button>
                <!-- SuPool 연결 -->
                <button v-if="!myplant.is_connected && !temp_OTP" @click="[fetchOTP(myplantPk), fetchMyplant(myplantPk), startTimer(), changeModal(3)]" class="btn plant-info-btn plant-info-btn-end">{{ isConnected }}</button>
                <!-- 연결중 -->
                <button v-if="!myplant.is_connected && !!temp_OTP" @click="changeModal(3)" class="btn plant-info-btn plant-info-btn-end">{{ isConnected }}</button>
              </div>

              <!-- 정보 모달 -->
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
                  <!-- 특별 관리 정보 모달 -->
                  <div v-if="modal===2">
                    <h5>특별 관리 정보</h5>
                    <p>{{ myplant.plant_info?.specl_manage_info }}</p>
                  </div>
                  <button class="modal-close-btn">닫기</button>
                </div>
              </div>

              <!-- OTP 모달 -->
              <div class="black-bg" @click="close($event)" v-if="modal===3 && isOwner">
                <div class="modal-bg myplant-modal">
                  <!-- OTP 모달 -->
                  <div>
                    <div v-if="!myplant.is_connected && !!temp_OTP" class="otp-timer">
                      <div>다음 숫자를 화분에 입력해주세요</div>
                      <div class="otp-number">{{ temp_OTP }}</div>
                      <div v-if="otpTimer > 0">{{ otpTimer }}초</div>
                      <div v-if="otpTimer <= 0">0</div>
                      <div class="d-flex justify-content-center">
                        <progress :value=otpTimer max="60" class="progress-bar"></progress>
                      </div>
                      <button class="modal-close-btn">취소</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="!myplant.is_connected && !temp_OTP" class="supool-info d-flex align-items-center">
              <span class="material-symbols-outlined supool-icon">potted_plant</span>
              <span>SuPool은 Plantinum에서 제작한 자동화 화분입니다</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 식물 일지 부분 -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'MyplantDetailView',
  data() {
    return {
      myplantPk: this.$route.params.plantPk,
      modal: 0,
      interval: 0,
    }
  },
  props: {
    username: String,
  },
  components: { NavBar },
  computed: {
    ...mapGetters(['myplant', 'isOwner', 'temp_OTP', 'otpTimer']),
    myplantCreatedAt() {
      return this.myplant.created_at?.substr(0, 10)
    },
    isConnected() {
      if (this.myplant.is_connected) { 
        return 'SuPool 연결 끊기'
      } else if (this.temp_OTP !== null && this.myplant.is_connected === false) {
        // return 'SuPool 연결중'
        return this.temp_OTP
      } else {
        return 'SuPool 연결'
      }
    },
  },

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

<style scoped>
.detail-back {
  min-height: 95vh;
}

.profile-body { 
  background-color: white;
  border-radius: 15px;
  padding: 3.5rem 2rem;
  margin-top: 3rem;
  margin-bottom: 3rem;
}

.plant-profile-img {
  width: 20rem;
  height: 20rem;
  border-radius: 100%;
  overflow: hidden;
}

.myplant-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.plant-profile-info {
  padding: 0 0 0 5rem;
}

.myplant-nickname {
  font-size: 3.5rem;
  font-weight: 600;
  display: inline;
  margin-right: 1rem;
}

.owner-btn {
  display: inline-block;
  color: #a6a6a6;
  margin-left: auto;
}

.edit-btn {
  text-decoration: none;
  margin-right: .5rem;
  color: inherit;
}

.edit-btn:hover {
  color: #845A49;
}

.delete-btn:hover {
  color: #845A49;
  cursor: pointer;
}

.botanical-name {
  color: #b2c9ab;
  font-family: 'MaruBuri';
  font-size: 1.1rem;
  font-style: italic;
}

.tmp-name {
  color: #f7d489;
}

.myplant-data {
  line-height: 2rem;
  font-size: 1.1rem;
}

.info-title {
  font-weight: 450;
}

.moisture-level {
  appearance: none;
  background-color: white;
  text-align: center;
  margin: auto 0;
  max-width: 11rem;
  height: 1rem;
}
.moisture-level::-webkit-progress-bar {
  background:#E9E9E9;
  border-radius:10px;
}
.moisture-level::-webkit-progress-value {
  border-radius:10px;
  background: #18A7DB;
  transition: width 1s linear;
}

.moisture-level-percent { 
  color: #18A7DB;
}

.not-connected {
  color: #a6a6a6;
}

.plant-btn-group {
  margin: .5rem 0;
}

.plant-info-btn {
  margin: 0.5rem 1rem 0.5rem 0;
  padding: 0 1rem;
  border-radius: 13px;
  height: 45px;
  font-size: 1rem;
  background-color: white;
  color: #a6a6a6;
  border-color: #a6a6a6;
  border-style: solid;
  border-width: thin;
}

.plant-info-btn:hover {
  background-color: #a6a6a6;
  color: white;
  transition: all 0.5s;
}

.plant-info-btn-end {
  margin-right: 0;
  color: #845A49;
  border-color: #845A49;
}

.plant-info-btn-end:hover {
  color: white;
  background-color: #845A49;
  transition: all 0.5s;
}

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
  max-width: 450px;
  margin: 2rem auto;
  background: white ;
  border-radius: 15px;
  padding: 2rem 2rem 1rem 2rem;
}

h5 {
  text-align: center;
}

.season { 
  font-weight: 500;
  font-size: 1.1rem;
  color: #845A49;
  margin: 0.5rem 0;
}

.modal-close-btn {
  cursor: pointer;
  border: none;
  background-color: #b2c9ab;
  color: white;
  font-weight: 500;
  margin: 0.5rem;
  padding: 0 1rem;
  border-radius: 13px;
  height: 45px;
  font-size: 1rem;
  margin-left: auto;
  display: block;
  margin-top: 1.5rem;
}

.modal-close-btn:hover {
  background-color: #65805d;
  transition: all 0.5s;
}

.otp-timer {
  text-align: center;
}

.otp-number{
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0.5rem;
  letter-spacing: 1rem;
}

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

.supool-info {
  font-size: 0.9rem;
  color: #845A49;
  margin-top: 0.7rem;
}

.supool-icon {
  margin-right: 0.7rem;
}
</style>