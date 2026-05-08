<script setup lang="ts">
import { RouterLink } from "vue-router";
import items from "../../helpers/menuItems";
</script>

<template>
  <Menu id="side-menu" :model="items">
    <template #item="{ item, props }">
      <router-link v-slot="{ href, navigate }" :to="item.route" custom>
        <a :href="href" v-bind="props.action" @click="navigate">
          <span :class="item.icon" />
          <span>{{ item.label }}</span>
        </a>
      </router-link>
    </template>
  </Menu>
</template>

<style scoped lang="scss">
div {
  &#side-menu {
    background-color: black;
  }
}
</style>
