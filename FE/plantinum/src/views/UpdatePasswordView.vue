<template>
  <div class="profile">
    <div class="row mx-0">
      <div class="col-md-3"></div>
      <update-password-detail class="col-md-6 mb-5 pb-5 pt-5"></update-password-detail>
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>
import UpdatePasswordDetail from '@/components/UpdatePasswordDetail.vue'

export default {
  name: 'UpdatePasswordView',
  
  components : {
    UpdatePasswordDetail
  }
}
</script>

<style scoped>
.profile {
  background-image: url('@/assets/ProfileView/background_img.jpg');
  background-size: cover;
  height: 1000px;
}
</style>