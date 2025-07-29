import os
from datetime import datetime

REPO_PATH = r"C:\Users\edan0\OneDrive\coding" 

os.chdir(REPO_PATH) 

os.system("git add .")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
os.system(f'git commit -m "Auto-commit at {now}"')

os.system("git push origin main")

print(f"[{now}] 커밋 및 푸시 완료")
     