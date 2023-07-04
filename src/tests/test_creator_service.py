```python
import unittest
from src.models.creator import Creator
from src.services.creator_service import CREATOR_SERVICE

class TestCreatorService(unittest.TestCase):

    def setUp(self):
        self.creator = Creator('creator1', 'password123', 'creator1@example.com')
        CREATOR_SERVICE.add_creator(self.creator)

    def test_add_creator(self):
        new_creator = Creator('creator2', 'password456', 'creator2@example.com')
        CREATOR_SERVICE.add_creator(new_creator)
        self.assertIn(new_creator, CREATOR_SERVICE.creators)

    def test_remove_creator(self):
        CREATOR_SERVICE.remove_creator(self.creator)
        self.assertNotIn(self.creator, CREATOR_SERVICE.creators)

    def test_get_creator_by_username(self):
        creator = CREATOR_SERVICE.get_creator_by_username('creator1')
        self.assertEqual(creator, self.creator)

    def test_get_creator_by_email(self):
        creator = CREATOR_SERVICE.get_creator_by_email('creator1@example.com')
        self.assertEqual(creator, self.creator)

    def tearDown(self):
        CREATOR_SERVICE.remove_creator(self.creator)

if __name__ == '__main__':
    unittest.main()
```