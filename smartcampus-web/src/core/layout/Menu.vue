<template>
  <Menubar id="main-menu">
    <template #start>
      <span class="system-name"> Automated Planning Management System </span>
    </template>
    <template #end>
      <div class="tiered-menu-avatar">
        <Button
          aria-controls="overlay_menu"
          aria-haspopup="true"
          variant="text"
          @click="toggleTieredMenu"
        >
          <Avatar image="https://i.pravatar.cc/150" shape="circle" />
          <i class="pi pi-chevron-down" />
        </Button>

        <TieredMenu id="overlay_menu" ref="tieredMenu" popup :model="items" />
      </div>
    </template>
  </Menubar>
</template>

<script setup lang="ts">
import type { TieredMenu } from "primevue";
import { ref } from "vue";

const tieredMenu = ref<InstanceType<typeof TieredMenu> | null>(null);

const toggleTieredMenu = (event: MouseEvent) => {
  tieredMenu.value?.toggle(event);
};

const items = ref([
  {
    label: "Profile",
    icon: "pi pi-user",
    command: () => {
      console.log("Profile clicked");
    },
  },
  {
    label: "Settings",
    icon: "pi pi-cog",
    command: () => {
      console.log("Settings clicked");
    },
  },
  {
    separator: true,
  },
  {
    label: "Logout",
    icon: "pi pi-sign-out",
    command: () => {
      console.log("Logout clicked");
    },
  },
]);
</script>

<style scoped lang="scss">
#main-menu {
  border-radius: 0;
  border-left: 0;

  .p-menubar-start {
    .system-name {
      font-size: 1.125rem;
      font-weight: 500;
    }
  }
}
</style>
