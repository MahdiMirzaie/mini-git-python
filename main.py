import argparse
import os

from Repository import init_repository
from hashing import save_object
from add import add_file
from commit import create_commit
from log import show_log
from checkout import checkout_commit , checkout_branch
from branch import create_branch, show_branches

parser = argparse.ArgumentParser()

parser.add_argument("command")
parser.add_argument("arg", nargs="?")

args = parser.parse_args()

if args.command == "init":

    init_repository()

elif args.command == "hash":

    if not args.arg:
        print("Please enter file name")

    else:

        file_hash = save_object(args.arg)

        print("Hash :", file_hash)

elif args.command == "add":

    if not args.arg:
        print("Please enter file name")

    else:

        add_file(args.arg)

elif args.command == "commit":

    if not args.arg:
        print("Please enter commit message")

    else:

        create_commit(args.arg)


elif args.command == "log":
    show_log()


elif args.command == "branch":
    if args.arg:
        create_branch(args.arg)
    else:
        show_branches()


elif args.command == "checkout":

    if not args.arg:
        print("Please enter commit ID or branch name")

    else:

        branch_path = f".mygit/branches/{args.arg}"

        if os.path.exists(branch_path):
            checkout_branch(args.arg)

        else:
            checkout_commit(args.arg)


elif args.command == "branch":
    if not args.arg:
        print("Please enter branch name")

    else:
        create_branch(args.arg)