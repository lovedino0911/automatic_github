import os
import time
from datetime import datetime

REPO_PATH = r"C:\Users\edan0\OneDrive\coding"  # Git 저장소 경로
INTERVAL = 3600  # 1시간 = 3600초

while True:
    os.chdir(REPO_PATH)
    os.system("git add .")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit -m "Auto-commit at {now}"')
    os.system("git push origin main")
    print(f"[{now}] 커밋 및 푸시 완료")
    time.sleep(INTERVAL)
