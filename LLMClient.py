# LLMClient.py
import openai
import os
from Config import Config

class LLMClient:
    def __init__(self):
        """初始化 LLMClient"""
        self.api_key = Config.OPENAI_API_KEY
        openai.api_key = self.api_key

    def summarize_issues_and_pulls(self, issues: list, pulls: list) -> str:
        """调用 GPT-4 API 对 issues 和 pull requests 进行总结"""
        prompt = self.generate_prompt(issues, pulls)
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        summary = response['choices'][0]['text'].strip()
        return summary

    def generate_prompt(self, issues: list, pulls: list) -> str:
        """生成用于 GPT-4 的提示"""
        prompt = "Please summarize the following GitHub issues and pull requests:\n\n"
        prompt += "### Issues:\n"
        for issue in issues:
            issue_body = issue.get('body') or 'No description provided.'
            prompt += f"- {issue.get('title')}: {issue_body[:200]}\n"

        prompt += "\n### Pull Requests:\n"
        for pull in pulls:
            pull_body = pull.get('body') or 'No description provided.'
            prompt += f"- {pull.get('title')}: {pull_body[:200]}\n"

        return prompt

# Example usage
if __name__ == "__main__":
    llm_client = LLMClient()
    issues = [
        {"title": "Bug fix in module X", "body": "This PR fixes a critical bug in module X that caused Y."},
        {"title": "New feature: Add support for Z", "body": "This issue proposes adding support for Z."}
    ]
    pulls = [
        {"title": "Implement feature Y", "body": "This pull request implements feature Y, which allows users to do X."}
    ]
    summary = llm_client.summarize_issues_and_pulls(issues, pulls)
    print("Summary:\n", summary)
