<script setup>
import { onMounted, ref } from 'vue';
import CreateRoomDialog from './CreateRoomDialog.vue';
import { deleteRoomById, getAllRooms } from '@/services/roomService';

const columns = [
  { header: 'ID', field: 'id' },
  { header: 'Name', field: 'name' },
  { header: 'Description', field: 'description' },
];

const createRoomDialog = ref(null);
const tableLoading = ref(false);
const rooms = ref([]);

onMounted(async () => {
  await loadingAllRooms();
});

function openCreateRoomDialog() {
  if (createRoomDialog.value) {
    createRoomDialog.value.toggleDialog(rooms.value[rooms.value.length - 1] || null);
  }
}

async function loadingAllRooms() {
  tableLoading.value = true;

  const { data, error } = await getAllRooms();

  if (error) {
    console.error('Error loading rooms:', error);
  } else {
    rooms.value = data;
  }

  tableLoading.value = false;
}

async function removeRoomById(id) {
  await deleteRoomById(id);
  loadingAllRooms();
}
</script>

<template>
  <div class="list-rooms">
    <CreateRoomDialog ref="createRoomDialog" @roomCreated="loadingAllRooms" />
    <DataTable stripedRows :loading="tableLoading" :value="rooms">
      <template #header>
        <div class="table-header">
          <Button icon="pi pi-plus" label="Create Room" @click="openCreateRoomDialog" />
        </div>
      </template>
      <Column v-for="col in columns" :field="col.field" :header="col.header" />
      <Column header="Actions" style="width: 10%">
        <template #body="slotProps">
          <div class="action-buttons">
            <Button icon="pi pi-pencil" severity="info" />
            <Button
              icon="pi pi-trash"
              severity="danger"
              @click="removeRoomById(slotProps.data.id)"
            />
          </div>
        </template>
      </Column>
      <template #empty>
        <p class="empty-text">No rooms registered.</p>
      </template>
    </DataTable>
  </div>
</template>

<style scoped lang="scss">
.list-rooms {
  .table-header {
    display: flex;
    justify-content: flex-end;
  }

  .action-buttons {
    display: flex;
    gap: 0.5rem;
  }

  .empty-text {
    margin: 0;
    color: #888;
    font-style: italic;
  }
}
</style>
