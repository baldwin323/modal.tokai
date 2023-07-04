```python
import unittest
from src.compatibility import check_compatibility

class TestCompatibility(unittest.TestCase):

    def setUp(self):
        self.creator_account = {
            "username": "test_creator",
            "platform": "Windows"
        }
        self.subscriber_account = {
            "username": "test_subscriber",
            "platform": "iOS"
        }

    def test_check_compatibility(self):
        # Test compatibility check for creator account
        result = check_compatibility(self.creator_account)
        self.assertTrue(result, "Compatibility check failed for creator account")

        # Test compatibility check for subscriber account
        result = check_compatibility(self.subscriber_account)
        self.assertTrue(result, "Compatibility check failed for subscriber account")

if __name__ == "__main__":
    unittest.main()
```