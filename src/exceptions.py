```python
class OnlyFansManagerAIException(Exception):
    """Base exception class for OnlyFans Manager AI"""
    pass

class ChatbotError(OnlyFansManagerAIException):
    """Exception raised for errors in the chatbot module"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SocialMediaIntegrationError(OnlyFansManagerAIException):
    """Exception raised for errors in the social media integration module"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AutomatedTasksError(OnlyFansManagerAIException):
    """Exception raised for errors in the automated tasks module"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ContentRecommendationError(OnlyFansManagerAIException):
    """Exception raised for errors in the content recommendation module"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```