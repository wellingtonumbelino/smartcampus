<!-- :style="{ backgroundColor: '#185FA5' }" -->
<template>
  <div class="generated-plan-container">
    <div class="generated-plan-header">
      <span class="generated-plan-title">Last Generate Plan</span>
      <Button icon="pi pi-play" label="Generate Plan" raised severity="help" />
    </div>

    <div class="generated-plan-status">
      <Tag
        icon="pi pi-check-circle"
        rounded
        severity="success"
        value="Success"
      />
      <span class="generated-plan-timestamp"> Today at 09:42:58 </span>
    </div>

    <div class="generated-plan-info">
      <InfoCard label="Execution time" value="2.5s" />
      <InfoCard label="Plan size" value="12 actions" />
      <InfoCard label="states analyzed" value="18" />
      <InfoCard label="Planner" value="POPF-TIF" />
    </div>
  </div>
</template>

<script setup lang="ts">
import InfoCard from "./InfoCard.vue";
</script>

<style scoped lang="scss">
.generated-plan-container {
  background-color: white;
  border-radius: 0.75rem;
  border: 0.5px solid rgba(0, 0, 0, 0.15);
  padding: 1.25rem;

  .generated-plan-header {
    display: flex;
    justify-content: space-between;
    align-items: center;

    .generated-plan-title {
      font-size: 0.875rem;
      font-weight: 500;
      text-transform: uppercase;
    }
  }

  .generated-plan-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;

    .generated-plan-timestamp {
      font-size: 0.75rem;
    }
  }

  .generated-plan-info {
    display: grid;
    grid-template-columns: repeat(2, minmax(200px, 1fr));
    gap: 0.75rem;
    margin-top: 1rem;
  }
}
</style>
