<template>
  <div class="info-card-container">
    <span class="label">{{ label }}</span>
    <span class="value">{{ value }}</span>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string;
  value: string | number;
}>();
</script>

<style scoped lang="scss">
.info-card-container {
  background-color: #f9fafb;
  padding: 0.75rem;
  border-radius: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;

  .label {
    font-size: 0.75rem;
    color: #6b7280;
  }

  .value {
    font-size: 1.25rem;
    font-weight: 600;
  }
}
</style>
