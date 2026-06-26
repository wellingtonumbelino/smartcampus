<template>
  <div class="list-devices">
    <HeaderTitle title="Devices" />

    <div class="card-table">
      <DataTable
        paginator
        stripedRows
        v-model:filters="filters"
        :globalFilterFields="['name']"
        :loading="tableLoading"
        :rows="20"
        :value="mockDevices.devices"
      >
        <template #header>
          <div class="table-header">
            <div>
              <IconField>
                <InputIcon>
                  <i class="pi pi-search" />
                </InputIcon>
                <InputText
                  v-model="filters['global'].value"
                  placeholder="Search devices..."
                />
              </IconField>
            </div>

            <Button icon="pi pi-plus" label="Add Device" severity="help" />
          </div>
        </template>
        <Column
          v-for="col in columns"
          :field="col.field"
          :header="col.header"
        />
        <Column header="Actions"></Column>
        <template #empty>
          <p class="empty-text">No devices registered.</p>
        </template>
      </DataTable>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { FilterMatchMode } from "@primevue/core/api";
import mockDevices from "../../../_mock/devices.json";
import HeaderTitle from "../../../shared/components/HeaderTitle.vue";

interface Column {
  header: string;
  field: string;
}

// interface Device {
//   id: string;
//   name: string;
//   description: string;
// }

const columns: Column[] = [
  { header: "Name", field: "name" },
  { header: "Identifier", field: "id" },
  { header: "Description", field: "description" },
];
const tableLoading = ref(false);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

// const allDevices = ref<Device[]>([]);

// onMounted(() => {
//   fetchAllDevices();
// });

// async function fetchAllDevices() {
//   try {
//     tableLoading.value = true;
//     const { data } = await getAllDevices();
//     allDevices.value = data;
//   } catch (error) {
//     console.error("Error fetching devices:", error);
//   } finally {
//     tableLoading.value = false;
//   }
// }
</script>

<style scoped lang="scss">
.list-devices {
  .card-table {
    .p-datatable {
      .p-datatable-header {
        .table-header {
          display: flex;
          justify-content: space-between;
        }
      }

      .empty-text {
        margin: 0;
        color: #888;
        font-style: italic;
      }
    }
  }
}
</style>
