import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'
import UpdatePasswordView from '@/views/UpdatePasswordView.vue'

import MyplantView from '@/views/MyplantView.vue'
import MyplantNewView from '@/views/MyplantNewView.vue'
import MyplantDetailView from '@/views/MyplantDetailView.vue'
import MyplantEditView from '@/views/MyplantEditView.vue'

import Leaf82View from '@/views/Leaf82View.vue'
import Leaf82NewView from '@/views/Leaf82NewView.vue'
import Leaf82DetailView from'@/views/Leaf82DetailView.vue'
import Leaf82EditView from '@/views/Leaf82EditView'
import MessengerView from '@/views/MessengerView.vue'
import UpdateProfileView from '@/views/UpdateProfileView.vue'

import NotFound404 from '@/views/NotFound404.vue'

import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/update',
    name: 'updateprofile',
    component: UpdateProfileView
  },
  {
    path: '/password/update',
    name: 'updatepassword',
    component: UpdatePasswordView
  },
  // 내 식물
  {
    path: '/myplant/:username',
    name: 'myplant',
    component: MyplantView,
    props: true
  },
  {
    path: '/myplant/new',
    name: 'myplantNew',
    component: MyplantNewView
  },
  {
    path: '/myplant/:username/:plantPk',
    name: 'myplantDetail',
    component: MyplantDetailView,
    props: true
  },
  {
    path: '/myplant/:plantPk/edit',
    name: 'myplantEdit',
    component: MyplantEditView,
    props: true
  },
  // 잎팔이
  {
    path: '/leaf82',
    name: 'leaf82',
    component: Leaf82View
  },
  {
    path: '/leaf82/new',
    name: 'leaf82New',
    component: Leaf82NewView
  },
  {
    path: '/leaf82/:username/:posting_addr',
    name: 'leaf82Detail',
    component: Leaf82DetailView,
    props: true
  },
  {
    path: '/leaf82/edit/:username/:posting_addr',
    name: 'leaf82Edit',
    component: Leaf82EditView,
    props: true
  },
  {
    path: '/messenger',
    name: 'messenger',
    component: MessengerView
  },
  //404
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: "/:catchAll(.*)",
    name: 'catch-all',
    redirect: '/404'
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup', 'home', 'leaf82', 'NotFound404', 'leaf82Detail']
  
  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인 필요합니다. 로그인 페이지로 이동합니다.')
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
