<template>
  <div class="no-plan-container">
    <div class="no-plan-presentation">
      <i class="pi pi-wave-pulse" style="font-size: 4rem" />
      <h3 class="no-plan-title">No plan generated yet</h3>
      <p class="no-plan-description">
        Run the planner to generate a daily plan of automated actions for the
        IoT environment
      </p>
      <Button
        icon="pi pi-play"
        label="Generate Plan"
        raised
        severity="help"
        @click="$emit('generate-plan')"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
defineEmits(["generate-plan"]);
</script>

<style scoped lang="scss">
.no-plan-container {
  flex: 1;
  overflow: auto;
  padding: 1rem;

  .no-plan-presentation {
    background-color: white;
    border: 0.5px solid rgba(0, 0, 0, 0.15);
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 31.25rem;
    padding: 3rem;

    .no-plan-title {
      font-size: 1.25rem;
      font-weight: 500;
      margin-bottom: 0.5rem;
    }

    .no-plan-description {
      font-size: 0.875rem;
      margin-bottom: 1.5rem;
      text-align: center;
    }
  }
}
</style>
