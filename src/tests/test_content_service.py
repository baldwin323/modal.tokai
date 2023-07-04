```python
import unittest
from src.models.content import Content
from src.services.content_service import ContentService

class TestContentService(unittest.TestCase):

    def setUp(self):
        self.content_service = ContentService()
        self.sample_content = Content("Sample Title", "Sample Description", "Sample URL", "Sample Creator")

    def test_add_content(self):
        result = self.content_service.add_content(self.sample_content)
        self.assertEqual(result, True)

    def test_get_content(self):
        self.content_service.add_content(self.sample_content)
        result = self.content_service.get_content("Sample Title")
        self.assertEqual(result, self.sample_content)

    def test_update_content(self):
        self.content_service.add_content(self.sample_content)
        updated_content = Content("Sample Title", "Updated Description", "Updated URL", "Updated Creator")
        result = self.content_service.update_content(updated_content)
        self.assertEqual(result, True)

    def test_delete_content(self):
        self.content_service.add_content(self.sample_content)
        result = self.content_service.delete_content("Sample Title")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
```