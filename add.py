import json

from hashing import save_object


def add_file(filepath):

    # save object and get hash
    file_hash = save_object(filepath)

    # load current index
    with open(".mygit/index.json", "r") as f:
        index = json.load(f)     # فایل جیسون را به یک دیکشنری پایتون تبدیل می کند ...

    # add file to staging area
    index[filepath] = file_hash

    # save updated index
    with open(".mygit/index.json", "w") as f:
        json.dump(index, f, indent=4)

    print(f"{filepath} added successfully")


