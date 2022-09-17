import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export const Leaf82 = {
  state: {
    sido: [],
    sigungu: [],
    sellObject: {},
    sellList: [],
    buyObject: {},
    buyList: [],
    leaf82Detail: {}
  },

  getters: {
    sido: state => state.sido,
    sigungu: state => state.sigungu,
    sellObject: state => state.sellObject,
    sellList: state => state.sellList,
    buyObject: state => state.buyObject,
    buyList: state => state.buyList,
    leaf82Detail: state => state.leaf82Detail
  },

  mutations: {
    SET_SIDO: (state, sido) => state.sido = sido,
    SET_SIGUNGU: (state, sigungu) => state.sigungu = sigungu,
    SET_SELLOBJECT: (state, sellObject) => {
      state.sellObject = {
        count: sellObject.count,
        next: sellObject.next,
        previous: sellObject.previous
      }
      state.sellList = sellObject.results
    },
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
    SET_LEAF82DETAIL: (state, leaf82Detail) => state.leaf82Detail = leaf82Detail
  },

  actions: {
    resetSigungu({ commit }) {
      commit('SET_SIGUNGU', [])
    },

    resetLeaf82Detail({ commit }) {
      commit('SET_LEAF82DETAIL', {})
    },

    fetchSido({ commit }) {
      axios({
        url: drf.leaf82.sido(),
        method: 'get'
      })
      .then (res => {
        commit('SET_SIDO', res.data)
      })
    },

    fetchSigungu({ commit }, sido) {
      axios({
        url: drf.leaf82.sigungu(sido),
        method: 'get'
      })
      .then(res=> {
        commit('SET_SIGUNGU', res.data)
      })

    },

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

    createLeaf82({ commit, getters }, credentials) {
      axios({
        url: drf.leaf82.new(),
        method: 'post',
        data: credentials,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(res => {
        commit('SET_LEAF82DETAIL', res.data)
        router.push({
          name: 'leaf82Detail',
          params: { username: getters.currentUser.username , posting_addr: getters.leaf82Detail.posting_addr }
        })
      })
      .catch(err => {
        alert('잘못된 접근입니다.')
        console.log(err)
      })
    },

    updateLeaf82({ commit, getters }, {credentials, info}) {
      const username = info.username
      const posting_addr = info.posting_addr
      axios({
        url: drf.leaf82.detail(username, posting_addr),
        method: 'put',
        data: credentials,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(res => {
        commit('SET_LEAF82DETAIL', res.data)
        router.push({
          name: 'leaf82Detail',
          params: { username: username , posting_addr: posting_addr }
        })
      })
      .catch(err => {
        alert('잘못된 접근입니다.')
        console.log(err)
      })
    },

    deleteLeaf82({ getters }, { username, posting_addr }) {
      if (confirm('정말로 삭제하시겠습니까?')) {
        axios({
          url: drf.leaf82.detail(username, posting_addr),
          method: 'delete',
          headers: getters.authHeader,
        })
        .then(() => {
          router.push({ name: 'leaf82' })
          }
        )
        .catch(err => {
          console.log(err)
        })
      }
    },

    fetchLeaf82Detail({ commit, }, {username, posting_addr}) {
      axios({
        url: drf.leaf82.detail(username, posting_addr),
        method: 'get',
      })
      .then(res => {
        commit('SET_LEAF82DETAIL', res.data)
      })
      .catch(err => {
        console.log(err)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    }
  },
}