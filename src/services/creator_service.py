```python
from src.models.creator import Creator
from src.exceptions import CreatorServiceError

class CreatorService:
    def __init__(self):
        self.creators = []

    def add_creator(self, creator):
        if not isinstance(creator, Creator):
            raise CreatorServiceError("Invalid creator object")
        self.creators.append(creator)

    def get_creator(self, creator_id):
        for creator in self.creators:
            if creator.id == creator_id:
                return creator
        raise CreatorServiceError("Creator not found")

    def update_creator(self, creator_id, data):
        for creator in self.creators:
            if creator.id == creator_id:
                creator.update(data)
                return creator
        raise CreatorServiceError("Creator not found")

    def delete_creator(self, creator_id):
        for creator in self.creators:
            if creator.id == creator_id:
                self.creators.remove(creator)
                return
        raise CreatorServiceError("Creator not found")
```