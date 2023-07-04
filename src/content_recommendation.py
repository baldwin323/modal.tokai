```python
from src.services.recommendation_service import RECOMMENDATION_SERVICE
from src.config import RECOMMENDATION_CRITERIA
from src.exceptions import ContentRecommendationError
from src.constants import CONTENT_TYPES

def recommend_content(subscriber_id):
    try:
        subscriber = SUBSCRIBER_SERVICE.get_subscriber(subscriber_id)
        if not subscriber:
            raise ContentRecommendationError(f"No subscriber found with id {subscriber_id}")

        content_preferences = subscriber.get('preferences', {})
        recommended_content = []

        for content_type in CONTENT_TYPES:
            if content_type in content_preferences:
                content_list = CONTENT_SERVICE.get_content_by_type(content_type)
                if content_list:
                    for criteria in RECOMMENDATION_CRITERIA:
                        if criteria in content_preferences[content_type]:
                            recommended_content.extend(
                                RECOMMENDATION_SERVICE.recommend_by_criteria(content_list, criteria)
                            )

        if not recommended_content:
            raise ContentRecommendationError("No content found for recommendation")

        return {
            'subscriber_id': subscriber_id,
            'recommended_content': recommended_content
        }

    except Exception as e:
        raise ContentRecommendationError(str(e))
```