import os, time

repo_path = input("Enter the path of the git repository: ")
delay = int(input("Enter the delay between commits (in seconds): "))

os.chdir(repo_path)

while True:
    os.system("git commit --allow-empty -m 'update'")
    os.system("git push origin main")
    time.sleep(float(delay))
