```python
import unittest
from src.services.chatbot_service import CHATBOT_SERVICE
from src.exceptions import ChatbotError

class TestChatbotService(unittest.TestCase):

    def setUp(self):
        self.chatbot_service = CHATBOT_SERVICE

    def test_handle_message(self):
        test_message = "Hello, how are you?"
        response = self.chatbot_service.handle_message(test_message)
        self.assertIsNotNone(response, "Response should not be None")

    def test_handle_message_with_empty_message(self):
        test_message = ""
        with self.assertRaises(ChatbotError):
            self.chatbot_service.handle_message(test_message)

    def test_handle_message_with_none_message(self):
        test_message = None
        with self.assertRaises(ChatbotError):
            self.chatbot_service.handle_message(test_message)

if __name__ == '__main__':
    unittest.main()
```