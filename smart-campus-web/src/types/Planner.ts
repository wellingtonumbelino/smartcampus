export interface PlannerResult {
  execution_time: number;
  job_id: string;
  message: string;
  status: string;
  scheduled_actions_count: number;
  states_evaluated: number;
  success: boolean;
}

export interface PlannerStatus {
  executionTime: string;
  jobId: string;
  message: string;
  status: string;
  actionsCount: number;
  statesEvaluated: number;
  success?: boolean;
}

export type PlanResultType = {
  execution_time: string;
  action_name: string;
  duration: string;
};
export interface PlannerResultJobId {
  job_id: string;
  status: string;
  execution_time: number;
  timestamp: string;
  plan: PlanResultType[];
}

export interface PlannerResultJobIdModel {
  executionTime: string;
  actionName: string;
  duration: string;
}
