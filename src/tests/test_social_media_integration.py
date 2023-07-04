```python
import unittest
from unittest.mock import patch
from src.social_media_integration import integrate_social_media
from src.services.social_media_service import SocialMediaService
from src.exceptions import SocialMediaIntegrationError

class TestSocialMediaIntegration(unittest.TestCase):

    @patch.object(SocialMediaService, 'integrate')
    def test_integrate_social_media_success(self, mock_integrate):
        mock_integrate.return_value = True
        result = integrate_social_media()
        self.assertTrue(result)

    @patch.object(SocialMediaService, 'integrate')
    def test_integrate_social_media_failure(self, mock_integrate):
        mock_integrate.side_effect = SocialMediaIntegrationError
        with self.assertRaises(SocialMediaIntegrationError):
            integrate_social_media()

if __name__ == '__main__':
    unittest.main()
```