import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export const Myplant = {
  state: {
    myplants: [],
    myplant: {},
    plant_list: [],
  },
  getters: {
    myplants: state => state.myplants,
    myplant: state => state.myplant,
    plant_list: state => state.plant_list,
    isOwner: (state, getters) => {
      return state.myplant.user?.username === getters.currentUser.username
    }
  },
  mutations: {
    SET_MYPLANTS: (state, myplants) => state.myplants = myplants,
    SET_MYPLANT: (state, myplant) => state.myplant = myplant,
    SET_PLANTLIST: (state, plant_list) => state.plant_list = plant_list,
  },
  actions: {
    fetchMyplants({ commit, getters }, { username }) {
      axios ({
        url : drf.myplant.myplant(username),
        method : 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_MYPLANTS', res.data))
      .catch(err => {
        console.log(err)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },

    searchPlant({ commit, getters }) {
      axios ({
        url : drf.myplant.plantSearch(),
        method: 'get',
        headers : getters.authHeader,
      })
      .then(res => commit('SET_PLANTLIST', res.data))
      .catch(err => console.log(err))
    },

    createMyplant({ commit, getters }, myplant) {
      axios({
        url: drf.myplant.newMyplant(),
        method: 'post',
        data: myplant,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(res => {
        commit('SET_MYPLANT', res.data)
        router.push({
          name: 'myplantDetail',
          params: { username: getters.currentUser.username, plantPk: getters.myplant.id }
        })
      })
      .catch(error => {
        console.log(error)
      })
    },

    fetchMyplant({ commit, getters }, plantPk) {
      axios({
        url: drf.myplant.myplantDetail(plantPk),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => 
        commit('SET_MYPLANT', res.data)
        )
      .catch(err => {
        console.log(err)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },

    disconnectMyplant({ getters }, plantPk) {
      if (confirm('정말 연결을 해제하시겠습니까?')) {
        axios({
          url: drf.myplant.disconnect(plantPk),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(() => {
          alert('화분의 전원을 꺼주세요.')
          router.go()
        })
        .catch(err => {
          console.log(err)
        })
      }
    },

    deleteMyplant({ commit, getters }, plantPk) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.myplant.myplantDetail(plantPk),
          method: 'delete',
          headers: getters.authHeader,
        })
        .then(() => {
          commit('SET_MYPLANT', {})
          router.push({
            name: 'myplant',
            params: {username: getters.currentUser.username}
          })
        })
        .catch(err => console.error(err))
      }
    },

    updateMyplant({ commit, getters }, { plantPk, nickname, photo, plantname }) {
      axios({
        url: drf.myplant.myplantDetail(plantPk),
        method: 'put',
        data: { nickname, photo, plantname },
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(res => {
        commit('SET_MYPLANT', res.data)
        router.push({
          name: 'myplantDetail',
          params: {
            username: getters.username,
            plantPk: plantPk
          }
        })
      })
      .catch(err => console.error(err))
    }
  },
}