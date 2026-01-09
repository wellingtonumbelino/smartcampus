<script setup>
import { computed, onBeforeMount, onBeforeUnmount, onMounted, ref } from 'vue';
import { RouterView, useRoute } from 'vue-router';

const route = useRoute();
const title = computed(() => route.meta.pageTitle || 'Default Title');
let loadingPage = ref(true);

onMounted(() => {
  loadingPage.value = false;
});
</script>

<template>
  <main id="page-content" class="page-content">
    <template v-if="loadingPage">
      <p>Loading...</p>
    </template>
    <template v-else>
      <HeaderTitle :title="title" />
      <RouterView />
    </template>
  </main>
</template>

<style scoped lang="scss">
#page-content {
  border: 0.0625rem solid #e2e8f0;
  border-radius: 0.375rem;
  padding: 1rem;
}
</style>
