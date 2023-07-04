```python
from src.services.social_media_service import SOCIAL_MEDIA_SERVICE
from src.config import SOCIAL_MEDIA_PLATFORMS
from src.exceptions import SocialMediaIntegrationError

class SocialMediaIntegration:
    def __init__(self):
        self.social_media_service = SOCIAL_MEDIA_SERVICE

    def integrate_social_media(self):
        try:
            for platform in SOCIAL_MEDIA_PLATFORMS:
                self.social_media_service.connect(platform)
        except Exception as e:
            raise SocialMediaIntegrationError("Failed to integrate social media platforms") from e

    def post_update(self, message):
        try:
            for platform in SOCIAL_MEDIA_PLATFORMS:
                self.social_media_service.post_update(platform, message)
        except Exception as e:
            raise SocialMediaIntegrationError("Failed to post update on social media platforms") from e

    def get_updates(self):
        updates = {}
        try:
            for platform in SOCIAL_MEDIA_PLATFORMS:
                updates[platform] = self.social_media_service.get_updates(platform)
        except Exception as e:
            raise SocialMediaIntegrationError("Failed to get updates from social media platforms") from e
        return updates
```