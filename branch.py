import os


def create_branch(branch_name):

    # branch path
    branch_path = f".mygit/branches/{branch_name}"

    # check if branch already exists
    if os.path.exists(branch_path):
        print("Branch already exists")
        return

    # get current branch
    with open(".mygit/HEAD", "r") as f:
        current_branch = f.read().strip()

    # current branch path
    current_branch_path = f".mygit/branches/{current_branch}"

    # get current commit
    with open(current_branch_path, "r") as f:
        current_commit = f.read().strip()

    # create new branch
    with open(branch_path, "w") as f:
        f.write(current_commit)

    print(f"Branch '{branch_name}' created")


def show_branches():

    # get all branches
    branches = os.listdir(".mygit/branches")

    # get current branch
    with open(".mygit/HEAD", "r") as f:
        current_branch = f.read().strip()

    # show branches
    for branch in branches:

        if branch == current_branch:
            print(f"* {branch}")
        else:
            print(f"  {branch}")