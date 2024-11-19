import smtplib
from Config import Config
from email.mime.text import MIMEText
from email.header import Header
import time

class NotificationSystem:
    def __init__(self):
        self.connect_to_smtp()

    def connect_to_smtp(self):
        """连接到 SMTP 服务器"""
        try:
            self.email_server = smtplib.SMTP(Config.EMAIL_SMTP_SERVER, 25, timeout=60)  # 使用端口25，无需 TLS
            self.email_server.login(Config.EMAIL_FROM, Config.EMAIL_PASSWORD)  # 使用环境变量中的邮箱密码
            print("成功连接到 SMTP 服务器。")
        except Exception as e:
            print(f"连接到 SMTP 服务器失败: {e}")

    def send_email_notification(self, subject: str, message: str):
        """发送电子邮件通知，添加重试机制"""
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = Header(Config.EMAIL_FROM, 'utf-8')
        msg['To'] = Header(Config.EMAIL_TO, 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')

        max_retries = 3
        for attempt in range(max_retries):
            try:
                # 检查 SMTP 连接是否正常
                if self.email_server.noop()[0] != 250:
                    print("SMTP 连接已关闭，重新连接中...")
                    self.connect_to_smtp()

                self.email_server.sendmail(Config.EMAIL_FROM, [Config.EMAIL_TO], msg.as_string())
                print("邮件已成功发送。")
                break
            except Exception as e:
                print(f"邮件发送失败: {e}")
                if attempt < max_retries - 1:
                    print("重试中...")
                    time.sleep(10)  # 等待 10 秒后重试
                else:
                    print("多次尝试后仍无法发送邮件，放弃。")

    def __del__(self):
        """关闭 SMTP 连接"""
        try:
            self.email_server.quit()
        except Exception as e:
            print(f"关闭 SMTP 连接失败: {e}")
