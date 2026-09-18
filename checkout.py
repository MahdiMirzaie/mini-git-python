import json
import os
import shutil    #برای کپی، جابه‌جایی و مدیریت فایل‌ها و پوشه‌ها استفاده می‌شود 


def checkout_commit(commit_id, old_commit_id=None):

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

    # _____________________________________
    # حذف فایل‌هایی که در commit جدید وجود ندارند
    # _____________________________________

    # اگر Commit قبلی از بیرون داده نشده باشد
    if old_commit_id is None:

        with open(".mygit/HEAD", "r") as f:
            current_branch = f.read().strip()

        branch_path = f".mygit/branches/{current_branch}"

        if os.path.exists(branch_path):

            with open(branch_path, "r") as f:
                old_commit_id = f.read().strip()

    # بررسی Commit قبلی
    if old_commit_id != "" and old_commit_id is not None:
        
        if old_commit_id != str(commit_id):

            old_commit_path = f".mygit/commits/{old_commit_id}.json"

            if os.path.exists(old_commit_path):

                with open(old_commit_path, "r") as f:
                    old_commit = json.load(f)

                old_files = old_commit["files"]

                for filepath in old_files:

                    if filepath not in files and os.path.exists(filepath):
                        os.remove(filepath)

    # _____________________________________
    # به روز کردن index مطابق commit جدید
    # _____________________________________

    with open(".mygit/index.json", "w") as f:
        json.dump(files, f, indent=4)

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

    # read current branch
    with open(".mygit/HEAD", "r") as f:
        current_branch = f.read().strip()

    # read old commit ID
    old_branch_path = f".mygit/branches/{current_branch}"

    old_commit_id = ""

    if os.path.exists(old_branch_path):

        with open(old_branch_path, "r") as f:
            old_commit_id = f.read().strip()

    # if branch has no commit
    if commit_id == "":

        # حذف فایل‌های Commit قبلی
        if old_commit_id != "":

            old_commit_path = f".mygit/commits/{old_commit_id}.json"

            if os.path.exists(old_commit_path):

                with open(old_commit_path, "r") as f:
                    old_commit = json.load(f)

                old_files = old_commit["files"]

                for filepath in old_files:

                    if os.path.exists(filepath):
                        os.remove(filepath)

        # خالی کردن index
        with open(".mygit/index.json", "w") as f:
            json.dump({}, f, indent=4)

        # change HEAD to new branch
        with open(".mygit/HEAD", "w") as f:
            f.write(branch_name)

        print(f"Switched to branch '{branch_name}'")
        return

    # restore files of branch's latest commit
    checkout_commit(commit_id, old_commit_id)

    # change HEAD to new branch
    with open(".mygit/HEAD", "w") as f:
        f.write(branch_name)

    print(f"Switched to branch '{branch_name}'")