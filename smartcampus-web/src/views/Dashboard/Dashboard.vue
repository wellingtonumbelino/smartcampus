<template>
  <div class="dashboard">
    <div class="dashboard-info-actions">
      <Card class="card-number-info">
        <template #title>TOTAL IOT DEVICES</template>
        <template #content>
          <p>{{ totalDevices }}</p>
        </template>
      </Card>

      <Card class="card-number-info">
        <template #title>PHYSICAL ROOMS</template>
        <template #content>
          <p>{{ roomStore.totalRooms }}</p>
        </template>
      </Card>

      <Card class="card-detail-info">
        <template #title>ACTIONS</template>
        <template #content>
          <Divider />
          <div class="actions-button">
            <Button
              label="Run Planner"
              icon="pi pi-play-circle"
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
        </template>
      </Card>

      <Card class="card-detail-info">
        <template #title>STATUS</template>
        <template #content>
          <div v-if="plannerStatusResult" class="status-info-container">
            <span class="status-info">
              <label>Execution ID</label>
              <p>{{ plannerStatusResult?.jobId }}</p>
            </span>
            <span class="status-info">
              <label>Execution Time</label>
              <p>{{ plannerStatusResult?.executionTime }}</p>
            </span>
            <span class="status-info">
              <label>N°. Actions Generated</label>
              <p>{{ plannerStatusResult?.actionsCount }}</p>
            </span>
            <Divider />
            <div class="status-card-footer">
              <i class="pi pi-check-circle" />
              <p>Execution completed without errors.</p>
            </div>
          </div>
          <p v-else>No planner status available.</p>
        </template>
      </Card>
    </div>

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

<style scoped lang="scss">
.dashboard {
  .dashboard-info-actions {
    display: flex;
    gap: 2rem;

    .card-number-info {
      width: 25%;
    }
    .card-detail-info {
      width: 50%;

      .actions-button {
        display: flex;
        gap: 1rem;
        width: 100%;

        .p-button {
          flex: 1;
          height: 2.5rem;
        }
      }

      .status-info-container {
        display: flex;
        flex-direction: column;
        gap: 1rem;

        p {
          margin: 0;
        }

        .status-info {
          display: flex;
          align-items: center;
          justify-content: space-between;
        }

        .status-card-footer {
          display: flex;
          gap: 1rem;
          align-items: center;
        }
      }
    }
  }

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
