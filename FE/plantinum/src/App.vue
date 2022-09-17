<template>
  <div id="app" :style="[isProfile ? { backgroundColor: '#f7f8f8' } : { backgroundColor: '#F8F5EE' }]">
    <router-view></router-view>
    <footer-bar v-if="isFooterGroup"></footer-bar>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import FooterBar from '@/components/FooterBar.vue'

export default {
  name: 'App',

  components: { FooterBar },

  data() {
    return {
      viewWidth: window.innerWidth,
      profileGroup: ['profile', 'updateprofile', 'updatepassword',],
      noFooterGroup: ['login', 'NotFound404']
    }
  },

  methods: {
    ...mapActions(['fetchCurrentUser', 'fetchProfile', 'setDevice', 'getDevice']),

    handleResize() {
      this.viewWidth = window.innerWidth
    },    
  },
  
  computed: {
    isProfile() {
      return this.profileGroup.includes(this.$route.name)
    },
    isFooterGroup() {
      return !this.noFooterGroup.includes(this.$route.name)
    },
  },
  
  mounted() {
    window.addEventListener('resize', this.handleResize);
	},

  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize);
  },

  created () {
    this.fetchCurrentUser()
    this.getDevice()
  },
  
  watch: {
    viewWidth() {
      this.setDevice(this.viewWidth)
    }
  }
}
</script>

<style>
  #app {
    font-family: 'SUIT';
    min-height: 100vh;
  }

  body {
    background-color: #F8F5EE;
  }
</style>
