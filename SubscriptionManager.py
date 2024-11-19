from typing import List

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self, repo_url: str):
        """添加订阅的GitHub仓库URL"""
        self.subscriptions.append(repo_url)

    def remove_subscription(self, repo_url: str):
        """移除订阅的GitHub仓库URL"""
        self.subscriptions.remove(repo_url)

    def get_subscriptions(self) -> List[str]:
        """获取所有订阅的GitHub仓库URL"""
        return self.subscriptions
