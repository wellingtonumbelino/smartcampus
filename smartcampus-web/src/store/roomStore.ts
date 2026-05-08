import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { getAllRooms } from "../services/roomService";
import type { Room } from "../types/Room";

export const useRoomStore = defineStore("rooms", () => {
  const rooms = ref<Room[]>([]);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const totalRooms = computed(() => rooms.value.length);

  async function fetchRooms() {
    loading.value = true;
    error.value = null;

    try {
      const data = await getAllRooms();
      rooms.value = data.data;
    } catch (err) {
      error.value = err instanceof Error ? err.message : String(err);
    } finally {
      loading.value = false;
    }
  }

  return { rooms, loading, totalRooms, error, fetchRooms };
});
