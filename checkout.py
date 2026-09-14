import json
import os
import shutil    #برای کپی، جابه‌جایی و مدیریت فایل‌ها و پوشه‌ها استفاده می‌شود 


def checkout_commit(commit_id):

    # مسیر فایل commit
    commit_path = f".mygit/commits/{commit_id}.json"

    # بررسی وجود commit
    if not os.path.exists(commit_path):
        print("Commit not found")
        return

    # خواندن اطلاعات commit
    with open(commit_path, "r") as f:
        commit = json.load(f)    # فایل جیسون رو به دیکشنری تبدیل میکنه   ..

    # گرفتن لیست فایل‌های آن commit
    files = commit["files"]

    # برگرداندن تک تک فایل‌ها
    for filepath, file_hash in files.items():

        # مسیر object ذخیره شده
        object_path = os.path.join(
            ".mygit",
            "objects",
            file_hash
        )

        # اگر object وجود نداشت
        if not os.path.exists(object_path):
            print(f"Object not found for {filepath}")
            continue

        # ساخت پوشه مقصد در صورت نیاز
        folder = os.path.dirname(filepath)

        if folder:
            os.makedirs(folder, exist_ok=True)

        # کپی object به فایل اصلی
        shutil.copyfile(object_path, filepath)

    print(f"Checked out commit #{commit_id}")


#_____________________________________
# برای جابه جا شدن برنچ ها 
#_____________________________________

def checkout_branch(branch_name):

    # branch path
    branch_path = f".mygit/branches/{branch_name}"

    # check if branch exists
    if not os.path.exists(branch_path):
        print("Branch not found")
        return

    # read commit ID of branch
    with open(branch_path, "r") as f:
        commit_id = f.read().strip()

    # change HEAD to new branch
    with open(".mygit/HEAD", "w") as f:
        f.write(branch_name)

    # if branch has no commit
    if commit_id == "":
        print(f"Switched to branch '{branch_name}'")
        return

    # restore files of branch's latest commit
    checkout_commit(commit_id)

    print(f"Switched to branch '{branch_name}'")