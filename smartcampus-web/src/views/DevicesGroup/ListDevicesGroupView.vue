<script setup>
const columns = [
  { header: 'ID', field: 'id' },
  { header: 'Name', field: 'name' },
  { header: 'Description', field: 'description' },
];
</script>

<template>
  <div class="list-device-groups">
    <DataTable>
      <template #header>
        <div class="table-header">
          <Button icon="pi pi-plus" label="Create Device Group" />
        </div>
      </template>
      <Column v-for="col in columns" :field="col.field" :header="col.header" />
      <Column header="Actions"></Column>
      <template #empty>
        <p class="empty-text">No rooms registered.</p>
      </template>
    </DataTable>
  </div>
</template>

<style scoped lang="scss">
.list-device-groups {
  .table-header {
    display: flex;
    justify-content: flex-end;
  }

  .empty-text {
    margin: 0;
    color: #888;
    font-style: italic;
  }
}
</style>
