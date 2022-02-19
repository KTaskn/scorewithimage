<template>
  <div class="grid" v-bind:style="gridStyle">
    <h1 style="padding: 10px">{{ entity.score.toFixed(3) }}</h1>
    <img style="padding: 10px" :src="entity.image" />
  </div>
</template>

<script>
import { ImageWithScore } from '@/models/ImageWithScore';
export default {
    props: {
        entity: {
            type: ImageWithScore,
            required: true,
        },
    },
    methods: {
        hue: (hue) => {
            hue = hue * 120
            return `hsl(${hue}, 90%, 70%)`
        },
    },
    computed: {
        gridStyle: function() {
            return {
                backgroundColor: this.hue(this.entity.score),
            }
        },
    }
}
</script>

<style>
.grid {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
</style>