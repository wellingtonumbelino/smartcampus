import { serviceApi } from "../core/api/config";
import mockExample from "../_mock/example.json";
import type { PlannerResult, PlannerStatus } from "../types/Planner";

function mapPlannerResultToStatus(result: PlannerResult): PlannerStatus {
  return {
    executionTime: result.execution_time.toString().concat(" ms"),
    jobId: result.job_id,
    message: result.message,
    status: result.status,
    actionsCount: result.scheduled_actions_count,
  };
}

export async function runPlanner() {
  try {
    const { data } = await serviceApi.post<PlannerResult>(
      "/planner/run",
      mockExample,
    );
    return { data: mapPlannerResultToStatus(data), error: null };
  } catch (error) {
    console.error("Error running planner:", error);
    return { data: null, error };
  }
}
