```python
import unittest
from unittest.mock import patch
from src.services.task_service import TASK_SERVICE
from src.exceptions import AutomatedTasksError

class TestAutomatedTasks(unittest.TestCase):

    @patch.object(TASK_SERVICE, 'automate_tasks')
    def test_automate_tasks_success(self, mock_automate_tasks):
        mock_automate_tasks.return_value = True
        result = TASK_SERVICE.automate_tasks()
        self.assertTrue(result)

    @patch.object(TASK_SERVICE, 'automate_tasks')
    def test_automate_tasks_failure(self, mock_automate_tasks):
        mock_automate_tasks.side_effect = AutomatedTasksError
        with self.assertRaises(AutomatedTasksError):
            TASK_SERVICE.automate_tasks()

if __name__ == '__main__':
    unittest.main()
```