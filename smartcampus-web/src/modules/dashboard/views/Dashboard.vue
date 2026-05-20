<template>
  <div class="dashboard">
    <template v-if="!loading && plannerStatusResult">
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

      <GeneratedPlan
        executionTime="1.34s"
        planner="POPF-TIF"
        planSize="12 actions"
        statesAnalyzed="18"
        :loading="loading"
        @generate-plan="runPlannerService"
      />

      <div class="dashboard-plan-actions-schedule">
        <PlanActionsTimeline :actions="planActions" />
        <ScheduledActions :schedule-actions="schedulerActions" />
      </div>
    </template>

    <template v-else>
      <NoPlan @generate-plan="runPlannerService" />
    </template>

    <!-- <section class="dashboard-schedule">
      <h2>Scheduled Actions</h2>
      <ul v-if="scheduleActions.length > 0">
        <li v-for="(action, index) in scheduleActions" :key="index">
          {{ action.jobId }}
        </li>
      </ul>
      <p v-else>No scheduled actions available.</p>
    </section> -->
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
import MetricCard from "../components/MetricCard.vue";
import GeneratedPlan from "../components/GeneratedPlan.vue";
import PlanActionsTimeline from "../components/PlanActionsTimeline.vue";
import ScheduledActions from "../components/ScheduledActions.vue";
import NoPlan from "../components/NoPlan.vue";

const roomStore = useRoomStore();
const plannerStatusResult = ref<PlannerStatus | null>(null);
const loading = ref(false);
const scheduleLoading = ref(false);
const scheduleActions = ref<SchedulerStatus[]>([]);
const statusTag = ref({ severity: "info", value: "Unavailable" });

const totalDevices = mockDevices.devices.length;

const planActions = ref([
  {
    executionTime: "1.000",
    actionName: "Turn on Light in Room 101",
    duration: "2.000",
  },
  {
    executionTime: "1.001",
    actionName: "Adjust Thermostat in Room 102",
    duration: "1.000",
  },
  {
    executionTime: "2.000",
    actionName: "Lock Door in Room 103",
    duration: "2.000",
  },
]);

const schedulerActions = ref([
  {
    actionId: "turn_on_air_conditioner:bl1_sl1_ac1",
    scheduled: "2024-10-01T10:00:00Z",
    command: "ON",
  },
  {
    actionId: "adjust_thermostat:bl1_sl1_t1",
    scheduled: "2024-10-01T11:00:00Z",
    command: "Set Temperature to 22°C",
  },
  {
    actionId: "lock_door:bl1_sl1_d1",
    scheduled: "2024-10-01T12:00:00Z",
    command: "LOCK",
  },
]);

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
    margin-bottom: 0.875rem;
  }

  .dashboard-plan-actions-schedule {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }
}
</style>
