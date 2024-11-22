# DailyProgressExporter.py
import os
import requests
from datetime import datetime
from Config import Config

class DailyProgressExporter:
    def __init__(self, github_token: str):
        self.github_token = github_token
        self.headers = {"Authorization": f"token {self.github_token}"}

    def fetch_issues_and_pulls(self, repo_url: str) -> dict:
        """获取仓库的 issues 和 pull requests"""
        repo_name = self.extract_repo_name(repo_url)
        issues_url = f"{Config.GITHUB_API_URL}/repos/{repo_name}/issues"
        pulls_url = f"{Config.GITHUB_API_URL}/repos/{repo_name}/pulls"

        issues = self.fetch_data(issues_url)
        pulls = self.fetch_data(pulls_url)

        return {"issues": issues, "pulls": pulls}

    def fetch_data(self, url: str) -> list:
        """从指定 URL 获取数据"""
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"获取数据失败: {response.status_code} - {response.text}")
            return []

    def export_to_markdown(self, repo_url: str, data: dict):
        """将 issues 和 pull requests 导出为 Markdown 文件"""
        repo_name = self.extract_repo_name(repo_url).replace("/", "_")
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{repo_name}_{date_str}.md"

        content = f"# {repo_name} - Daily Progress ({date_str})\n\n"
        content += "## Issues\n"
        for issue in data.get("issues", []):
            content += f"- [{issue.get('title')}]({issue.get('html_url')})\n"

        content += "\n## Pull Requests\n"
        for pull in data.get("pulls", []):
            content += f"- [{pull.get('title')}]({pull.get('html_url')})\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"导出每日进展为 Markdown 文件: {filename}")

    @staticmethod
    def extract_repo_name(repo_url: str) -> str:
        """从仓库URL中提取仓库名称"""
        parts = repo_url.strip("/").split("/")
        return "/".join(parts[-2:])

# Example usage
if __name__ == "__main__":
    exporter = DailyProgressExporter(Config.GITHUB_TOKEN)
    repo_url = "https://github.com/langchain-ai/langchain"
    data = exporter.fetch_issues_and_pulls(repo_url)
    exporter.export_to_markdown(repo_url, data)
