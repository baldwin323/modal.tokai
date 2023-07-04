```python
import json
import os
from datetime import datetime

def load_config(file_path):
    """
    Load configuration from a JSON file.
    """
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

def save_config(config, file_path):
    """
    Save configuration to a JSON file.
    """
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

def format_date(date):
    """
    Format date to a string in the format of YYYY-MM-DD.
    """
    return date.strftime('%Y-%m-%d')

def parse_date(date_str):
    """
    Parse date from a string in the format of YYYY-MM-DD.
    """
    return datetime.strptime(date_str, '%Y-%m-%d')

def create_dir_if_not_exists(dir_path):
    """
    Create a directory if it does not exist.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def validate_social_media_platform(platform):
    """
    Validate if the given platform is supported.
    """
    supported_platforms = ['Kik', 'Telegram', 'WhatsApp']
    if platform not in supported_platforms:
        raise ValueError(f'Unsupported social media platform: {platform}')
```
