<script setup>
import PageContent from './layout/PageContent.vue';
import SideMenu from './layout/SideMenu.vue';
</script>

<template>
  <div class="main-layout">
    <SideMenu />
    <PageContent />
  </div>
</template>

<style scoped lang="scss">
.main-layout {
  display: grid;
  grid-template-columns: 16rem 1fr;
  gap: 1rem;
  grid-template-areas: 'side-menu page-content';

  #side-menu {
    grid-area: side-menu;
  }

  #page-content {
    grid-area: page-content;
  }
}
</style>
