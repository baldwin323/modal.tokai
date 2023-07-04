```python
from src.models.content import Content
from src.services.content_service import CONTENT_SERVICE
from src.config import RECOMMENDATION_CRITERIA

class RecommendationService:
    def __init__(self):
        self.content_service = CONTENT_SERVICE

    def recommend_content(self, subscriber):
        """
        Recommend content to a subscriber based on their preferences, interests, and previous engagement.
        """
        # Fetch all content
        all_content = self.content_service.get_all_content()

        # Filter content based on recommendation criteria
        recommended_content = self.filter_content(all_content, subscriber)

        return recommended_content

    def filter_content(self, all_content, subscriber):
        """
        Filter content based on the subscriber's preferences, interests, and previous engagement.
        """
        recommended_content = []

        for content in all_content:
            # Check if content matches the subscriber's preferences and interests
            if self.match_preferences(content, subscriber) and self.match_interests(content, subscriber):
                recommended_content.append(content)

        # Sort content based on previous engagement
        recommended_content.sort(key=lambda content: self.get_engagement_score(content, subscriber), reverse=True)

        return recommended_content

    def match_preferences(self, content, subscriber):
        """
        Check if content matches the subscriber's preferences.
        """
        return content.type in subscriber.preferences

    def match_interests(self, content, subscriber):
        """
        Check if content matches the subscriber's interests.
        """
        return any(interest in content.tags for interest in subscriber.interests)

    def get_engagement_score(self, content, subscriber):
        """
        Calculate an engagement score for content based on the subscriber's previous engagement.
        """
        return subscriber.engagement.get(content.id, 0)

RECOMMENDATION_SERVICE = RecommendationService()
```