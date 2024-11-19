GitHub Sentinel | GitHub 哨兵

GitHub Sentinel is an open-source AI Agent tool designed for developers and project managers to automatically retrieve and summarize the latest updates from GitHub repositories. It helps you stay informed about changes to your favorite or critical projects, without having to manually check each repository.

GitHub 哨兵是一个开源的 AI 代理工具，专为开发者和项目经理设计，能够自动检索并汇总 GitHub 仓库的最新更新。它帮助你及时了解你关注或重要项目的变化，无需手动检查每个仓库。

Key Features | 主要功能

Subscription Management | 订阅管理: Easily add or remove repository subscriptions to track the projects you care about.

Update Retrieval | 更新检索: Fetch the latest issues and pull requests on a daily or weekly basis, keeping you up to date.

Report Generation | 报告生成: Summarizes issues and pull requests into formalized daily project reports, providing a clear overview of ongoing activities.

Notification System | 通知系统: Get notified about significant updates to repositories directly, improving team collaboration.

GitHub Sentinel is built to enhance project management efficiency by ensuring all team members stay aligned with the latest developments in the open-source projects they follow. The tool includes an interactive command-line interface for immediate updates and integrates with the GPT-4 API for advanced summarization capabilities.

GitHub 哨兵旨在通过确保团队成员了解他们所关注的开源项目的最新进展来提升项目管理效率。该工具包括一个交互式命令行界面，用于即时更新，并与 GPT-4 API 集成以提供高级摘要功能。

Tech Stack | 技术栈

Python with OpenAI SDK for AI integration.

Markdown report generation for clear and easy-to-share summaries.

Scheduler runs in the background without blocking the tool's I/O operations.

How to Use GitHub Sentinel | 如何使用 GitHub 哨兵

Clone the Repository | 克隆仓库:

git clone https://github.com/usametallica/GitHubSentinel.git
cd GitHubSentinel

Install Dependencies | 安装依赖:

pip install -r requirements.txt

Set Up Environment Variables | 设置环境变量:
Create a .env file in the root directory:

GITHUB_API_URL=https://api.github.com
GITHUB_TOKEN=your_github_token_placeholder
EMAIL_SMTP_SERVER=mail.example.com
EMAIL_FROM=usametallica@gmail.com
EMAIL_TO=recipient_email@example.com
EMAIL_PASSWORD=your_email_password_placeholder
NOTIFICATION_FREQUENCY=daily

Run the Tool | 运行工具:

python GitHubSentinel.py

Release Notes | 发布说明

Version v0.0.1

Initial release of GitHub Sentinel.

Features include:

Subscription management for GitHub repositories.

Automated update retrieval (issues and pull requests).

Daily or weekly Markdown report generation.

Interactive command-line interface for managing subscriptions and fetching updates.

中文发布说明

版本 v0.0.1

GitHub 哨兵的初始版本。

包含的功能：

GitHub 仓库的订阅管理。

自动检索更新（issues 和 pull requests）。

每日或每周 Markdown 报告生成。

交互式命令行界面，用于管理订阅和获取更新。

License

MIT License

Contributing | 贡献

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

Contact | 联系

For any inquiries, please contact [usametallica@gmail.com].

