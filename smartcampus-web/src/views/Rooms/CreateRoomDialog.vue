<script setup>
import { createNewRoom } from '@/services/roomService';
import { ref } from 'vue';

const emit = defineEmits(['roomCreated']);

const showModal = ref(false);
const roomName = ref('');
const roomDescription = ref('');
const roomId = ref(null);

function toggleDialog(lastRoom = null) {
  if (lastRoom) {
    roomId.value = '00'.concat(parseInt(lastRoom.id.slice(-1)) + 1);
  } else {
    roomId.value = '001';
  }

  if (showModal.value) showModal.value = false;
  else showModal.value = true;
}

async function createRoom() {
  await createNewRoom(roomId.value, roomName.value, roomDescription.value);
  emit('roomCreated');
  clearForm();
  toggleDialog();
}

function clearForm() {
  roomName.value = '';
  roomDescription.value = '';
  roomId.value = null;
}

defineExpose({ toggleDialog });
</script>

<template>
  <div class="create-room-dialog">
    <Dialog v-model:visible="showModal" header="Create a New Room" modal>
      <div class="create-room-dialog-content">
        <div class="field">
          <label for="room-name-input">Room Name</label>
          <InputText
            id="room-name-input"
            placeholder="Insert Room Name"
            type="text"
            v-model="roomName"
          />
        </div>
        <div class="field">
          <label for="room-description-input">Room Description</label>
          <InputText
            id="room-description-input"
            placeholder="Insert Room Description"
            type="text"
            v-model="roomDescription"
          />
        </div>
      </div>
      <template #footer>
        <Button label="Cancel" severity="secondary" @click="toggleDialog" />
        <Button label="Confirm" @click="createRoom" />
      </template>
    </Dialog>
  </div>
</template>

<style lang="scss">
.create-room-dialog {
  &-content {
    display: flex;
    flex-direction: column;
    gap: 1rem;

    .field {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;

      label {
        font-size: 0.875rem;
      }
    }
  }
}
</style>
