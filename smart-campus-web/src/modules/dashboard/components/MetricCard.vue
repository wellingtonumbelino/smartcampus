<template>
  <div class="card-metric-container">
    <Avatar
      :icon="icon"
      :style="{ backgroundColor: iconBg, color: iconColor }"
      size="large"
    />
    <div class="card-metric-info">
      <span class="card-metric-value">{{ value }}</span>
      <span class="card-metric-label">{{ label }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  icon: string;
  iconColor: string;
  iconBg: string;
  value: string | number;
  label: string;
}>();
</script>

<style scoped lang="scss">
.card-metric-container {
  display: flex;
  border-radius: 0.75rem;
  padding: 1rem;
  align-items: center;
  gap: 1rem;
  background-color: #f9fafb;

  .card-metric-info {
    display: flex;
    flex-direction: column;
    gap: 0.125rem;

    .card-metric-value {
      font-size: 1.875rem;
      font-weight: 600;
    }

    .card-metric-label {
      font-size: 0.875rem;
    }
  }
}
</style>
