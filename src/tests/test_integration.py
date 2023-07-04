```python
import unittest
from src.integration import integrate_social_media

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.creator_account = {
            "username": "test_creator",
            "email": "test_creator@example.com",
            "password": "test_password"
        }

    def test_integrate_social_media(self):
        result = integrate_social_media(self.creator_account)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```