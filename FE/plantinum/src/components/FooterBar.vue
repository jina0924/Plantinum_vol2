<template>
  <div :class="footerBar">
    <hr>
    <div class="d-flex justify-content-between">
      <span :class="firstLine">Copyright © 2022 PLANTinum. 모든 권리 보유.</span>
      <span :class="firstLine">대한민국</span>
    </div>
    <div>
      <span :class="secondLine">주소 : 서울특별시 강남구 역삼동 테헤란로 212 | 대표자 : 임진경 | 대표번호 : 010-3440-8727</span>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'FooterBar',

  data() {
    return {
      footerBar: 'footer-bar PC',
      firstLine: 'first-line PC',
      secondLine: 'second-line PC'
    }
  },

  computed: {
    ...mapGetters(['device'])
  },

  methods: {
    changeDevice() {
      if (this.device === 'PC') {
        this.footerBar = 'footer-bar PC'
        this.firstLine = 'first-line PC'
        this.secondLine = 'second-line PC'
      } else if (this.device === 'Tablet') {
        this.footerBar = 'footer-bar tablet'
        this.firstLine = 'first-line tablet'
        this.secondLine = 'second-line tablet'
      } else {
        this.footerBar = 'footer-bar mobile'
        this.firstLine = 'first-line mobile'
        this.secondLine = 'second-line mobile'
      }
    },
  },

  created() {
    this.changeDevice()
  },
  
  watch: {
    device() {
      this.changeDevice()
    }
  }
}
</script>

<style scoped>
hr {
  margin-top: 0;
}

.footer-bar.PC {
  font-family: 'SUIT', sans-serif;
  padding-left: 3rem;
  padding-right: 3rem;
  padding-bottom: 1rem;
}

.footer-bar.tablet {
  font-family: 'SUIT', sans-serif;
  padding-left: 3rem;
  padding-right: 3rem;
  padding-bottom: 1rem;
}

.footer-bar.mobile {
  font-family: 'SUIT', sans-serif;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  padding-bottom: 0.8rem;
}

.first-line.PC {
  font-size: 0.75rem;
  color: rgb(77, 77, 77);
}

.first-line.tablet {
  font-size: 0.6rem;
  color: rgb(77, 77, 77);
}

.first-line.mobile {
  font-size: 0.5rem;
  color: rgb(77, 77, 77);
}

.second-line.PC {
  font-size: 0.65rem;
  color: gray;
}

.second-line.tablet {
  font-size: 0.5rem;
  color: gray;
}

.second-line.mobile {
  font-size: 0.4rem;
  color: gray;
}
</style>