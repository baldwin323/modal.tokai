```python
from src.social_media_integration import integrate_social_media
from src.config import SOCIAL_MEDIA_PLATFORMS
from src.exceptions import SocialMediaIntegrationError

class SocialMediaService:
    def __init__(self):
        self.platforms = SOCIAL_MEDIA_PLATFORMS

    def integrate_platforms(self, creator):
        try:
            for platform in self.platforms:
                integrate_social_media(creator, platform)
        except Exception as e:
            raise SocialMediaIntegrationError("Failed to integrate social media platforms") from e

SOCIAL_MEDIA_SERVICE = SocialMediaService()
```