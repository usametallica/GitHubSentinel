import argparse
import threading
import time
import schedule
import requests
from datetime import datetime
from SubscriptionManager import SubscriptionManager
from UpdateRetriever import UpdateRetriever
from NotificationSystem import NotificationSystem
from ReportGenerator import ReportGenerator
from Config import Config

class GitHubSentinel:
    def __init__(self):
        self.subscription_manager = SubscriptionManager()
        self.update_retriever = UpdateRetriever(Config.GITHUB_TOKEN)
        self.notification_system = NotificationSystem()
        self.report_generator = ReportGenerator()

    def fetch_and_notify_updates(self):
        """获取仓库更新并发送通知"""
        updates = []
        for repo_url in self.subscription_manager.get_subscriptions():
            print(f"正在获取仓库 {repo_url} 的最新更新...")
            repo_updates = self.update_retriever.fetch_repo_updates(repo_url)

            # 打印 repo_updates 以进行调试
            print(f"仓库 {repo_url} 更新数据: {repo_updates}")

            # 检查响应数据的类型
            if isinstance(repo_updates, list):
                updates.extend(repo_updates)
            else:
                print("警告：获取的更新数据不是列表，无法处理。")

        if updates:
            report = self.report_generator.generate_report(updates)
            self.notification_system.send_email_notification("GitHub Sentinel - 更新通知", report)
            print("更新已获取并发送通知。")
        else:
            print("未能获取到任何更新。")

    def schedule_updates(self):
        """在后台定期获取更新"""
        if Config.NOTIFICATION_FREQUENCY == "daily":
            schedule.every().day.at("09:00").do(self.fetch_and_notify_updates)
        elif Config.NOTIFICATION_FREQUENCY == "weekly":
            schedule.every().monday.at("09:00").do(self.fetch_and_notify_updates)

        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次

    def start_scheduler(self):
        """启动调度器线程"""
        scheduler_thread = threading.Thread(target=self.schedule_updates, daemon=True)
        scheduler_thread.start()

    def add_subscription(self, repo_url):
        """添加一个 GitHub 仓库订阅"""
        self.subscription_manager.add_subscription(repo_url)
        print(f"已添加仓库 {repo_url} 到订阅列表。")

    def remove_subscription(self, repo_url):
        """移除 GitHub 仓库订阅"""
        self.subscription_manager.remove_subscription(repo_url)
        print(f"已移除仓库 {repo_url}。")

    def list_subscriptions(self):
        """列出所有订阅的仓库"""
        subscriptions = self.subscription_manager.get_subscriptions()
        print("当前订阅的仓库：")
        for repo in subscriptions:
            print(f"- {repo}")

    def run_update(self):
        """立即获取更新并发送报告"""
        self.fetch_and_notify_updates()

    def show_status(self):
        """显示当前工具状态"""
        print(f"当前通知频率：{Config.NOTIFICATION_FREQUENCY}")
        print("定时器正在后台运行，等待执行...")

    def print_help(self):
        """打印帮助信息"""
        print("\n可用命令：")
        print("add <repo_url>    添加一个 GitHub 仓库到订阅列表")
        print("remove <repo_url> 移除一个 GitHub 仓库")
        print("list              查看当前所有订阅的仓库")
        print("update            立即获取所有仓库的最新更新")
        print("status            查看当前工具的状态")
        print("help              查看帮助信息")
        print("report            获取仓库的最新版本信息，格式为：report <repo_url>")
        print("exit              退出工具")

    def get_latest_release_info(self, repo_url):
        """获取 GitHub 仓库的最新版本信息并生成报告"""
        headers = {"Authorization": f"token {Config.GITHUB_TOKEN}"}
        repo_name = "/".join(repo_url.strip("/").split("/")[-2:])
        response = requests.get(f"{Config.GITHUB_API_URL}/repos/{repo_name}/releases/latest", headers=headers)
        
        if response.status_code == 200:
            release_info = response.json()
            report = (
                f"最新版本: {release_info.get('tag_name')}\n"
                f"发布者: {release_info.get('author', {}).get('login')}\n"
                f"发布日期: {release_info.get('published_at')}\n"
                f"发布说明: {release_info.get('body')}\n"
            )
            print(report)
            return report
        else:
            print(f"获取版本信息失败: {response.status_code}")
            return "获取版本信息失败"

    def interactive_mode(self):
        """交互式命令行模式"""
        while True:
            command = input("\n请输入命令：")

            # 处理命令
            if command.startswith("add "):
                repo_url = command[4:]
                self.add_subscription(repo_url)
            elif command.startswith("remove "):
                repo_url = command[7:]
                self.remove_subscription(repo_url)
            elif command == "list":
                self.list_subscriptions()
            elif command == "update":
                self.run_update()
            elif command == "status":
                self.show_status()
            elif command == "help":
                self.print_help()
            elif command.startswith("report "):
                repo_url = command[7:] if len(command) > 7 else input("请输入仓库 URL: ")
                self.get_latest_release_info(repo_url)
            elif command == "exit":
                print("退出工具...")
                break
            else:
                print("无效命令，请重新输入。")
            
            # 每次执行完命令后打印可用命令
            self.print_help()

    def run(self):
        """启动 GitHub Sentinel"""
        self.print_help()  # 启动时打印帮助信息
        self.start_scheduler()  # 启动后台调度任务
        self.interactive_mode()  # 启动命令行交互模式

# 启动项目
if __name__ == "__main__":
    sentinel = GitHubSentinel()
    sentinel.run()
