<script setup lang="ts">
import { onMounted, ref } from "vue";
import { getAllDevices } from "../../services/deviceService";

interface Column {
  header: string;
  field: string;
}

const columns: Column[] = [
  { header: "ID", field: "id" },
  { header: "Name", field: "name" },
  { header: "Description", field: "description" },
];
const tableLoading = ref(false);

const allDevices = ref([]);

onMounted(() => {
  fetchAllDevices();
});

async function fetchAllDevices() {
  tableLoading.value = true;

  const { data, error } = await getAllDevices();

  if (error) {
    console.error("Error fetching devices:", error);
  } else {
    allDevices.value = data;
  }

  tableLoading.value = false;
}
</script>

<template>
  <div class="list-devices">
    <DataTable stripedRows>
      <template #header>
        <div class="table-header">
          <Button icon="pi pi-plus" label="Create Device" />
        </div>
      </template>
      <Column v-for="col in columns" :field="col.field" :header="col.header" />
      <Column header="Actions"></Column>
      <template #empty>
        <p class="empty-text">No devices registered.</p>
      </template>
    </DataTable>
  </div>
</template>

<style scoped lang="scss">
.list-devices {
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
