```python
from src.models.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, creator_id, subscriber_id, content_id, amount):
        transaction = Transaction(creator_id, subscriber_id, content_id, amount)
        self.transactions.append(transaction)
        return transaction

    def get_transactions_by_creator(self, creator_id):
        return [transaction for transaction in self.transactions if transaction.creator_id == creator_id]

    def get_transactions_by_subscriber(self, subscriber_id):
        return [transaction for transaction in self.transactions if transaction.subscriber_id == subscriber_id]

    def get_transactions_by_content(self, content_id):
        return [transaction for transaction in self.transactions if transaction.content_id == content_id]

    def get_total_revenue(self, creator_id):
        transactions = self.get_transactions_by_creator(creator_id)
        return sum(transaction.amount for transaction in transactions)
```