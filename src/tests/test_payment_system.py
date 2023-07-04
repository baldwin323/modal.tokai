```python
import unittest
from src.payment_system import process_payment, PaymentSchema

class TestPaymentSystem(unittest.TestCase):

    def setUp(self):
        self.creator_account = {
            "name": "Test Creator",
            "email": "test_creator@example.com",
            "account_id": "123456"
        }
        self.subscriber_account = {
            "name": "Test Subscriber",
            "email": "test_subscriber@example.com",
            "account_id": "654321"
        }
        self.payment_methods = ["credit card", "digital wallet", "cryptocurrency"]
        self.payment_data = {
            "amount": 100,
            "currency": "USD",
            "method": "credit card",
            "subscriber_id": self.subscriber_account["account_id"],
            "creator_id": self.creator_account["account_id"]
        }

    def test_process_payment(self):
        result = process_payment(self.payment_data)
        self.assertEqual(result, "PaymentSuccess")

    def test_payment_schema(self):
        schema = PaymentSchema()
        data, errors = schema.load(self.payment_data)
        self.assertEqual(errors, {})

if __name__ == "__main__":
    unittest.main()
```