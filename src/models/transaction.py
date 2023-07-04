```python
class Transaction:
    def __init__(self, transaction_id, subscriber_id, creator_id, content_id, amount, transaction_date):
        self.transaction_id = transaction_id
        self.subscriber_id = subscriber_id
        self.creator_id = creator_id
        self.content_id = content_id
        self.amount = amount
        self.transaction_date = transaction_date

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'subscriber_id': self.subscriber_id,
            'creator_id': self.creator_id,
            'content_id': self.content_id,
            'amount': self.amount,
            'transaction_date': self.transaction_date
        }
```