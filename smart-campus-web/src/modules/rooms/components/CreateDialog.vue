<script setup lang="ts">
import { ref } from "vue";
import { createNewRoom } from "../../services/roomService";

const emit = defineEmits(["roomCreated"]);

const showModal = ref(false);
const roomName = ref("");
const roomDescription = ref("");
const roomId = ref("");

function toggleDialog() {
  if (showModal.value) showModal.value = false;
  else showModal.value = true;
}

async function createRoom() {
  await createNewRoom(roomId.value, roomName.value, roomDescription.value);
  emit("roomCreated");
  clearForm();
  toggleDialog();
}

function clearForm() {
  roomName.value = "";
  roomDescription.value = "";
  roomId.value = "";
}

defineExpose({ toggleDialog });
</script>

<template>
  <div class="create-room-dialog">
    <Dialog
      v-model:visible="showModal"
      header="New Room"
      modal
      style="min-width: 20rem"
    >
      <div class="create-room-dialog-content">
        <div class="field">
          <label for="room-id-input">ID</label>
          <InputText
            id="room-id-input"
            placeholder="Insert Room ID"
            type="text"
            v-model="roomId"
          />
        </div>
        <div class="field">
          <label for="room-name-input">Name</label>
          <InputText
            id="room-name-input"
            placeholder="Insert Room Name"
            type="text"
            v-model="roomName"
          />
        </div>
        <div class="field">
          <label for="room-description-input">Description</label>
          <InputText
            id="room-description-input"
            placeholder="Insert Room Description"
            type="text"
            v-model="roomDescription"
          />
        </div>
      </div>
      <template #footer>
        <Button
          label="Cancel"
          severity="secondary"
          @click="() => toggleDialog()"
        />
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
