```python
from src.services.chatbot_service import CHATBOT_SERVICE
from src.constants import DEFAULT_RESPONSE
from src.exceptions import ChatbotError

class Chatbot:
    def __init__(self):
        self.service = CHATBOT_SERVICE

    def handle_message(self, message):
        try:
            response = self.service.process_message(message)
        except Exception as e:
            raise ChatbotError("Error processing message") from e

        if not response:
            response = DEFAULT_RESPONSE

        return response
```