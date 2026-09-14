import json
import os


def show_log():

    commit_files = os.listdir(".mygit/commits")

    if len(commit_files) == 0:
        print("No commits found")
        return

    commit_files.sort(
        key=get_commit_number,
        reverse=True
    )

    for commit_file in commit_files:

        path = os.path.join(
            ".mygit/commits",
            commit_file
        )

        with open(path, "r") as f:
            commit = json.load(f)

        print("-" * 40)
        print(f"Commit #{commit['id']}")
        print(f"Message : {commit['message']}")
        print(f"Date : {commit['timestamp']}")
        print("-" * 40)
        print()

# چون اسم فایل ها به صورت شماره ی کامیت ذخیره می شود با این تابع شماره کامیت را از اسم در میاریم 
# for exapmle 6.json 

def get_commit_number(filename):                       

    number = filename.replace(".json", "")

    return int(number)