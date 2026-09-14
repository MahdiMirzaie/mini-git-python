import os
import json


def init_repository():

    # create .mygit folder
    os.makedirs(".mygit", exist_ok =True)

    # create subfolders
    os.makedirs(".mygit/objects", exist_ok=True)
    os.makedirs(".mygit/commits", exist_ok=True)
    os.makedirs(".mygit/branches", exist_ok=True)

    # create index file                  فایل هایی که استیج شدن رو نگه میداره
    with open(".mygit/index.json", "w") as f:
        json.dump({}, f)  # ذخیره ی فایل جیسون

    # create HEAD file
    with open(".mygit/HEAD", "w") as f:
        f.write("main")     # f.write = نوشتن در فایل 

    # create default branch
    with open(".mygit/branches/main", "w") as f:
        f.write("")

    print("Repository initialized successfully")