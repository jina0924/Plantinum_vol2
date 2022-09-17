<template>
  <div class="leaf82-view">
    <nav-bar></nav-bar>
    <div class="leaf82-new">
      <leaf-82-new-form></leaf-82-new-form>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import Leaf82NewForm from '@/components/Leaf82NewForm.vue'

export default {
  name: 'Leaf82NewView',
  
  components: {
    NavBar,
    Leaf82NewForm,
  }
}
</script>

<style scoped>
.leaf82-view {
  background-color: #F8F5EE;
}
</style>