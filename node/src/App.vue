<template>
  <v-app>
    <v-main>
      <s-scroller :items="items" />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import SScroller from "./components/SScroller.vue";

export default Vue.extend({
  name: "App",
  components: {
    SScroller,
  },
  mounted: function () {
    const itemsDom = document.getElementById('items-data');
    if (itemsDom) {
      console.log(itemsDom.innerText)
      const items = JSON.parse(itemsDom.innerText);
      this.items = items;
      itemsDom.style.display = 'none';
    }
  },
  data: () => ({
    field: "",
    items: [],
  }),
});
</script>
