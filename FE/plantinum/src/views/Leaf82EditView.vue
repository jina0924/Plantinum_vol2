<template>
  <div class="leaf82Edit">
    <nav-bar></nav-bar>
    <leaf-82-edit></leaf-82-edit>
  </div>
</template>

<script>
import Leaf82Edit from '@/components/Leaf82Edit.vue'
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'Leaf82EditView',

  components: {
    Leaf82Edit,
    NavBar
  },

  data() {
    return {
      info: {
        username: this.$route.params.username,
        posting_addr: this.$route.params.posting_addr
      },
    }
  },

  methods: {
    ...mapActions(['fetchLeaf82Detail'])
  },
  
  created() {
    this.fetchLeaf82Detail(this.info)
  },
}
</script>

<style scoped>

</style>