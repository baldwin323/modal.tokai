```python
from src.config import AUTOMATED_TASKS
from src.services.task_service import TASK_SERVICE
from src.exceptions import AutomatedTasksError

class AutomatedTasks:
    def __init__(self):
        self.tasks = AUTOMATED_TASKS

    def automate_tasks(self):
        for task in self.tasks:
            try:
                TASK_SERVICE.perform_task(task)
            except Exception as e:
                raise AutomatedTasksError(f"Failed to perform task: {task}. Error: {str(e)}")

    def schedule_tasks(self):
        for task in self.tasks:
            try:
                TASK_SERVICE.schedule_task(task)
            except Exception as e:
                raise AutomatedTasksError(f"Failed to schedule task: {task}. Error: {str(e)}")

if __name__ == "__main__":
    automated_tasks = AutomatedTasks()
    automated_tasks.automate_tasks()
    automated_tasks.schedule_tasks()
```