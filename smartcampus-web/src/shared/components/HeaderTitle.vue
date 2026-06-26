<script setup lang="ts">
defineProps({
  title: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <h1 class="header-template">{{ title }}</h1>
</template>

<style scoped lang="scss">
.header-template {
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.5rem;
  font-weight: 500;
}
</style>
