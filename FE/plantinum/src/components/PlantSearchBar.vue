<template>
  <div class="row g-3 justify-content-center">
    <div class="col-10 d-flex justify-content-between">
      <input v-model="keyword" type="text" class="form-control" placeholder="식물 이름을 검색하세요">
      <button type="submit" class="btn mx-3">찾아보기</button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'PlantSearchBar',
  data() {
    return {
      keyword: '',
    }
  },
  computed: {
    ...mapGetters([''])
  },
  methods: {
    ...mapActions([''])
  }
}
</script>

<style>

</style>