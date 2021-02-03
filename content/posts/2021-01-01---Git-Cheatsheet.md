---
title: "Git Cheatsheet"
date: "2021-01-01"
template: "post"
draft: false
slug: "git-cheatsheet"
category: "Tools"
tags:
  - "git"
  - "cheatsheet"
  - "advanced"
description: "Tips to enhance your Git workflow."
socialImage: "/media/gutenberg.jpg"
---

While writing software, Version Control is very important. Every software developer must learn to use version control. Git has become the default version control tool, and a software developer can't skip learning this tool.  

This article is intended for readers who have just started using git. Hopefully this helps them in making the git journey more fun.

Mentioning common git commands and aliases below.

## Common Git Commands

### Clone a repository

```sh
git clone <repository_name> <destination_folder>
```

if `<destination_folder>` is not given git creates a new folder with the name of the repo.

The following clones the [official React repo](https://github.com/facebook/react), into the a new folder react into your local machine.

![git-clone](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/5Sex4ntFGqjYT1NPTPyXuzQaZDJbdtqv)

And the following clone the React repo, in the folder called `my-react`.

![git-clone](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/fcom9lpIihWQGhqpQKnWj1M7xl2myG7s)

### To start a new git tracked repo

```sh
mkdir new-project
﻿
git init     # Makes the current directory a git tracked repo

# Add files to the new-project
# Its a good idea to add a 'README.md' file and a '.gitignore' file and then make your first commit.
﻿
# Adds all the files in the current directory
git add .
﻿
# Make your first commit and give a meaningful message
git commit -m "Add README and gitignore"
```

### Configure your git installation

Add your username and email to git config so that git can add them in each that you make.

```sh
git config --global user.name "your_username"
git config --global user.email your_email@example.com
```

Git shows the user details in logs etc.

![git log](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/e93yMczUbrfxO8FpDy3lrCB10fU9n7Q8)

### Making changes in your local and push it to remote repo

```sh
# Make changes in the files

# Check which files has changes
git status
```

![git status](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/j4KZpA218BYXb88M4tJohFa1UNgZk4SN)

```sh
# Add changes to the staging area
git add <file1> <file2>

# Or to add all changes
git add .

# Files in the staging area are shown in green colour
```

![git status](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/Z1AqY60Cyj9ENZgXhxfn1DwaCZy1ukVu)

```sh
 # Commit the changes in the staging area
git commit -m "A meaningful commit message"

# push the changes in the remote repo
git push origin <current_branch_name>
```

### Switch between branches

```sh
git checkout <branch>
```
### Merge your branch in master

```sh
# Switch to master branch
git checkout master
﻿
git merge <your_branch>

# Might have conflicts. Resolve conflicts and then continue merging.

# Check logs to see if the changes have been incorporated
git log

# If everything looks fine, push to remote master
git push origin master
```

### Determine what changes you have made

```sh
git diff <filename>
```

![git diff](https://s3.ap-south-1.amazonaws.com/prd-hc-oj-public-1/public/users/73794b05-fe63-4188-81cd-b6fd35c7aa4e/images/9UU5KQKtF8BQrQ7hP31BVFBU6FzJMcpY)

Additions and deletions are shown by + and - signs, and can be color-coded depending on the shell you use.

## Useful Aliases

Git is a very useful tool, something that developers use multiple times in a
day. Typing git commands can be eased by using aliases to most common commands
like `git status` or `git push`.

Mentioning few useful aliases below. Include them in your `~/.bashrc` file. Your
configuration file may vary depending on your operating system and shell. If you
are using Ubuntu or Mac OS X, `~/.bashrc` is the file you need. If the file
doesn't exist, create the file.

```sh
g=git

# Use: ga README.md .gitignore
ga='git add'

# To add deleted files also
gaa='git add --all'

# Use: gcmsg "Meaningful commit message"
gcmsg='git commit -m'

# To switch to another branch
# Use: gco master
gco='git checkout'

# Use: gd <filename>
gd='git diff'

# Get the list of branches, and you current branch
gb='git branch'

# Use: gc -m "A meaningful message"
gc='git commit -v'
```

Function to get the current branch name.

```sh
function git_current_branch() {  
    local ref  
    ref=$(command git symbolic-ref --quiet HEAD 2> /dev/null)  
    local ret=$?  
    if [[ $ret != 0 ]]; then 
        [[ $ret == 128 ]] && return  # no git repo.  
        ref=$(command git rev-parse --short HEAD 2> /dev/null) || return  
    fi
    echo ${ref#refs/heads/}
}
```

Aliases for `git push` and `git pull`. These save typing a lot of characters, and possible typos. Very useful!

Pull your current branch to remote.

```sh
# Use:
# git checkout <your_branch>
# ggpull  # Get the latest changes from remote

ggpull='git pull origin $(git_current_branch)'
```

Push your current branch to remote. A new branch in remote is created, if already not present.

```sh
# Use: After making commits to your current branch
# ggpush

ggpush='git push origin $(git_current_branch)'
```

Hope this cheatsheet makes your git journey easier.

Happy coding! 😊
