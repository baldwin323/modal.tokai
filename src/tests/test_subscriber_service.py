```python
import unittest
from src.services.subscriber_service import SubscriberService
from src.models.subscriber import Subscriber

class TestSubscriberService(unittest.TestCase):

    def setUp(self):
        self.subscriber_service = SubscriberService()
        self.subscriber = Subscriber("test_subscriber", "test@email.com")

    def test_add_subscriber(self):
        result = self.subscriber_service.add_subscriber(self.subscriber)
        self.assertEqual(result, True)

    def test_remove_subscriber(self):
        self.subscriber_service.add_subscriber(self.subscriber)
        result = self.subscriber_service.remove_subscriber(self.subscriber)
        self.assertEqual(result, True)

    def test_get_subscriber(self):
        self.subscriber_service.add_subscriber(self.subscriber)
        result = self.subscriber_service.get_subscriber(self.subscriber.name)
        self.assertEqual(result, self.subscriber)

    def test_update_subscriber(self):
        self.subscriber_service.add_subscriber(self.subscriber)
        updated_subscriber = Subscriber("updated_subscriber", "updated@email.com")
        result = self.subscriber_service.update_subscriber(self.subscriber.name, updated_subscriber)
        self.assertEqual(result, updated_subscriber)

if __name__ == '__main__':
    unittest.main()
```