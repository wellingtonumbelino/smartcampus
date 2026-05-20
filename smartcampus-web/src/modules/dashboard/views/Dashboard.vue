<template>
  <div class="dashboard">
    <div class="dashboard-iot-info">
      <MetricCard
        icon="pi pi-microchip"
        iconColor="#185FA5"
        iconBg="#E6F1FB"
        label="Iot Devices"
        :value="totalDevices"
      />
      <MetricCard
        icon="pi pi-building"
        iconColor="#0F6E56"
        iconBg="#E1F5EE"
        label="Physical Rooms"
        :value="roomStore.totalRooms"
      />
    </div>

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
        <template #title>System Planner</template>

        <template #content>
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
        <template #title>
          <div class="card-header-title">
            <span>Last Plan Status</span>
            <Tag
              rounded
              :severity="statusTag.severity"
              :value="statusTag.value"
            />
          </div>
        </template>

        <template #content>
          <div class="card-content">
            <div
              v-if="!loading && plannerStatusResult"
              class="status-info-container"
            >
              <span class="status-info">
                <label>Execution ID</label>
                <p>{{ plannerStatusResult?.jobId }}</p>
              </span>
              <span class="status-info">
                <label>Timestamp</label>
                <p>10-27 14:32:01</p>
              </span>
              <span class="status-info">
                <label>Execution Time</label>
                <p>{{ plannerStatusResult?.executionTime }}</p>
              </span>
              <span class="status-info">
                <label>Plan Size</label>
                <p>{{ plannerStatusResult?.actionsCount }}</p>
              </span>
              <span class="status-info">
                <label>States Explored</label>
                <p>78</p>
              </span>
            </div>

            <div v-else-if="loading" class="status-info-container">
              <Skeleton width="100%" />
              <Skeleton width="100%" />
              <Skeleton width="100%" />
              <Skeleton width="100%" />
              <Skeleton width="100%" />
            </div>

            <p v-else>No planner status available.</p>
          </div>
        </template>
      </Card>
    </div>

    <section class="dashboard-schedule">
      <PlanTimeline />
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
import { runPlanner } from "../../../services/plannerService";
import { useRoomStore } from "../../rooms/store/room.store";
import { getSchedulerActions } from "../../../services/schedulerService";
import type { PlannerStatus } from "../../../types/Planner";
import type { SchedulerStatus } from "../../../types/Scheduler";
import mockDevices from "../../../_mock/devices.json";
import PlanTimeline from "../components/PlanTimeline.vue";
import MetricCard from "../components/MetricCard.vue";

const roomStore = useRoomStore();
const plannerStatusResult = ref<PlannerStatus | null>(null);
const loading = ref(false);
const scheduleLoading = ref(false);
const scheduleActions = ref<SchedulerStatus[]>([]);
const statusTag = ref({ severity: "info", value: "Unavailable" });

const totalDevices = mockDevices.devices.length;

onMounted(async () => {
  if (roomStore.rooms.length === 0) {
    await roomStore.fetchRooms();
  }
});

async function defineStatusTag() {
  console.log("chamou", plannerStatusResult.value);

  if (plannerStatusResult.value) {
    switch (plannerStatusResult.value.success) {
      case true:
        statusTag.value = { severity: "success", value: "Success" };
        break;
      case false:
        statusTag.value = { severity: "danger", value: "Error" };
        break;
      default:
        statusTag.value = { severity: "info", value: "Unavailable" };
    }
  }
}

async function runPlannerService() {
  loading.value = true;

  const { data, error } = await runPlanner();

  if (data) {
    plannerStatusResult.value = data;

    await defineStatusTag();
  } else if (error) {
    plannerStatusResult.value = {
      executionTime: "N/A",
      jobId: "N/A",
      message: `Error: ${(error as Error).message}`,
      status: "Error",
      actionsCount: 0,
      success: undefined,
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
  .dashboard-iot-info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
  }
  .dashboard-info-actions {
    display: flex;
    gap: 2rem;

    .card-number-info {
      width: 25%;
    }

    .card-detail-info {
      width: 50%;

      .p-card-body {
        .p-card-caption {
          .p-card-title {
            .card-header-title {
              display: flex !important;
              align-items: center;
              justify-content: space-between;
            }
          }
        }

        .p-card-content {
          .card-content {
            margin-top: 1rem;
          }
        }
      }

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

          &:not(:last-child) {
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 0.5rem;
          }
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
