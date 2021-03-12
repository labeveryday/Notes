# Git Notes

These are my notes on managing a repo through git version control.

Reasons for using GIT

1. Share your code - Collaboration

2. Version Control - Writing code and making a change and then losing or confusing your scripts sucks

3. Backup and store your code remotely.

## Git Command line

| Command                                               | Description                                                                                   |
| -------------                                         |:-------------                                                                                |
| git                                                   | Everything begins with git                                                                    |
| `git help`                                            | Allows you to get help for a specific command  |
| `git config`                                          | Config the tooling                                                                            |
| `git config --global user.name "duan"`                | Configure the user name globally                                                              |
| `git config --global user.email "duan@test.com"`      | Configure the user email globally                                                             |
| `git config --edit --global`                          | Open a file to edit global configs                                                            |
| `git init`                                            | Initialize a git local repo                                                                   |
| `git clone https://github.com/labeveryday/Notes.git`  | Download a project from remote                                                                |
| `git --version`                                       | Check the version of git you are running                                                      |
| `git status`                                          | - Tracking progress - Current Branch - Which files were modified - Next steps                 |
| `git add .`                                           | Recursively add all files to staging                                                          |
| `git commit -m "test"`                                | Commits files with a message                                                                  |
| `git checkout --test.py`                              | Removes a change in working directory before adding to staging                                |
| `git reset HEAD`                                      | Unstages file but retains the most recent changes.                                            |
| `git checkout -b test`                                | Create a new branch and switch to it                                                          |
| `git checkout -d test`                                | Removes a branch                                                                              |
| `git log --all --decorate --oneline -graph`           | For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes                             |
| `git show e38f2b2`                                    | To view more details about a commit                                                           |                                            
| `git diff`                                            | For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes                             |
| `git remote add origin git@github.com:duan/test.git`  | Meaning you can push up and pull down from origin                                             |
| `git push -u origin master`                           | Push your code to repo                                                                        |
| `git log`                                             | Check log                                                                                     |
| `git rebase -i master`                                | To rebase your branch with master                                                             |
| `git merge test_branch`                               | Merge a branch into the main branch                                                           |
