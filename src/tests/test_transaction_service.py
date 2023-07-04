```python
import unittest
from src.models.transaction import Transaction
from src.services.transaction_service import TRANSACTION_SERVICE

class TestTransactionService(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction('123', '456', '789', 100.0, 'USD', 'completed')
        TRANSACTION_SERVICE.transactions = [self.transaction]

    def test_get_transaction_by_id(self):
        transaction = TRANSACTION_SERVICE.get_transaction_by_id('123')
        self.assertEqual(transaction, self.transaction)

    def test_get_transactions_by_creator_id(self):
        transactions = TRANSACTION_SERVICE.get_transactions_by_creator_id('456')
        self.assertEqual(transactions, [self.transaction])

    def test_get_transactions_by_subscriber_id(self):
        transactions = TRANSACTION_SERVICE.get_transactions_by_subscriber_id('789')
        self.assertEqual(transactions, [self.transaction])

    def test_create_transaction(self):
        new_transaction = Transaction('124', '457', '790', 200.0, 'USD', 'pending')
        TRANSACTION_SERVICE.create_transaction(new_transaction)
        self.assertIn(new_transaction, TRANSACTION_SERVICE.transactions)

    def test_update_transaction_status(self):
        TRANSACTION_SERVICE.update_transaction_status('123', 'failed')
        self.assertEqual(self.transaction.status, 'failed')

if __name__ == '__main__':
    unittest.main()
```