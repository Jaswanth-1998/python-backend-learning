Title: Git Handbook — Single Branch (main) Workflow

# Git Handbook — Single Branch (`main`) Workflow

**GitHub:** `Jaswanth-1998`
**Branch:** `main`
**Workflow:** Local → GitHub `main`

---

## 1. Purpose

Use this workflow for small or simple projects where you do not need separate development and testing branches.

There is only one branch:

```text
main
```

Everything happens on `main`:

```text
LOCAL
  ↓
CODE
  ↓
TEST
  ↓
COMMIT
  ↓
PUSH
  ↓
GITHUB main
```

The local `main` branch and GitHub `main` branch should stay synchronized.

---

# 2. First-Time Project Setup

Use these steps only when creating a new project.

---

## Step 1 — Create Your Project

Create your project folder.

Example:

```text
MyProject/
```

Open the folder in VS Code.

---

## Step 2 — Open Terminal

```bash
cd path/to/MyProject
```

---

## Step 3 — Initialize Git

```bash
git init
```

Check:

```bash
git status
```

---

## Step 4 — Create `.gitignore`

For a Python project:

```gitignore
.venv/
venv/
__pycache__/
*.pyc
.env
*.log
.vscode/
.idea/
.pytest_cache/
```

Never commit:

```text
.env
passwords
API keys
tokens
virtual environments
```

---

# 3. Create GitHub Repository

Create a new repository on GitHub.

Example:

```text
GitHub
└── Jaswanth-1998
    └── MyProject
```

If you already initialized Git locally, avoid creating unnecessary files such as another README during repository creation if you want the simplest setup.

---

# 4. Connect Local Project to GitHub

Add the GitHub remote:

```bash
git remote add origin https://github.com/Jaswanth-1998/REPOSITORY_NAME.git
```

Check:

```bash
git remote -v
```

---

# 5. Make Sure Branch Is `main`

Check:

```bash
git branch
```

If the current branch is not `main`:

```bash
git branch -M main
```

Check again:

```bash
git branch
```

Expected:

```text
* main
```

---

# 6. First Commit

Check:

```bash
git status
```

Add files:

```bash
git add .
```

Check what is staged:

```bash
git status
```

Commit:

```bash
git commit -m "Initial project setup"
```

---

# 7. Push First Version to GitHub

```bash
git push -u origin main
```

Now:

```text
LOCAL main
    ↓
GitHub main
```

Your project is connected.

---

# 8. DAILY WORKFLOW

From now on, use this workflow every time you work on the project.

---

## Step 1 — Open Project

```bash
cd path/to/MyProject
```

---

## Step 2 — Check Branch

```bash
git branch
```

Expected:

```text
* main
```

If not:

```bash
git switch main
```

---

## Step 3 — Check Status

```bash
git status
```

You want to understand the current state before doing anything.

Ideally:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## Step 4 — Update Local From GitHub

Before starting work:

```bash
git pull origin main
```

Now:

```text
GitHub main
    ↓
Local main
```

Your local project is up to date.

---

# 9. Write Code

Now work normally.

```text
CODE
 ↓
RUN
 ↓
TEST
 ↓
DEBUG
 ↓
CODE
 ↓
TEST
```

Do not use Git commands every time you save a file.

Work until you reach a logical checkpoint.

---

# 10. Check Changes

When your work is ready:

```bash
git status
```

Then:

```bash
git diff
```

Check what you actually changed.

---

# 11. Stage Changes

```bash
git add .
```

Check:

```bash
git status
```

Review staged changes:

```bash
git diff --staged
```

---

# 12. Commit

Use a meaningful message.

Example:

```bash
git commit -m "Add OCR keyword extraction"
```

Other examples:

```bash
git commit -m "Fix image upload validation"
```

```bash
git commit -m "Update API error handling"
```

```bash
git commit -m "Add PostgreSQL configuration"
```

Avoid:

```bash
git commit -m "update"
```

```bash
git commit -m "changes"
```

```bash
git commit -m "done"
```

---

# 13. Check Local Status

After committing:

```bash
git status
```

Expected:

```text
nothing to commit, working tree clean
```

---

# 14. Push to GitHub

```bash
git push origin main
```

Now:

```text
LOCAL main
    ↓
    PUSH
    ↓
GitHub main
```

---

# 15. Verify

Check:

```bash
git status
```

You want:

```text
Your branch is up to date with 'origin/main'.
```

Then check GitHub and confirm the latest commit/files are there.

---

# 16. Complete Daily Flow

Every working day:

```text
START
  ↓
Open project
  ↓
git switch main
  ↓
git status
  ↓
git pull origin main
  ↓
CODE
  ↓
TEST
  ↓
git status
  ↓
git diff
  ↓
git add .
  ↓
git diff --staged
  ↓
git commit -m "Describe change"
  ↓
git status
  ↓
git push origin main
  ↓
git status
  ↓
DONE
```

---

# 17. Daily Command Cheat Sheet

### Start

```bash
git switch main
git status
git pull origin main
```

### Work

```text
CODE
TEST
DEBUG
```

### Commit

```bash
git status
git diff
git add .
git diff --staged
git commit -m "Describe the change"
```

### Push

```bash
git status
git push origin main
git status
```

---

# 18. If GitHub Was Updated From Another Device

If GitHub has newer code:

```bash
git pull origin main
```

Do not manually copy files from GitHub into your local project.

Git should update your local branch.

---

# 19. If VS Code Shows Old Code

Check:

```bash
git branch
```

Then:

```bash
git status
```

Then:

```bash
git pull origin main
```

Make sure you are actually working on:

```text
main
```

---

# 20. If You Have Uncommitted Changes

Example:

```text
modified: app.py
```

Before pulling, understand what the changes are.

```bash
git status
git diff
```

If the changes are your current work, finish/commit them first.

Do not blindly use:

```bash
git reset --hard
```

because it can delete uncommitted work.

---

# 21. Basic Git Commands

Check status:

```bash
git status
```

Check branch:

```bash
git branch
```

View history:

```bash
git log --oneline
```

View changes:

```bash
git diff
```

View staged changes:

```bash
git diff --staged
```

Update local:

```bash
git pull origin main
```

Push:

```bash
git push origin main
```

---

# 22. Golden Rule

For a single-branch project:

```text
ALWAYS WORK ON main
```

Daily:

```text
PULL
 ↓
CODE
 ↓
TEST
 ↓
COMMIT
 ↓
PUSH
```

The local and GitHub repositories should remain synchronized.

---

# 23. Final Mental Model

Think of GitHub as the remote copy and your computer as the working copy.

```text
             GITHUB
              main
               ▲
               │ push
               │
            LOCAL
             main
               │
               │ pull
               ▼
             GITHUB
```

Your normal cycle is:

```text
GitHub
  ↓ pull
Local
  ↓ code
Local
  ↓ commit
Local
  ↓ push
GitHub
```

**Simple rule:**

```text
PULL → CODE → TEST → COMMIT → PUSH
```
