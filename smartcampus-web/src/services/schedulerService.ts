import { serviceApi } from "../core/api/config";
import type { JobResponse, SchedulerStatus } from "../types/Scheduler";

function mapSchedulerResultToStatus(result: JobResponse): SchedulerStatus[] {
  return result.jobs.map((job) => ({
    jobId: job.id,
    nextAction: job.function,
    args: job.args,
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
