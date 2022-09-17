<template>
  <div>
    <nav-bar></nav-bar>
    <leaf-82-search-list></leaf-82-search-list>
  </div>
</template>

<script>
import Leaf82SearchList from'@/components/Leaf82SearchList.vue'
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'Leaf82View',

  components: {
    NavBar,
    Leaf82SearchList
  },

  methods: {
    ...mapActions(['fetchSido']),
  },

  computed: {
  },
  
  created() {
    this.fetchSido()
  },
}
</script>

<style scoped>
div {
  background-color: #F8F5EE;
}
</style>