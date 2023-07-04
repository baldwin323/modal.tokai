```python
import nltk
from nltk.chat.util import Chat, reflections

class ChatBot:
    def __init__(self, pairs, reflections):
        self.chat = Chat(pairs, reflections)

    def generate_response(self, user_input):
        return self.chat.respond(user_input)

pairs = [
    # Add pairs of patterns and responses
    # Example:
    # [
    #     r"my name is (.*)",
    #     ["Hello %1, how can I assist you today?",]
    # ],
]

reflections = {
    # Add custom reflections
    # Example:
    # "i am"       : "you are",
    # "i was"      : "you were",
}

if __name__ == "__main__":
    chatbot = ChatBot(pairs, reflections)
    while True:
        user_input = input("> ")
        if user_input == "quit":
            break
        response = chatbot.generate_response(user_input)
        print(response)
```