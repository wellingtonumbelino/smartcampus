<template>
  <div class="loading-plan-container">
    <div class="metric-cards">
      <Skeleton height="5.5rem" />
      <Skeleton height="5.5rem" />
    </div>

    <div class="generate-plan">
      <Skeleton height="16.5rem" />
    </div>

    <div class="plan-actions">
      <Skeleton height="18.375rem" />
      <Skeleton height="18.375rem" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.loading-plan-container {
  .metric-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 0.875rem;
  }

  .plan-actions {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }
}
</style>
