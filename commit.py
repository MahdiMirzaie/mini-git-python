import json
import os
from datetime import datetime


def create_commit(message):

    # load staging area
    with open(".mygit/index.json", "r") as f:
        index = json.load(f)

    # if nothing added
    if len(index) == 0:
        print("Nothing to commit")
        return

    # determine next commit id
    commit_files = os.listdir(".mygit/commits")    #تمام فایل‌های داخل پوشه را برمی‌گرداند


# شماره کامیت بعدی رو طبق کامیت های قبلی میزاریم مثلا 4 تا کامیت داریم شماره کامیت بعدی = 5 
    commit_id = len(commit_files) + 1       
    commit_data = {
        "id": commit_id,
        "message": message,
        "timestamp": str(datetime.now()),
        "files": index
    }

    commit_path = f".mygit/commits/{commit_id}.json"

    with open(commit_path, "w") as f:
        json.dump(commit_data, f, indent=4)

        # clear staging area
    with open(".mygit/index.json", "w") as f:
        json.dump({}, f, indent=4)

    print(f"Commit #{commit_id} created")

        # get current branch
    with open(".mygit/HEAD", "r") as f:
        current_branch = f.read().strip()

    # update current branch
    branch_path = f".mygit/branches/{current_branch}"

    with open(branch_path, "w") as f:
        f.write(str(commit_id))