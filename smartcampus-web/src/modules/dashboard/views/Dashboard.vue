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
        planner="POPF-TIF"
        :executionTime="plannerStatusResult.executionTime"
        :loading="loading"
        :planSize="plannerStatusResult.actionsCount"
        :statesAnalyzed="plannerStatusResult.statesEvaluated"
        @generate-plan="runPlannerService"
      />

      <div class="dashboard-plan-actions-schedule">
        <PlanActionsTimeline :actions="planActions" />
        <ScheduledActions :schedule-actions="scheduleActions" />
      </div>
    </template>

    <template v-else-if="loading">
      <LoadingPlan />
    </template>

    <template v-else>
      <NoPlan @generate-plan="runPlannerService" />
    </template>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import {
  getPlannerByJobId,
  runPlanner,
} from "../../../services/plannerService";
import { useRoomStore } from "../../rooms/store/room.store";
import { getSchedulerActions } from "../../../services/schedulerService";
import type {
  PlannerResultJobIdModel,
  PlannerStatus,
} from "../../../types/Planner";
import type { SchedulerStatus } from "../../../types/Scheduler";
import mockDevices from "../../../_mock/devices.json";
import MetricCard from "../components/MetricCard.vue";
import GeneratedPlan from "../components/GeneratedPlan.vue";
import PlanActionsTimeline from "../components/PlanActionsTimeline.vue";
import ScheduledActions from "../components/ScheduledActions.vue";
import NoPlan from "../components/NoPlan.vue";
import LoadingPlan from "../components/LoadingPlan.vue";

const roomStore = useRoomStore();
const plannerStatusResult = ref<PlannerStatus | null>(null);
const loading = ref(false);
const scheduleLoading = ref(false);
const scheduleActions = ref<SchedulerStatus[]>([]);
const planActions = ref<PlannerResultJobIdModel[]>([]);
const statusTag = ref({ severity: "info", value: "Unavailable" });

const totalDevices = mockDevices.devices.length;

onMounted(async () => {
  if (roomStore.rooms.length === 0) {
    await roomStore.fetchRooms();
  }
});

async function defineStatusTag() {
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
    await getPlanActions(data.jobId);
    await viewSchedule();
  } else if (error) {
    plannerStatusResult.value = {
      executionTime: "N/A",
      jobId: "N/A",
      message: `Error: ${(error as Error).message}`,
      status: "Error",
      actionsCount: 0,
      statesEvaluated: 0,
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

async function getPlanActions(jobId: string) {
  const { data, error } = await getPlannerByJobId(jobId);

  if (data) {
    planActions.value = data;
  } else if (error) {
    console.error("Error fetching schedule actions:", error);
  }
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
