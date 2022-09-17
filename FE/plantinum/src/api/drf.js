// const HOST = 'http://127.0.0.1:8000/api/v1/'
const HOST = 'http://i7a109.p.ssafy.io/api/v1/'

const ACCOUNTS = 'accounts/'

const PLANTS = 'plants/myplant/'

const LEAF82 = 'leaf82/'

export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'signup/',
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: () => HOST + ACCOUNTS + 'profile/',
    updateProfile: () => HOST + ACCOUNTS + 'userinformation/',
    changePassword: () => HOST + ACCOUNTS + 'password/' + 'change/',
    signout: () => HOST + ACCOUNTS + 'withdraw/',
    nickname: (username) => HOST + ACCOUNTS + 'nickname/' + `${username}/`
  },
  myplant: {
    plantSearch: () => HOST + 'plants/' + 'search/',
    myplant: (username) => HOST + PLANTS + `${username}/`,
    newMyplant: () => HOST + PLANTS, 
    myplantDetail: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'detail/',
    plantOTP: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'otp/',
    otpStatus: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'otp/' + 'status/',
    disconnect: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'disconnect/',
    removeOTP: (plantPk) => HOST + PLANTS + `${plantPk}/` + 'otp/' + 'remove/'
  },
  leaf82: {
    leaf82: () => HOST + LEAF82 + 'main',
    sido: () => HOST + LEAF82 + 'search/sido/',
    sigungu: (sido) => HOST + LEAF82 + `search/${sido}/` + 'sigungu/',
    search: () => HOST + LEAF82 + 'search',
    new: () => HOST + LEAF82 + 'new/',
    detail: (username, posting_addr) => HOST + LEAF82 + `${username}/` + `${posting_addr}/`
  }
}