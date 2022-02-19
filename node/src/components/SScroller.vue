<template>
  <v-virtual-scroll
    :bench="benched"
    :items="items"
    :item-height="item_height + 50"
    :height="item_height * num_row"
  >
    <template v-slot:default="{ item }">
      <s-grid :entity="item" />
    </template>
  </v-virtual-scroll>
</template>

<script>
import SGrid from './atoms/SGrid.vue';

const ITEM_HEIGHT = 200;
const NUM_ROW = 10;

export default {
    components: { SGrid },
    props: {
        items: {
            type: Array,
            required: true,
        },
    },
    data: () => ({
        benched: 0,
        item_height: ITEM_HEIGHT,
        num_row: NUM_ROW,
    }),
}
</script>

<style>
</style>