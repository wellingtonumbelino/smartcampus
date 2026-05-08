<script setup lang="ts">
import PageContent from "./components/layout/PageContent.vue";
import SideMenu from "./components/layout/SideMenu.vue";
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
  grid-template-columns: auto 1fr;
  grid-template-areas: "side-menu page-content";
  height: 100%;

  #side-menu {
    grid-area: side-menu;
  }

  #page-content {
    grid-area: page-content;
  }
}
</style>
