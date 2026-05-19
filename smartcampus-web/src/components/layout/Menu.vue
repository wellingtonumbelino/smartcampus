<template>
  <Menubar id="main-menu">
    <template #start>
      <span class="system-name">
        Automated Planning Management System (APMS)
      </span>
    </template>
    <template #end>
      <div>
        <Avatar image="https://i.pravatar.cc/150" shape="circle" />
      </div>
    </template>
  </Menubar>
</template>

<style scoped lang="scss">
#main-menu {
  border-radius: 0;

  .p-menubar-start {
    .system-name {
      font-size: 1.25rem;
      font-weight: bold;
    }
  }
}
</style>
