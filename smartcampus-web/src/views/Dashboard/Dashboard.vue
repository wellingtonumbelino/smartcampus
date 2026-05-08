<script setup lang="ts">
import { onMounted, ref } from "vue";
import mockDevices from "../../_mock/devices.json";
import { useRoomStore } from "../../store/roomStore";
import { runPlanner } from "../../services/plannerService";
import type { PlannerStatus } from "../../types/Planner";
import { getSchedulerActions } from "../../services/schedulerService";
import type { SchedulerStatus } from "../../types/Scheduler";

const roomStore = useRoomStore();
const plannerStatusResult = ref<PlannerStatus | null>(null);
const loading = ref(false);
const scheduleLoading = ref(false);
const scheduleActions = ref<SchedulerStatus[]>([]);

onMounted(async () => {
  if (roomStore.rooms.length === 0) {
    await roomStore.fetchRooms();
  }
});

const totalDevices = mockDevices.devices.length;

async function runPlannerService() {
  loading.value = true;
  const { data, error } = await runPlanner();
  if (data) {
    plannerStatusResult.value = data;
  } else if (error) {
    plannerStatusResult.value = {
      executionTime: "N/A",
      jobId: "N/A",
      message: `Error: ${(error as Error).message}`,
      status: "Error",
      actionsCount: 0,
    };
  }
  loading.value = false;
}

async function viewSchedule() {
  scheduleLoading.value = true;
  const { data, error } = await getSchedulerActions();
  if (data) {
    scheduleActions.value = data;
  } else if (error) {
    console.error("Error fetching schedule actions:", error);
  }
  scheduleLoading.value = false;
}
</script>

<template>
  <div class="dashboard">
    <section class="dashboard-section">
      <h2>Resumo</h2>
      <div class="cards">
        <div class="card">
          <h3>Total Devices</h3>
          <p>{{ totalDevices }}</p>
        </div>
        <div class="card">
          <h3>Total Rooms</h3>
          <p>{{ roomStore.totalRooms }}</p>
        </div>
      </div>
    </section>
    <section class="dashboard-section">
      <h2>Actions</h2>
      <div class="dashboard-actions">
        <Button
          label="Run Planner"
          icon="pi pi-play"
          :loading="loading"
          @click="runPlannerService"
        />
        <Button
          label="View Schedule"
          icon="pi pi-eye"
          :loading="scheduleLoading"
          @click="viewSchedule"
        />
      </div>
    </section>
    <section class="dashboard-status">
      <h2>Status</h2>
      <div class="dashboard-status-info">
        <div v-if="plannerStatusResult">
          <p>Execution Time: {{ plannerStatusResult.executionTime }}</p>
          <p>Job ID: {{ plannerStatusResult.jobId }}</p>
          <pMessage
            :severity="
              plannerStatusResult.status === 'Success' ? 'success' : 'error'
            "
            :summary="plannerStatusResult.message"
          />
          <p>Actions Count: {{ plannerStatusResult.actionsCount }}</p>
        </div>
        <div v-else>
          <p>No planner status available.</p>
        </div>
      </div>
    </section>
    <section class="dashboard-schedule">
      <h2>Scheduled Actions</h2>
      <ul v-if="scheduleActions.length > 0">
        <li v-for="(action, index) in scheduleActions" :key="index">
          {{ action.jobId }}
        </li>
      </ul>
      <p v-else>No scheduled actions available.</p>
    </section>
  </div>
</template>

<style scoped lang="scss">
.dashboard {
  .dashboard-section {
    h3 {
      margin: 0.5rem;
    }
  }

  .cards {
    display: flex;
    gap: 1rem;
  }

  .card {
    flex: 1;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    padding: 0.5rem;
    text-align: center;
  }

  .dashboard-actions {
    display: flex;
    gap: 1rem;
  }
}
</style>
