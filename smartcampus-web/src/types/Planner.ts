export interface PlannerResult {
  execution_time: number;
  job_id: string;
  message: string;
  status: string;
  scheduled_actions_count: number;
  success: boolean;
}

export interface PlannerStatus {
  executionTime: string;
  jobId: string;
  message: string;
  status: string;
  actionsCount: number;
  success?: boolean;
}
