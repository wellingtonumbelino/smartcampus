<script setup>
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
}
</style>
