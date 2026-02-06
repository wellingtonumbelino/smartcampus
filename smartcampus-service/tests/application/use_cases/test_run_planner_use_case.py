from unittest.mock import MagicMock, patch
from app.application.use_cases.run_planner_use_case_impl import RunPlannerUseCaseImpl

def test_execute_planner_success_calls_scheduler():
  gen_pddl_mock = MagicMock()
  fs_mock = MagicMock()
  planner_mock = MagicMock()
  parser_mock = MagicMock()
  scheduler_mock = MagicMock()

  planner_mock.create_job.return_value = "job123"
  planner_mock.run.return_value = {"success": True, "execution_time": 1.5}
  fs_mock.get_plan_path.return_value = "fake_path.txt"

  parser_mock.parse_file.return_value = [MagicMock(name="Action1")]

  with patch("builtins.open", MagicMock()):
    with patch("app.application.use_cases.run_planner_use_case_impl.open", MagicMock()):
      use_case = RunPlannerUseCaseImpl(
        generate_pddl_use_case=gen_pddl_mock,
        filesystem_service=fs_mock,
        planner_service=planner_mock,
        parser=planner_mock,
        scheduler=scheduler_mock
      )

      result = use_case.execute(input_data={"test": "data"})

      assert result["job_id"] == "job123"
      assert result["scheduled_actions_count"] == 1

      scheduler_mock.schedule_many.assert_called_once()
      fs_mock.archive_job.assert_called_with("job_123", "success", 1.5)