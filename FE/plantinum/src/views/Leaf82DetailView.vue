<template>
  <div class="leaf82-detail">
    <nav-bar></nav-bar>
    <div class="leaf82-detail-view">
      <leaf-82-detail></leaf-82-detail>
    </div>
  </div>
</template>

<script>
import Leaf82Detail from '@/components/Leaf82Detail.vue'
import NavBar from '@/components/NavBar.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Leaf82DetailView',

  components: {
    Leaf82Detail,
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
    ...mapActions(['fetchLeaf82Detail']),
  },

  computed: {
    ...mapGetters(['leaf82Detail'])
  },
  
  created() {
    this.fetchLeaf82Detail(this.info)
  },
}
</script>

<style scoped>
.leaf82-detail {
  background-color: #F8F5EE;
}
</style>