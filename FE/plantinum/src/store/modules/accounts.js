import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export const Account = {
  state: {
    token: localStorage.getItem('token') || '' ,
    currentUser: {},
    authError: null,
    profile: {},
    username: localStorage.getItem('username') || '',
    leaf82Set: []
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}`}),
    profile: state => state.profile,
    username: state => state.username,
    leaf82Set: state => state.leaf82Set
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => {
      state.currentUser = user
      state.username = user.username
    },
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_PROFILE: (state, profile) => {
      state.profile = profile,
      state.leaf82Set = profile.leaf82_set
    }
  },

  actions: {
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

    resetAuthError({ commit }) {
      commit('SET_AUTH_ERROR', null)
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        dispatch('fetchProfile')
        dispatch('resetAuthError')
        router.push({ name: 'home' })
      })
      .catch(err => {
        console.log(err)
        if(!!err.response.data.username && err.response.data.username[0] === '해당 사용자 이름은 이미 존재합니다.') {
          alert('해당 사용자 이름은 이미 존재합니다.')
        } else if (!!err.response.data.email && err.response.data.email[0] === '유효한 이메일 주소를 입력하십시오.') {
          alert('유효한 이메일 주소를 입력하십시오.')
        } else if (!!err.response.data.email && err.response.data.email[0] === '이미 이 이메일 주소로 등록된 사용자가 있습니다.') {
          alert('이미 등록된 메일입니다.')
        } else if (!!err.response.data.non_field_errors && err.response.data.non_field_errors[0] === '두 개의 패스워드 필드가 서로 맞지 않습니다.') {
          alert('패스워드가 일치하지 않습니다.')
        } else if (!!err.response.data.password1 && err.response.data.password1[0] === '비밀번호가 너무 일상적인 단어입니다.') {
          alert('비밀번호가 단순합니다. 복잡한 비밀번호를 입력해주세요.')
        } else if (!!err.response.data.password1 && err.response.data.password1[0] === '비밀번호가 전부 숫자로 되어 있습니다.') {
          alert('비밀번호가 전부 숫자로 되어 있습니다.')
        } else if (!!err.response.data.password1 && err.response.data.password1[0] === '비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.') {
          alert('비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.')
        } else {
          alert('다시 입력해주세요.')
        }
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    
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
        dispatch('resetAuthError')
        router.push({ name: 'home' })
      })
      .catch(err => {
        console.log(err)
        alert('다시 한 번 작성해주세요.')
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
      .catch(err => {
        alert('잘못된 접근입니다.')
        console.log(err)
      })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          localStorage.setItem('username', res.data.username)
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          console.log(err)
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    fetchAuthError({ commit }, authState) {
      commit('SET_AUTH_ERROR', authState)
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
        console.log(err)
        if (err.response.status === 404) {
          router.push({ name: 'NotFound404' })
        }
      })
    },
    
    updateProfile({ commit, getters, }, info) {
      axios({
        url: drf.accounts.updateProfile(),
        method: 'put',
        data: info,
        headers: {
          ...getters.authHeader,
          'Content-Type': 'multipart/form-data',
        },
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
          router.push({ name: 'profile' })
        })
        .catch(err => {
          console.log(err)
          if (!!err.response.data && err.response.data.phone_number[0] === '사용자의 phone number은/는 이미 존재합니다.') {
            alert('이미 등록되어 있는 전화번호입니다.')
          } else if (!!err.response.data && err.response.data.email === '이메일이 이미 존재합니다.') {
            alert('이미 등록되어 있는 이메일입니다.')
          } else if (!!err.response.data && err.response.data.nickname === '닉네임이 이미 존재합니다.') {
            alert('이미 사용중인 닉네임입니다.')
          } else {
            alert('잘못된 접근입니다.')
            commit('SET_AUTH_ERROR', err.response.data)
            router.push({ name: 'updateProfile' })
            if (err.response.status === 401) {
              router.push({ name: 'updateProfile' })
            }
          }
        })
    },

    changePassword({getters, dispatch}, credentials) {
      axios({
        url : drf.accounts.changePassword(),
        method : 'post',
        data : credentials,
        headers : getters.authHeader
      })
      .then(() => {
        dispatch('removeToken')
        dispatch('resetCurrentUser')
        dispatch('resetProfile')
        alert('비밀번호가 변경되었습니다. 재로그인해주세요.')
        router.push({ name: 'login' })
      })
      .catch(err => {
        console.log(err)
        alert('다음과 같은 같은 상황입니다.\n - 단순한 비밀번호\n - 숫자로 이루어진 비밀번호\n - 짧은 비밀번호\n등등.')
        router.push({ name: 'updatepassword' })
      })
    },
    
    signout({ dispatch , getters }) {
      if (confirm('정말로 탈퇴하시겠습니까?')) {
        axios({
          url: drf.accounts.signout(),
          method: 'delete',
          headers: getters.authHeader
        })
        .then(() =>{
          dispatch('removeToken')
          dispatch('resetCurrentUser')
          dispatch('resetProfile')
          alert('성공적으로 탈퇴되었습니다.')
          router.push({ name: 'home' })          
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  }
}