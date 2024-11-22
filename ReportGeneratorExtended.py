# ReportGeneratorExtended.py
import os
from LLMClient import LLMClient
from datetime import datetime

class ReportGeneratorExtended:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client

    def generate_daily_report(self, repo_name: str, issues: list, pulls: list) -> str:
        """使用 GPT-4 生成每日项目报告"""
        summary = self.llm_client.summarize_issues_and_pulls(issues, pulls)
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"{repo_name.replace('/', '_')}_daily_report_{date_str}.md"

        content = (
            f"# {repo_name} - Daily Report ({date_str})\n\n"
            f"## Summary\n{summary}\n\n"
            f"## Issues\n"
        )
        for issue in issues:
            content += f"- [{issue.get('title')}]({issue.get('html_url')})\n"

        content += "\n## Pull Requests\n"
        for pull in pulls:
            content += f"- [{pull.get('title')}]({pull.get('html_url')})\n"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"生成每日项目报告为 Markdown 文件: {filename}")
        return filename

# Example usage
if __name__ == "__main__":
    from Config import Config

    llm_client = LLMClient(Config.GITHUB_TOKEN)
    report_generator = ReportGeneratorExtended(llm_client)
    repo_name = "langchain-ai/langchain"
    issues = [
        {"title": "Bug fix in module X", "html_url": "https://github.com/langchain-ai/langchain/issues/1"},
        {"title": "New feature: Add support for Z", "html_url": "https://github.com/langchain-ai/langchain/issues/2"}
    ]
    pulls = [
        {"title": "Implement feature Y", "html_url": "https://github.com/langchain-ai/langchain/pull/3"}
    ]
    report_generator.generate_daily_report(repo_name, issues, pulls)
