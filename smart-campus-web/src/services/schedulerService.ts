import { serviceApi } from "../core/api/config";
import type { JobResponse, SchedulerStatus } from "../types/Scheduler";

function mapJobId(jobId: string): string {
  return jobId.split(":").slice(0, 2).join(":");
}

function mapCommand(args: string): string {
  const command = args.match(/command='([^']+)'/);
  return command ? command[1] : "";
}

function mapSchedulerResultToStatus(result: JobResponse): SchedulerStatus[] {
  return result.jobs.map((job) => ({
    actionId: mapJobId(job.id),
    scheduled: job.next_run_time,
    command: mapCommand(job.args),
  }));
}

export async function getSchedulerActions() {
  try {
    const { data } = await serviceApi.get<JobResponse>("/scheduler/jobs");
    return { data: mapSchedulerResultToStatus(data), error: null };
  } catch (error) {
    console.error("Error fetching scheduler actions:", error);
    return { data: null, error };
  }
}
