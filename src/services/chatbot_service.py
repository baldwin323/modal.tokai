```python
from src.chatbot import Chatbot
from src.models.subscriber import Subscriber
from src.exceptions import ChatbotError

class ChatbotService:
    def __init__(self):
        self.chatbot = Chatbot()

    def handle_message(self, subscriber: Subscriber, message: str):
        try:
            response = self.chatbot.process_message(message)
            return response
        except Exception as e:
            raise ChatbotError("Failed to process message") from e

CHATBOT_SERVICE = ChatbotService()
```