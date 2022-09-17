export const Viewport = {
  state: {
    device: ''
  },
  getters: {
    device: state => state.device,
  },
  mutations: {
    SET_DEVICE: (state, device) => state.device = device
  },
  actions: {
    setDevice({commit}, viewWidth) {
      let device = ''
      if (viewWidth <= 420) {
        device = 'Mobile'
      } else if (576 < viewWidth && viewWidth <= 920) {
        device = 'Tablet'
      } else {
        device = 'PC'
      }
      commit('SET_DEVICE', device)
    },

    getDevice({commit}) {
      let device = ''
      // console.log(window.innerWidth)
      if (window.innerWidth <= 420) {
        device = 'Mobile'
      } else if (576 < window.innerWidth && window.innerWidth <= 920) {
        device = 'Tablet'
      } else {
        device = 'PC'
      }
      // console.log(device)
      commit('SET_DEVICE', device)
    }
  },
}