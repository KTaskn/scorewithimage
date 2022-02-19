<template>
  <v-app>
    <v-main>
      <s-scroller :items="items" />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import SScroller from './components/SScroller.vue';

export default Vue.extend({
  name: 'App',
  components: {
    SScroller
  },
  mounted: async function() {
    const { data } = await axios.get('./items.json');
    this.items = data;
  },
  data: () => ({
    items: []
  })
});
</script>
