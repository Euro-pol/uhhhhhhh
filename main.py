import os, time

repo_path = input("Enter the path of the git repository: ")
delay = float(input("Enter the delay between commits (in seconds): "))

os.chdir(repo_path)

def commit():
    os.system("git commit --allow-empty -m 'update'")
    os.system("git push origin main")

while True:
    commit()
    time.sleep(delay)
