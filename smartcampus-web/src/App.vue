<template>
  <div class="main-layout">
    <SideMenu />
    <Menu />
    <PageContent />
  </div>
</template>

<script setup lang="ts">
import PageContent from "./components/layout/PageContent.vue";
import SideMenu from "./components/layout/SideMenu.vue";
import Menu from "./components/layout/Menu.vue";
</script>

<style scoped lang="scss">
.main-layout {
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-rows: auto 1fr;
  grid-template-areas:
    "side-menu main-menu"
    "side-menu page-content";
  height: 100%;

  #side-menu {
    grid-area: side-menu;
  }

  #main-menu {
    grid-area: main-menu;
  }

  #page-content {
    grid-area: page-content;
    overflow-y: auto;
  }
}
</style>
