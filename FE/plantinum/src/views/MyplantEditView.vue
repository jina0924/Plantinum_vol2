<template>
  <div class="edit-myplant">
    <nav-bar></nav-bar>
    <myplant-form :myplant="myplant" action="update" class="mt-3"></myplant-form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MyplantForm from '@/components/MyplantForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MyplantEdit',
  components: { NavBar, MyplantForm },
  computed: {
    ...mapGetters(['myplant'])
  },
  methods: {
    ...mapActions(['fetchMyplant'])
  },
  created() {
    this.fetchMyplant(this.$route.params.plantPk)
  }
}
</script>

<style scoped>
.edit-myplant{  
  background-color: #F8F5EE;
  min-height: 95vh;
}
</style>