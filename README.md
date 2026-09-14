# Mini Git

A lightweight Git-like version control system implemented from scratch in Python.

## Overview

Mini Git is an educational implementation of core version control concepts, designed to explore how Git manages file versions, objects, commits, branches, and repository state at a lower level.

The project was built without using GitPython or Dulwich, with the core functionality implemented using Python's standard library.

## Key Features

- Repository initialization
- SHA-1 based file hashing
- Content-based object storage
- Staging area management
- Commit creation and history
- Branch creation and management
- Commit checkout and file restoration
- Command-line interface

## Architecture

```text
Working Files
      │
      ▼
   SHA-1 Hash
      │
      ▼
Object Storage
      │
      ▼
 Staging Area
      │
      ▼
   Commit
      │
      ├──────► Branch
      │
      ▼
  Checkout
```
Repository metadata and version information are stored locally inside a .mygit directory .

## Tech Stack
- Python 3
- hashlib
- argparse
- os
- json
- shutil
- datetime

## Example
- py main.py init
- py main.py add test.txt
- py main.py commit "Initial commit"
- py main.py log
- py main.py branch feature
- py main.py checkout 1

## Project Structure
```
mini-git-python/
├── main.py
├── Repository.py
├── hashing.py
├── add.py
├── commit.py
├── log.py
├── branch.py
├── checkout.py
└── Mini Version Control System---.pdf
```

## What I Learned
- Git and version control fundamentals
- Hash-based content identification
- File and directory management in Python
- JSON-based data persistence
- Command-line application design
- Modular Python project architecture
- Commit and branch management concepts
- Documentation

The complete technical report is available in :

Mini Version Control System---.pdf  
The report includes the project architecture, implementation details, testing process, and references.

## Author

**Mahdi Mirzaie**  
Computer Science Student
