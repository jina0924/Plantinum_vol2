<template>
  <div class="profile">
    <nav-bar></nav-bar>
    <div class="row mx-0">
      <div class="col-md-1 px-0 mx-0"></div>
      <profile-detail class="col-md-10 mb-5 pb-5 px-0 mx-0"></profile-detail>
      <div class="col-md-1 px-0 mx-0"></div>
    </div>
  </div>
</template>

<script>
import ProfileDetail from '@/components/ProfileDetail.vue'
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'ProfileView',

  components: {
    ProfileDetail,
    NavBar
  },

  methods: {
    ...mapActions(['fetchProfile'])
  },
  
  created() {
    this.fetchProfile()
  }
}
</script>

<style scoped>
.profile {
  background-image: url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
  height: 1200px;
}
</style>
