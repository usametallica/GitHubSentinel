import requests
from typing import Dict
from Config import Config

class UpdateRetriever:
    def __init__(self, github_token: str):
        self.github_token = github_token

    def fetch_repo_updates(self, repo_url: str) -> Dict:
        """从GitHub API获取仓库的最新更新"""
        headers = {"Authorization": f"token {self.github_token}"}
        repo_name = self.extract_repo_name(repo_url)
        response = requests.get(f"{Config.GITHUB_API_URL}/repos/{repo_name}/events", headers=headers)
        
        # 打印响应状态和数据以进行调试
        print(f"GitHub API 响应状态: {response.status_code}")
        if response.status_code != 200:
            print(f"错误：GitHub API 响应 - {response.text}")
            return {}
        
        try:
            return response.json()
        except ValueError:
            print("错误：无法解析 JSON 响应。")
            return {}

    @staticmethod
    def extract_repo_name(repo_url: str) -> str:
        """从仓库URL中提取仓库名称"""
        parts = repo_url.strip("/").split("/")
        return "/".join(parts[-2:])
