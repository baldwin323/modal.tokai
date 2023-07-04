```python
class Subscriber:
    def __init__(self, id, name, preferences, engagement):
        self.id = id
        self.name = name
        self.preferences = preferences
        self.engagement = engagement

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_preferences(self):
        return self.preferences

    def get_engagement(self):
        return self.engagement

    def set_preferences(self, preferences):
        self.preferences = preferences

    def set_engagement(self, engagement):
        self.engagement = engagement
```