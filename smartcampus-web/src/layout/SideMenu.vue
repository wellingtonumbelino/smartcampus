<script setup>
import Menu from 'primevue/menu';
import { RouterLink } from 'vue-router';
import items from '@/helpers/menuItems';
</script>

<template>
  <div id="side-menu">
    <Menu :model="items">
      <template #item="{ item, props }">
        <router-link v-slot="{ href, navigate }" :to="item.route" custom>
          <a :href="href" v-bind="props.action" @click="navigate">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
          </a>
        </router-link>
      </template>
    </Menu>
  </div>
</template>
