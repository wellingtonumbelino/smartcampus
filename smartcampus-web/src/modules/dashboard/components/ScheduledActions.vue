<template>
  <div class="scheduled-actions-container">
    <header class="scheduled-actions-header">
      <span class="title">IoT API Requests</span>
    </header>
    <div class="scheduled-actions-body">
      <DataTable :value="scheduleActions">
        <Column v-for="col in columns" :header="col.header">
          <template #body="{ data }">
            <span class="p-column-data-field">{{ data[col.field] }}</span>
          </template>
        </Column>
        <Column header="Status">
          <template #body>
            <Tag rounded severity="success" value="Success" />
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script setup lang="ts">
type ScheduledAction = {
  actionId: string;
  scheduled: string;
  command: string;
};

type ColActionItem = {
  field: string;
  header: string;
};

defineProps<{
  scheduleActions: ScheduledAction[];
}>();

const columns: ColActionItem[] = [
  { field: "actionId", header: "Action" },
  { field: "scheduled", header: "Scheduled" },
  { field: "command", header: "Command" },
];
</script>

<style scoped lang="scss">
.scheduled-actions-container {
  background-color: white;
  border-radius: 0.75rem;
  border: 0.5px solid rgba(0, 0, 0, 0.15);

  .scheduled-actions-header {
    padding: 1.25rem;

    .title {
      font-size: 0.875rem;
      font-weight: 500;
      text-transform: uppercase;
    }
  }

  .scheduled-actions-body {
    overflow-x: auto;

    .p-datatable {
      .p-datatable-table-container {
        .p-datatable-table {
          .p-datatable-tbody {
            tr {
              td {
                .p-column-data-field {
                  font-size: 0.875rem;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>
