```python
from src.models.content import Content
from src.exceptions import ContentServiceError

class ContentService:
    def __init__(self):
        self.contents = []

    def create_content(self, creator_id, content_data):
        try:
            new_content = Content(creator_id, **content_data)
            self.contents.append(new_content)
            return new_content
        except Exception as e:
            raise ContentServiceError("Failed to create content") from e

    def get_content(self, content_id):
        try:
            return next(content for content in self.contents if content.id == content_id)
        except StopIteration:
            raise ContentServiceError("Content not found")

    def update_content(self, content_id, update_data):
        try:
            content = self.get_content(content_id)
            content.update(**update_data)
            return content
        except Exception as e:
            raise ContentServiceError("Failed to update content") from e

    def delete_content(self, content_id):
        try:
            self.contents = [content for content in self.contents if content.id != content_id]
        except Exception as e:
            raise ContentServiceError("Failed to delete content") from e

    def get_all_content(self, creator_id):
        try:
            return [content for content in self.contents if content.creator_id == creator_id]
        except Exception as e:
            raise ContentServiceError("Failed to get all content") from e
```