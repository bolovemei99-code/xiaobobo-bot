# main.py（自动重启保护版）
import time
from forwarder import run

if __name__ == "__main__":
    while True:
        try:
            print("🤖 小波波机器人启动中...")
            run()
        except Exception as e:
            print(f"⚠️ 出错啦：{e}")
            print("⏳ 5 秒后自动重启中...")
            time.sleep(5)
