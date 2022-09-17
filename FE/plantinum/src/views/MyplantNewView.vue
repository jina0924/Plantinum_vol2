<template>
  <div class="new-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="create" class="mt-3"></myplant-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyplantForm from '@/components/MyplantForm.vue'

export default {
  name: 'MyplantNewView',
  components: { NavBar, MyplantForm },
  data() {
    return {
      myplant: {
        nickname: '',
        photo: '',
        plantname: '',
        tmp: '',
      }
    }
  }
}
</script>

<style scoped>
.new-myplant{
  background-color: #F8F5EE;
  min-height: 95vh;
}
</style>