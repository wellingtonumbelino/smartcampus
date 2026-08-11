<template>
  <div id="side-menu">
    <Menu :model="sideMenuItems">
      <template #start>
        <div class="system-info-container">
          <Avatar label="A" />
          <div class="system-info">
            <span class="system-name-acronym">APMS</span>
            <span class="system-version">v{{ version }}</span>
          </div>
        </div>
      </template>

      <template #item="{ item, props }">
        <router-link
          v-if="item.route"
          v-slot="{ href, navigate }"
          :to="item.route"
          custom
        >
          <a v-ripple :href="href" v-bind="props.action" @click="navigate">
            <span :class="item.icon" />
            <span>{{ item.label }}</span>
          </a>
        </router-link>
      </template>
    </Menu>
  </div>
</template>

<script setup lang="ts">
import { useNavigation } from "./composables/useNavigation";
import { version } from "../../../package.json";

const { sideMenuItems } = useNavigation();
</script>

<style scoped lang="scss">
#side-menu {
  height: 100%;

  .p-menu-start {
    .system-info-container {
      display: flex;
      gap: 0.625rem;
      padding: 0.75rem 1rem;
      align-items: center;

      .system-info {
        display: flex;
        flex-direction: column;

        .system-name-acronym {
          font-size: 0.875rem;
          font-weight: 500;
          letter-spacing: 0.025rem;
        }

        .system-version {
          font-size: 0.75rem;
          font-weight: 300;
        }
      }
    }
  }

  &.p-component {
    border-radius: 0;
  }
}
</style>
