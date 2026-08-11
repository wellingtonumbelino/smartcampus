<template>
  <div class="plan-actions-timeline-container">
    <header class="plan-actions-timeline-header">
      <span class="title">Plan Actions Timeline</span>
    </header>
    <div class="plan-actions-timeline-body">
      <div
        v-for="action in actions"
        class="plan-actions-items"
        :key="action.actionName"
      >
        <span class="execution-time">{{ action.executionTime }}</span>
        <span class="action-name">{{ action.actionName }}</span>
        <span class="duration">{{ action.duration }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
type PlanAction = {
  executionTime: string;
  actionName: string;
  duration: string;
};

defineProps<{
  actions: PlanAction[];
}>();
</script>

<style scoped lang="scss">
.plan-actions-timeline-container {
  background-color: white;
  border-radius: 0.75rem;
  overflow-x: hidden;
  max-height: 50rem;
  border: 0.5px solid rgba(0, 0, 0, 0.15);

  .plan-actions-timeline-header {
    padding: 1.25rem 1.5rem 0.75rem 1.5rem;

    .title {
      font-size: 0.875rem;
      font-weight: 500;
      text-transform: uppercase;
    }
  }

  .plan-actions-timeline-body {
    overflow-y: auto;
    max-height: 46rem;

    .plan-actions-items {
      display: flex;
      align-items: center;
      height: 2rem;
      padding-left: 0.75rem;
      padding-right: 0.75rem;
      background-color: #f5f5f3;

      &:nth-child(odd) {
        background-color: #ffffff;
      }

      &:not(:last-child) {
        border-bottom: 0.5px solid rgba(0, 0, 0, 0.08);
      }

      .execution-time {
        flex-shrink: 0;
        width: 25%;
        font-size: 0.75rem;
        color: #888780;
      }

      .action-name {
        flex: 1;
        font-size: 0.75rem;
        font-weight: 500;
        color: #1f2937;
      }

      .duration {
        width: 25%;
        text-align: right;
        font-size: 0.75rem;
        color: #888780;
      }
    }
  }
}
</style>
