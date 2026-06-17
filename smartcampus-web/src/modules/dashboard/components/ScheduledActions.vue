<template>
  <div class="scheduled-actions-container">
    <header class="scheduled-actions-header">
      <span class="title">IoT API Requests</span>
    </header>
    <div class="scheduled-actions-body">
      <DataTable :value="scheduleActions">
        <Column v-for="col in columns" :header="col.header">
          <template #body="{ data }">
            <span class="p-column-data-field">
              {{
                col.field === "scheduled"
                  ? formatDate(data[col.field])
                  : data[col.field]
              }}
            </span>
          </template>
        </Column>
        <Column header="Status">
          <template #body="{ data }">
            <Tag
              rounded
              :severity="setTagSeverity(data.scheduled)"
              :value="setTagValue(data.scheduled)"
            />
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { SchedulerStatus } from "../../../types/Scheduler";

type ColActionItem = {
  field: string;
  header: string;
};

type StatusTagType = "success" | "info";

const props = defineProps<{
  scheduleActions: SchedulerStatus[];
}>();

const columns: ColActionItem[] = [
  { field: "actionId", header: "Action" },
  { field: "scheduled", header: "Scheduled" },
  { field: "command", header: "Command" },
];

function formatDate(value: string): string {
  const date = new Date(value);

  if (isNaN(date.getTime())) return value;

  const month = new Intl.DateTimeFormat("en-US", { month: "short" }).format(
    date,
  );
  const day = String(date.getDate()).padStart(2, "0");
  const year = date.getFullYear();

  const hours = date.getHours() % 12 || 12;
  const minute = String(date.getMinutes()).padStart(2, "0");
  const period = date.getHours() < 12 ? "AM" : "PM";

  return `${month} ${day} ${year} ${hours}:${minute} ${period}`;
}

function handleScheduledDataExecuted(value: string): boolean {
  const targetDate = new Date(value);
  const currentDate = new Date();

  targetDate.setUTCMilliseconds(0);
  currentDate.setUTCMilliseconds(0);

  return targetDate.getTime() > currentDate.getTime();
}

function setTagValue(value: string): string {
  return handleScheduledDataExecuted(value) ? "Pending" : "Sending";
}

function setTagSeverity(value: string): StatusTagType {
  return handleScheduledDataExecuted(value) ? "info" : "success";
}
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
