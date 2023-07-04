```python
from src.models.subscriber import Subscriber

class SubscriberService:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber_data):
        subscriber = Subscriber(subscriber_data)
        self.subscribers.append(subscriber)
        return subscriber

    def get_subscriber(self, subscriber_id):
        for subscriber in self.subscribers:
            if subscriber.id == subscriber_id:
                return subscriber
        return None

    def update_subscriber(self, subscriber_id, update_data):
        subscriber = self.get_subscriber(subscriber_id)
        if subscriber:
            subscriber.update(update_data)
            return subscriber
        return None

    def delete_subscriber(self, subscriber_id):
        subscriber = self.get_subscriber(subscriber_id)
        if subscriber:
            self.subscribers.remove(subscriber)
            return True
        return False
```