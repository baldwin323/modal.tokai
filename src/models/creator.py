```python
class Creator:
    def __init__(self, id, username, password, email, social_media_accounts):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.social_media_accounts = social_media_accounts

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "social_media_accounts": self.social_media_accounts
        }
```