```python
import unittest
from src.chatbot import generate_response

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.creator_account = {
            'username': 'test_creator',
            'content': 'Welcome to my Onlyfans!'
        }
        self.subscriber_account = {
            'username': 'test_subscriber',
            'message': 'Hello, I am a new subscriber!'
        }

    def test_generate_response(self):
        response = generate_response(self.creator_account, self.subscriber_account)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, '')

if __name__ == '__main__':
    unittest.main()
```