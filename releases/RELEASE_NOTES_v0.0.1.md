GitHub Sentinel | GitHub 哨兵

GitHub Sentinel is an open-source AI Agent tool designed for developers and project managers to automatically retrieve and summarize the latest updates from GitHub repositories. It helps you stay informed about changes to your favorite or critical projects, without having to manually check each repository.

GitHub 哨兵是一个开源的 AI 代理工具，专为开发者和项目经理设计，能够自动检索并汇总 GitHub 仓库的最新更新。它帮助你及时了解你关注或重要项目的变化，无需手动检查每个仓库。

Key Features | 主要功能:

Subscription Management | 订阅管理: Easily add or remove repository subscriptions to track the projects you care about.
轻松添加或删除仓库订阅，以跟踪你关心的项目。

Update Retrieval | 更新检索: Fetch the latest issues and pull requests on a daily or weekly basis, keeping you up to date。
每天或每周获取最新的 issue 和 pull request，确保你始终保持最新状态。

Report Generation | 报告生成: Summarizes issues and pull requests into formalized daily project reports, providing a clear overview of ongoing activities。
将 issue 和 pull request 汇总为正式的每日项目报告，提供清晰的活动概览。

Notification System | 通知系统: Get notified about significant updates to repositories directly, improving team collaboration。
直接获取仓库的重要更新通知，提升团队协作效率。

GitHub Sentinel is built to enhance project management efficiency by ensuring all team members stay aligned with the latest developments in the open-source projects they follow. The tool includes an interactive command-line interface for immediate updates and integrates with the GPT-4 API for advanced summarization capabilities.

GitHub 哨兵旨在通过确保团队成员了解他们所关注的开源项目的最新进展来提升项目管理效率。该工具包括一个交互式命令行界面，用于即时更新，并与 GPT-4 API 集成以提供高级摘要功能。

Tech Stack | 技术栈:

Python with OpenAI SDK for AI integration.

Markdown report generation for clear and easy-to-share summaries.

Scheduler runs in the background without blocking the tool's I/O operations.

Python 与 OpenAI SDK 集成，用于 AI 功能。

Markdown 报告生成，清晰且易于分享。

调度程序 在后台运行，不会阻塞工具的 I/O 操作。

How to Use GitHub Sentinel | 如何使用 GitHub 哨兵:

Clone the Repository | 克隆仓库:

git clone https://github.com/yourusername/GitHubSentinel.git
cd GitHubSentinel

Install Dependencies | 安装依赖:
Make sure you have Python installed. Then, install the required Python packages:
确保你已安装 Python。然后，安装所需的 Python 包：

pip install -r requirements.txt

Set Up Environment Variables | 设置环境变量:
Create a .env file in the root directory or set up system environment variables for sensitive information like GITHUB_TOKEN and EMAIL_PASSWORD.
在根目录中创建 .env 文件，或设置系统环境变量来保存 GITHUB_TOKEN 和 EMAIL_PASSWORD 等敏感信息。

GITHUB_API_URL=https://api.github.com
GITHUB_TOKEN=your_github_token
EMAIL_SMTP_SERVER=mail.example.com
EMAIL_FROM=your_email@example.com
EMAIL_TO=recipient_email@example.com
EMAIL_PASSWORD=your_email_password
NOTIFICATION_FREQUENCY=daily

Run the Tool | 运行工具:
To start retrieving updates and generating reports, run the following command:
要开始检索更新并生成报告，运行以下命令：

python GitHubSentinel.py

Interactive Commands | 交互命令:

Add a Subscription | 添加订阅: You can add a repository to track by running:
你可以通过运行以下命令来添加一个要跟踪的仓库：

python GitHubSentinel.py add-repo owner/repository_name

Remove a Subscription | 删除订阅: To remove a repository from tracking:
要从跟踪中移除一个仓库：

python GitHubSentinel.py remove-repo owner/repository_name

Fetch Immediate Updates | 立即获取更新: To fetch updates immediately instead of waiting for the scheduler:
要立即获取更新，而不是等待调度程序：

python GitHubSentinel.py fetch-updates

View Reports | 查看报告:
Reports are generated in Markdown format and saved in the reports/ directory, named by project and date for easy reference.
报告以 Markdown 格式生成，并保存在 reports/ 目录中，按项目和日期命名，便于参考。

Create Git Tag and Release | 创建 Git 标签和发布

To create a versioned release of the current code as v0.0.1, follow these steps:
要创建当前代码的版本发布为 v0.0.1，请按以下步骤操作：

Commit All Changes (if any) | 提交所有更改（如果有）:

git add .
git commit -m "Prepare for v0.0.1 release"

Tag the Release | 打标签:

git tag -a v0.0.1 -m "Initial release v0.0.1"

Push the Tag to GitHub | 推送标签到 GitHub:

git push origin v0.0.1

Create a Release Note | 创建发布说明:

Go to your GitHub repository page.

Click on the Releases tab.

Click Draft a new release.

In the Tag version field, select v0.0.1.

Enter the Release title as v0.0.1.

In the Description field, add the following release notes:
在 描述 字段中，添加以下发布说明：

### GitHub Sentinel v0.0.1
- Initial release of GitHub Sentinel.
- Features include:
  - Subscription management for GitHub repositories.
  - Automated update retrieval (issues and pull requests).
  - Daily or weekly Markdown report generation.
  - Interactive command-line interface for managing subscriptions and fetching updates.
### GitHub 哨兵 v0.0.1
- GitHub 哨兵的初始版本。
- 包含的功能：
  - GitHub 仓库的订阅管理。
  - 自动检索更新（issues 和 pull requests）。
  - 每日或每周 Markdown 报告生成。
  - 交互式命令行界面，用于管理订阅和获取更新。

Click Publish release。

点击 发布。

Deploy Local Code to Your GitHub Account | 将本地代码部署到你的 GitHub 账号

To deploy the locally created GitHub Sentinel code to your own GitHub account, follow these steps:
要将本地创建的 GitHub Sentinel 代码部署到你自己的 GitHub 账号，请按以下步骤操作：

Initialize a Git Repository | 初始化 Git 仓库:
If you haven't already initialized the repository, run:
如果还没有初始化仓库，运行以下命令：

git init

Add Remote Origin | 添加远程仓库地址:
Add the link to your GitHub repository as the remote origin. Replace yourusername and GitHubSentinel with your actual GitHub username and repository name.
添加你 GitHub 仓库的链接作为远程地址。将 yourusername 和 GitHubSentinel 替换为你的 GitHub 用户名和仓库名。

git remote add origin https://github.com/yourusername/GitHubSentinel.git

Add Files and Commit | 添加文件并提交:
Add all files to the staging area and commit them.
将所有文件添加到暂存区并提交。

git add .
git commit -m "Initial commit"

Push to GitHub | 推送到 GitHub:
Push the committed changes to the remote GitHub repository.
将提交的更改推送到远程 GitHub 仓库。

git push -u origin main

If your default branch is master, replace main with master.
如果你的默认分支是 master，请将 main 替换为 master。

Create Repository on GitHub | 在 GitHub 上创建仓库:

Go to GitHub and log in.

Click on the New button to create a new repository.

Name the repository GitHubSentinel.

Do not initialize with a README, since you have local files to push.

Push Tags and Releases | 推送标签和发布:
If you have created tags, push them as well.
如果你创建了标签，也将它们推送到远程：

git push origin --tags

By following these steps, you will have successfully deployed the GitHub Sentinel code to your GitHub account.
按照这些步骤操作，你将成功地将 GitHub Sentinel 代码部署到你的 GitHub 账号上。

Contribute to GitHub Sentinel and help shape the future of AI-driven project management tools!
参与 GitHub 哨兵项目，帮助塑造 AI 驱动的项目管理工具的未来！

