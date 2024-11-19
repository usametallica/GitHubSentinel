from typing import List, Dict

class ReportGenerator:
    def generate_report(self, updates: List[Dict]) -> str:
        """根据仓库更新生成报告"""
        report = "GitHub Sentinel - 项目更新报告\n"
        for update in updates:
            if isinstance(update, dict):
                repo_name = update.get('repo', {}).get('name', '未知仓库')
                event_type = update.get('type', '未知事件')
                created_at = update.get('created_at', '未知时间')
                report += f"\n仓库: {repo_name}\n事件类型: {event_type}\n更新时间: {created_at}\n"
            else:
                report += "\n错误：获取的更新数据格式不正确。\n"
        return report
