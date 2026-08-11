<template>
  <main id="page-content" class="page-content">
    <template v-if="loadingPage">
      <p>Loading...</p>
    </template>
    <template v-else>
      <RouterView />
    </template>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { RouterView } from "vue-router";

let loadingPage = ref(true);

onMounted(() => {
  loadingPage.value = false;
});
</script>

<style scoped lang="scss">
#page-content {
  padding: 2rem;
  background-color: #f3f3f5;
}
</style>
