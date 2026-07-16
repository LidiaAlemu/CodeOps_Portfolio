# Day 01 Notes: Terminal & Git Basics

## Five Essential Terminal Commands

1. **`pwd` (Print Working Directory)**
   - Shows your current location in the file system
   - Helps you know exactly where you are before running other commands

2. **`ls` (List)**
   - Displays files and folders in the current directory
   - Use `ls -la` to see hidden files and detailed information

3. **`cd` (Change Directory)**
   - Moves you to a different folder
   - `cd ..` goes up one level, `cd ~` goes to home directory

4. **`mkdir` (Make Directory)**
   - Creates new folders

5. **`cat` (Concatenate)**
   - Displays file contents in the terminal
   - Useful for quickly viewing small files without opening an editor


## Three Essential Git Commands

1. **`git init`**
   - Initializes a new Git repository in your current directory
   - Creates a hidden `.git` folder that tracks all changes
   - Only needed once when starting a new project

2. **`git add`**
   - Stages changes for commit (moves files to the staging area)
   - `git add filename` stages a specific file
   - `git add .` stages all changes in current directory

3. **`git commit`**
   - Saves staged changes permanently to the repository history
   - Always include a meaningful message with `-m "message"`