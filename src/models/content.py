```python
class Content:
    def __init__(self, id, creator_id, title, description, type, created_at, updated_at):
        self.id = id
        self.creator_id = creator_id
        self.title = title
        self.description = description
        self.type = type
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"Content(id={self.id}, creator_id={self.creator_id}, title={self.title}, description={self.description}, type={self.type}, created_at={self.created_at}, updated_at={self.updated_at})"

    def to_dict(self):
        return {
            "id": self.id,
            "creator_id": self.creator_id,
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
```