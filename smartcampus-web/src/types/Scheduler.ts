export interface Job {
  id: string;
  next_run_time: string;
  function: string;
  args: string;
}

export interface JobResponse {
  total_jobs: number;
  jobs: Job[];
}

export interface SchedulerStatus {
  actionId: string;
  scheduled: string;
  command: string;
}
