```python
import pandas as pd
from sklearn import metrics

class Analytics:
    def __init__(self, content_data, engagement_data, revenue_data):
        self.content_data = pd.DataFrame(content_data)
        self.engagement_data = pd.DataFrame(engagement_data)
        self.revenue_data = pd.DataFrame(revenue_data)

    def analyze_performance(self):
        content_popularity = self._analyze_content_popularity()
        subscriber_engagement = self._analyze_subscriber_engagement()
        revenue_generation = self._analyze_revenue_generation()

        performance_report = {
            'Content Popularity': content_popularity,
            'Subscriber Engagement': subscriber_engagement,
            'Revenue Generation': revenue_generation
        }

        return performance_report

    def _analyze_content_popularity(self):
        # Analyze content popularity based on views, likes, comments, etc.
        popularity_metrics = self.content_data.describe()
        return popularity_metrics

    def _analyze_subscriber_engagement(self):
        # Analyze subscriber engagement based on comments, likes, shares, etc.
        engagement_metrics = self.engagement_data.describe()
        return engagement_metrics

    def _analyze_revenue_generation(self):
        # Analyze revenue generation based on subscriptions, tips, purchases, etc.
        revenue_metrics = self.revenue_data.describe()
        return revenue_metrics
```