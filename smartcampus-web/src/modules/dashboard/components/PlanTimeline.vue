<template>
  <div class="plan-timeline">
    <header class="plan-timeline-header">
      <div class="header-info">
        <h3 class="title">Generated Action Plan</h3>
        <span class="label-info">
          <label>States Explored</label>
          <span>12</span>
        </span>
        <span class="label-info">
          <label>Plan Size</label>
          <span>8 actions</span>
        </span>
        <span class="label-info">
          <label>Execution Time</label>
          <span>2.5 s</span>
        </span>
      </div>
    </header>
  </div>
</template>

<style scoped lang="scss">
.plan-timeline {
  margin-top: 2rem;
  border: 1px solid #cecece;
  border-radius: 0.625rem;

  .plan-timeline-header {
    display: flex;
    padding: 1rem 1.5rem;
    border-bottom: 1px solid #cecece;

    .header-info {
      display: flex;
      gap: 1.5rem;
      align-items: center;

      .title {
        margin: 0;
      }

      .label-info {
        display: flex;
        flex-direction: column;
        gap: 0.125rem;

        label {
          font-size: 0.75rem;
          text-transform: uppercase;
        }

        span {
          font-size: 0.875rem;
        }
      }
    }
  }
}
</style>
