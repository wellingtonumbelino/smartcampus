<script setup lang="ts">
import mockDevices from "../../_mock/devices.json";
import mockRooms from "../../_mock/rooms.json";

const totalDevices = mockDevices.devices.length;
const totalRooms = mockRooms.rooms.length;
</script>

<template>
  <div class="dashboard">
    <section class="dashboard-section">
      <h2>Resumo</h2>
      <div class="cards">
        <div class="card">
          <h3>Total Devices</h3>
          <p>{{ totalDevices }}</p>
        </div>
        <div class="card">
          <h3>Total Rooms</h3>
          <p>{{ totalRooms }}</p>
        </div>
      </div>
    </section>
    <section class="dashboard-section">
      <h2>Actions</h2>
      <div class="dashboard-actions">
        <Button label="Run Planner" icon="pi pi-eye" />
        <Button label="View Rooms" icon="pi pi-eye" />
      </div>
    </section>
    <section class="dashboard-status">
      <h2>Status</h2>
      <div class="dashboard-status-info">
        <p>Planner last run: 2024-06-01 12:00:00</p>
        <p>Last planner result: Success</p>
      </div>
    </section>
  </div>
</template>

<style scoped lang="scss">
.dashboard {
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
