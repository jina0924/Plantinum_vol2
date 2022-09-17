<template>
  <div class="search">
    <div :class="searchBox">
      <div class="d-flex justify-content-center">
        <input class="search-input pl-3" type="text" v-model="info.plantname" placeholder="식물명을 입력해주세요" @keyup.enter="beforeSearch()">        
        <button class="search-btn" type="submit" @click="beforeSearch()">
          <span class="material-symbols-outlined d-flex align-items-center justify-content-center">search</span>
        </button>
      </div>
      <div class="d-flex justify-content-center">
        <select class="sido pl-3 active" @change="beforeFetchSigungu($event)">
          <option value="null">지역을 선택해주세요</option>
          <option v-for="loc in sido" :key="loc.pk" :value="loc.sido">{{ loc.sido }}</option>
        </select>
        <select class="sigungu pl-3 active" @change="beforeFetchSearch($event)" v-if="this.info.sido">
          <option selected>동네를 선택해주세요</option>
          <option v-for="loc in sigungu" :key="loc.pk" :value="loc.sigungu">{{ loc.sigungu }}</option>
        </select>
        <select class="sigungu pl-3" v-if="!this.info.sido" disabled>
          <option selected>동네를 선택해주세요</option>
        </select>
        <button class="reset d-flex align-items-center justify-content-center" @click="reset">
          <span class="material-symbols-outlined">autorenew</span>
        </button>
      </div>
    </div>
  </div>
  <div class="select-box mt-5 mb-3">
    <div class="select d-flex justify-content-end">
      <div :class="create">
        <router-link :to="{ name : 'leaf82New' }" v-if="isLoggedIn">
          <button class="create-btn">
            등록
          </button>
        </router-link>
      </div>
    </div>
  </div>
  <div class="leaf82-sell">
    <div :class="title" v-if="isSell">
      <span class="sell-on pr-2">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-off pl-2" @click="onoff()">분양받아요</span>
    </div>
    <div class="leaf82-list-box row pb-2" v-if="isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sList"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!sList">
        <div class="item px-3 pb-4" v-for="leaf82 in sList" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
            <div class="item-img d-flex justify-content-center">
              <img :src="leaf82.photo" :alt="`${leaf82.plantname} 사진입니다.`">
            </div>
            <div class="item-info">
              <p class="name">{{ leaf82.plantname }}</p>
              <p class="price">{{ leaf82.price }} 원</p>
              <p class="addr">{{ leaf82.addr.sido }} {{ leaf82.addr.sigungu }}</p>
              <p class="status">{{ leaf82.status_class }}</p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!!sList"></div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!sList[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!sList[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!sList[0]"></div>
    </div>
    <div :class="title" v-if="!isSell">
      <span class="sell-off pr-2" @click="onoff()">분양해요</span>
      <span class="divider"> | </span>
      <span class="buy-on pl-2">분양받아요</span>
    </div>
    <div class="leaf82-list-box row pb-2" v-if="!isSell">
      <div class="col-sm-2 col-md-3 col-0" v-if="!!bList"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 row d-flex justify-content-center" v-if="!!bList">
        <div class="item px-3 pb-4" v-for="leaf82 in bList" :key="leaf82.pk">
          <router-link class="route" :to="{ name: 'leaf82Detail', params: { username: leaf82.user.username , posting_addr: leaf82.posting_addr } }">
            <div class="item-img d-flex justify-content-center">
              <img :src="leaf82.photo" :alt="`${leaf82.plantname} 사진입니다.`">
            </div>
            <div class="item-info">
              <p class="name">{{ leaf82.plantname }}</p>
              <p class="price">{{ leaf82.price }} 원</p>
              <p class="addr">{{ leaf82.addr.sido }} {{ leaf82.addr.sigungu }}</p>
              <p class="status">{{ leaf82.status_class }}</p>
            </div>
          </router-link>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!!bList"></div>
      <div class="col-sm-2 col-md-3 col-0" v-if="!bList[0]"></div>
      <div class="leaf82-list col-sm-8 col-md-6 col-0 mt-5" v-if="!bList[0]">
        <div class="d-flex justify-content-center">
          <span class="material-symbols-outlined noplant-icon">macro_off</span>
        </div>
        <div class="noplant-text d-flex justify-content-center">
          <p>등록된 식물이 없습니다.</p>
        </div>
      </div>
      <div class="col-sm-2 col-md-3 col-0" v-if="bList[0]"></div>
    </div>
    <div class="d-flex justify-content-center pb-5" v-if="isSell">
      <button class="more-btn" v-if="!!sellObject.next" @click="more()">- 더보기 -</button>
    </div>
    <div class="d-flex justify-content-center pb-5" v-if="!isSell">
      <button class="more-btn" v-if="!!buyObject.next" @click="more()">- 더보기 -</button>
    </div>
  </div>
</template>

<script>
import { mapActions , mapGetters } from 'vuex'
import router from '@/router'


export default {
  name: 'Leaf82SearchList',

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

    fetchSearch() {
      const params = {
        limit : this.info.limit,
        page: this.info.page,
        category_class: '분양해요',
      }
      this.search(params)
    },

    beforeSearch() {
      if (!!this.info.plantname === true && !!this.info.sido === true && !!this.info.sigungu === true) {
        this.info.page = 1
        const params = this.info
        this.search(params)
      } else if (!!this.info.plantname === true && !!this.info.sigungu === false) {
        this.info.page = 1
        const params = {
          plantname : this.info.plantname,
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      } else if (!!this.info.plantname === false && !!this.info.sido === true && !!this.info.sigungu === true) {
        this.info.page = 1
        const params = {
          sido: this.info.sido,
          sigungu: this.info.sigungu,
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      } else if (!!this.info.plantname === false && !!this.info.sido === false && !!this.info.sigungu === false) {
        const params = {
          limit: this.info.limit,
          page: this.info.page,
          category_class: this.info.category_class,
        }
        this.search(params)
      }
    },

    beforeFetchSigungu(event) {
      const sido = event.target.value
      if (sido === 'null') {
        if (this.info.plantname !== '') {
          this.info.sido = ''
          this.info.sigungu = ''
          this.info.page = 1
          if (this.isSell) {
            const params = {
              plantname: this.info.plantname,
              page: this.info.page,
              limit: this.info.limit,
              category_class: '분양해요'
            }
            this.search(params)
          } else {
            const params = {
              plantname: this.info.plantname,
              page: this.info.page,
              limit: this.info.limit,
              category_class: '분양받아요'
            }
            this.search(params)
          }
        } else {
          this.info.sido = ''
          this.info.sigungu = ''
          this.info.page = 1
          if (this.isSell) {
            const params = {
            category_class: '분양해요',
            page: this.info.page,
            limit: this.info.limit
            }
            this.search(params)
          } else {
            const params = {
            category_class: '분양받아요',
            page: this.info.page,
            limit: this.info.limit
            }
            this.search(params)
          }
        }       
      } else {
        this.info.sido = sido
        this.fetchSigungu(sido)
      }
    },

    beforeFetchSearch(event) {
      const sigungu = event.target.value
      this.info.sigungu = sigungu
      if (!this.info.plantname) {
        this.info.page = 1
        const params = {
          sido: this.info.sido,
          sigungu: this.info.sigungu,
          category_class: this.info.category_class,
          page: this.info.page,
          limit: this.info.limit
        }
        this.search(params)
      } else {
        this.info.page = 1
        const params = this.info
        this.search(params)
      }
    },

    reset() {
      this.info.plantname = ''
      this.info.sido = ''
      this.info.sigungu = ''
      // this.fetchSearch()
      router.go()
    },

    onoff() {
      this.isSell = !this.isSell
      if(this.isSell) {
        this.info.category_class = '분양해요'
      } else {
        this.info.category_class = '분양받아요'
      }
      if (this.isSell) {
        if (!!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          this.search(this.info)
        } else if (!!this.info.plantname && !this.info.sigungu) {
          this.info.page = 1
          const params ={
            plantname: this.info.plantname,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else if (!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          const params ={
            sido: this.info.sido,
            sigungu: this.info.sigungu,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else {
          this.info.page = 1
          const params ={
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)            
        }
      } else {
        if (!!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          this.search(this.info)
        } else if (!!this.info.plantname && !this.info.sigungu) {
          this.info.page = 1
          const params ={
            plantname: this.info.plantname,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else if (!this.info.plantname && !!this.info.sigungu) {
          this.info.page = 1
          const params ={
            sido: this.info.sido,
            sigungu: this.info.sigungu,
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)          
        } else {
          this.info.page = 1
          const params ={
            category_class: this.info.category_class,
            page: this.info.page,
            limit: this.info.limit
          }
          this.search(params)
        }
      }
    },

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

    changeDevice() {
      if (this.device === 'PC') {
        this.searchBox = 'search-box PC'
        this.create = 'create PC'
        this.title = 'title PC d-flex justify-content-center mb-5'
      } else if (this.device === 'Tablet') {
        this.searchBox = 'search-box tablet'
        this.create = 'create tablet'
        this.title = 'title tablet d-flex justify-content-center mb-5'
      } else {
        this.searchBox = 'search-box mobile'
        this.create = 'create mobile'
        this.title = 'title mobile d-flex justify-content-center mb-5'
      }
    },
  },

  computed: {
    ...mapGetters(['sido', 'sigungu', 'isLoggedIn', 'sellObject', 'sellList', 'buyObject', 'buyList', 'device'])
  },

  created() {
    this.fetchSearch()
    this.changeDevice()
  },

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

<style scoped>
div {
  margin: 0;
  padding: 0;
}

.search {
  background: url('@/assets/Leaf82/searchbar_pic_0.jpg') bottom right;
  padding-top: 175px;
  padding-bottom: 175px;
  background-size: cover;
}

.search-box.PC {
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
  font-size: 1.2rem;
  margin-right: 25%;
  margin-left: 25%;
}

.search-box.tablet {
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
  font-size: 1.2rem;
  margin-right: 20%;
  margin-left: 20%;
}

.search-box.mobile {
  border-radius: 0.5rem;
  box-shadow: 0rem 0rem 1rem #d2d2d2;
  font-size: 0.8rem;
  margin-right: 10%;
  margin-left: 10%;
}

.search-input {
  width: 90%;
  height: 2.5rem;
  border: 0;
  border-top-left-radius: 0.5rem;
}

.search-input:focus {
  outline: none;
}

.search-btn {
  width: 10%;
  border: 0;
  background-color: white;
  border-top-right-radius: 0.5rem;
  color: black;
}

.search-btn:focus {
  outline: none;
}

.search-btn:hover {
  cursor: pointer;
}

select {
  height: 2.5rem;
  width: 45%;
}

select:focus {
  outline: none;
}

.active:hover {
  cursor: pointer;
}

.sido {
  border-color: #d2d2d2;
  border-left: none;
  border-bottom: none;
  border-bottom-left-radius: 0.5rem;
}

.sigungu {
  border-color: #d2d2d2;
  border-left: none;
  border-right: none;
  border-bottom: none;
}

.reset {
  width: 10%;
  height: 2.5rem;
  padding-top: 0;
  padding-bottom: 0;
  border-color: #d2d2d2;
  border-right: none;
  border-bottom: none;
  border-width: 1px;
  background-color: white;
  border-bottom-right-radius: 0.5rem;
  color: black;
}

.reset:focus {
  outline: none;
}

.reset:hover {
  cursor: pointer;
}

.create.PC {
  width: 4rem;
  margin-right: 25%;
}

.create.tablet {
  width: 4rem;
  margin-right: 20%;
}

.create.mobile {
  width: 4rem;
  margin-right: 10%;
  margin-bottom: 1rem;
}

.create-btn {
  width: 100%;
  border: none;
  background-color: #b2c9ab;
  color: white;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  height: 1.8rem;
}

.create-btn:focus {
  outline: none;
}

.create-btn:hover {
  cursor: pointer;
  background-color: #65805d;
  transition: all 0.5s;
}

/* 리스트 영역 */

.title.PC {
  font-size: 2rem;
}

.title.tablet {
  font-size: 2rem;
}

.title.mobile {
  font-size: 1.6rem;
}

.divider {
  font-weight: bold;  
}

.sell-on {
  font-weight: bold;
}

.buy-off {
  color: #7E7E7E;
}

.buy-off:hover {
  color: black;
  cursor: pointer;
}

.sell-off {
  color: #7E7E7E;
}

.sell-off:hover {
  color: black;
  cursor: pointer;  
}

.buy-on {
  font-weight: bold;
}

p {
  margin: 0;
}

.item img {
  width: 130px;
  height: 130px;
  object-fit: cover;
}

.item-info .name {
  font-size: 1rem;
}

.item-info .price {
  font-size: 0.8rem;
  font-weight: bold;
}

.item-info .addr {
  font-size: 0.8rem;
}

.item-info .status {
  font-size: 0.7rem;
  color: #A6A6A6;
}

.noplant-icon {
  color: #A6A6A6;
  font-size: 15rem;
}

.noplant-text {
  color: #A6A6A6;
  font-size: 1.2rem;
}

a {
  color: black;
  text-decoration: none;
}

.more-btn {
  background-color: transparent;
  border: none;
  color: #7E7E7E;
}

.more-btn:hover {
  cursor: pointer;
  color: #65805d;
}
</style>