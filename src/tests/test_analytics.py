```python
import unittest
from src.analytics import analyze_performance

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.creator_account = {
            'username': 'test_creator',
            'content': ['post1', 'post2', 'post3'],
            'subscribers': ['user1', 'user2', 'user3']
        }
        self.content_data = {
            'post1': {'views': 100, 'likes': 50, 'comments': 20},
            'post2': {'views': 200, 'likes': 100, 'comments': 50},
            'post3': {'views': 150, 'likes': 75, 'comments': 30}
        }
        self.engagement_data = {
            'user1': {'viewed': ['post1', 'post2'], 'liked': ['post1'], 'commented': ['post2']},
            'user2': {'viewed': ['post1', 'post3'], 'liked': ['post1', 'post3'], 'commented': []},
            'user3': {'viewed': ['post2'], 'liked': ['post2'], 'commented': ['post2']}
        }
        self.revenue_data = {
            'subscriptions': 300,
            'tips': 100,
            'paid_messages': 50
        }

    def test_analyze_performance(self):
        result = analyze_performance(self.creator_account, self.content_data, self.engagement_data, self.revenue_data)
        self.assertIsInstance(result, dict)
        self.assertIn('PerformanceReport', result)

if __name__ == '__main__':
    unittest.main()
```