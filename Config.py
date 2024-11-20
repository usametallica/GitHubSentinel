# Config.py
import os

class Config:
    # 通过环境变量加载配置
    GITHUB_API_URL = os.getenv('GITHUB_API_URL', 'https://api.github.com')
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
    EMAIL_SMTP_SERVER = os.getenv('EMAIL_SMTP_SERVER')
    EMAIL_FROM = os.getenv('EMAIL_FROM')
    EMAIL_TO = os.getenv('EMAIL_TO')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    NOTIFICATION_FREQUENCY = os.getenv('NOTIFICATION_FREQUENCY', 'daily')

    # 检查关键环境变量是否成功获取
    if not GITHUB_TOKEN or not EMAIL_PASSWORD:
        raise ValueError("环境变量 GITHUB_TOKEN 或 EMAIL_PASSWORD 未设置。")