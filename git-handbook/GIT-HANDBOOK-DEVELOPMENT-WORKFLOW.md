Title: Git Handbook — Development, Testing & Main Branch Workflow

# Git Handbook — Development, Testing & Main Branch Workflow

**GitHub:** `Jaswanth-1998`
**Branches:** `development`, `testing`, `main`
**Workflow:** `development → testing → main`

---

# 1. Purpose

Use this workflow for projects where you want separate stages for:

```text
development = Coding
testing     = Testing / Validation
main        = Stable / Production
```

The overall flow is:

```text
                 GitHub
                   │
                   ▼
             ┌──────────┐
             │   main   │
             └────▲─────┘
                  │
                  │ PR
                  │
             ┌────┴─────┐
             │ testing  │
             └────▲─────┘
                  │
                  │ PR
                  │
             ┌────┴────────┐
             │ development │
             └─────────────┘
                   ▲
                   │
                LOCAL
```

Daily coding happens on:

```text
development
```

---

# 2. Branch Responsibilities

## `development`

Use for:

```text
New features
Code changes
Bug fixes
Refactoring
Experiments
```

This is your main working branch.

---

## `testing`

Use for:

```text
Integration
Testing
Validation
Bug verification
Release preparation
```

---

## `main`

Use for:

```text
Stable code
Production-ready code
Final version
```

Do not directly develop on `main`.

---

# 3. First-Time Project Setup

Use these steps only when creating the repository.

---

# Step 1 — Create Project

Create your project locally.

Example:

```text
MyProject/
```

Open it in VS Code.

---

# Step 2 — Initialize Git

```bash
cd path/to/MyProject
git init
```

Check:

```bash
git status
```

---

# Step 3 — Create `.gitignore`

For Python:

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

# 4. Create GitHub Repository

Create the repository under:

```text
Jaswanth-1998
```

Example:

```text
GitHub
└── Jaswanth-1998
    └── MyProject
```

---

# 5. Connect Local to GitHub

```bash
git remote add origin https://github.com/Jaswanth-1998/REPOSITORY_NAME.git
```

Check:

```bash
git remote -v
```

---

# 6. Create `main`

Make sure the default branch is:

```text
main
```

Check:

```bash
git branch
```

If necessary:

```bash
git branch -M main
```

---

# 7. First Commit

```bash
git status
git add .
git status
git commit -m "Initial project setup"
```

---

# 8. Push `main`

```bash
git push -u origin main
```

Now GitHub has:

```text
main
```

---

# 9. Create `development`

Create the development branch from main:

```bash
git switch -c development
```

Push it:

```bash
git push -u origin development
```

Now:

```text
GitHub

main
development
```

---

# 10. Create `testing`

Switch to main:

```bash
git switch main
```

Create testing:

```bash
git switch -c testing
```

Push:

```bash
git push -u origin testing
```

Now:

```text
GitHub

main
testing
development
```

Return to development:

```bash
git switch development
```

---

# 11. Final Branch Structure

You now have:

```text
main
testing
development
```

The intended direction is:

```text
development
     ↓
    PR
     ↓
testing
     ↓
    PR
     ↓
main
```

---

# 12. DAILY WORKFLOW

This is the workflow to follow every time you start working.

---

# Step 1 — Open Project

```bash
cd path/to/MyProject
```

---

# Step 2 — Go to Development

```bash
git switch development
```

Check:

```bash
git branch
```

Expected:

```text
* development
  main
  testing
```

---

# Step 3 — Check Status

```bash
git status
```

Understand what Git is telling you.

Ideally:

```text
nothing to commit, working tree clean
```

---

# Step 4 — Update Local Development

```bash
git pull origin development
```

Now:

```text
GitHub development
        ↓
Local development
```

Your local development branch is synchronized.

---

# 13. Write Code

Now work only on:

```text
development
```

Example:

```text
Add feature
 ↓
Run application
 ↓
Test
 ↓
Find bug
 ↓
Fix bug
 ↓
Test again
```

---

# 14. Check Your Changes

When your work is ready:

```bash
git status
```

Then:

```bash
git diff
```

Review the actual changes.

---

# 15. Stage

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

# 16. Commit

Example:

```bash
git commit -m "Add OCR keyword extraction"
```

Other examples:

```bash
git commit -m "Fix invoice amount extraction"
```

```bash
git commit -m "Add image validation"
```

```bash
git commit -m "Improve API error handling"
```

---

# 17. Verify Local Development

```bash
git status
```

Expected:

```text
nothing to commit, working tree clean
```

Check latest commit:

```bash
git log -1
```

---

# 18. Push Development

```bash
git push origin development
```

Now:

```text
LOCAL development
       ↓
     PUSH
       ↓
GITHUB development
```

---

# 19. Create Pull Request

Go to GitHub.

Create:

```text
development → testing
```

Review the changed files.

Then merge the PR.

---

# 20. Update Local Testing

After the PR is merged, your GitHub `testing` branch contains the new code.

Your local `testing` branch may still be old.

Update it:

```bash
git switch testing
git pull origin testing
```

Now:

```text
GitHub testing
      ↓
Local testing
```

---

# 21. Test

Run the project's testing procedure.

For example:

```bash
pytest
```

Or:

```bash
uvicorn app:app --reload
```

Then manually test the application if required.

---

# 22. If Testing Fails

Do not directly edit `testing` unless you intentionally use that workflow.

Normally:

```text
testing problem
      ↓
switch development
      ↓
fix code
      ↓
commit
      ↓
push development
      ↓
PR development → testing
      ↓
test again
```

Example:

```bash
git switch development
git pull origin development
```

Fix the problem.

Then:

```bash
git status
git diff
git add .
git commit -m "Fix OCR validation issue"
git push origin development
```

Create another:

```text
development → testing
```

PR.

---

# 23. When Testing Passes

When everything is working correctly:

```text
testing = stable
```

Create the second Pull Request:

```text
testing → main
```

Review.

Merge.

Now:

```text
development
     ↓
testing
     ↓
main
```

---

# 24. Update Local Main

After merging testing → main, your local `main` branch may still be old.

If you need the updated main locally:

```bash
git switch main
git pull origin main
```

Now:

```text
GitHub main
    ↓
Local main
```

---

# 25. Return to Development

After updating main:

```bash
git switch development
git pull origin development
```

Continue your next development task.

Your normal working branch is:

```text
development
```

---

# 26. Complete Daily Cycle

```text
START
  ↓
git switch development
  ↓
git status
  ↓
git pull origin development
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
git push origin development
  ↓
GitHub PR
  ↓
development → testing
  ↓
Update local testing
  ↓
TEST
  ↓
If successful
  ↓
GitHub PR
  ↓
testing → main
  ↓
Update local main if needed
  ↓
git switch development
  ↓
Next task
```

---

# 27. Daily Command Cheat Sheet

## Start Work

```bash
git switch development
git status
git pull origin development
```

## Work

```text
CODE
TEST
DEBUG
```

## Prepare Commit

```bash
git status
git diff
git add .
git status
git diff --staged
```

## Commit

```bash
git commit -m "Describe the change"
```

## Push

```bash
git status
git push origin development
git status
```

## GitHub

```text
development → testing
```

## Local Testing

```bash
git switch testing
git pull origin testing
```

## After Testing

GitHub:

```text
testing → main
```

## Update Local Main

```bash
git switch main
git pull origin main
```

## Return to Development

```bash
git switch development
git pull origin development
```

---

# 28. Branch Switching Rules

Before switching branches:

```bash
git status
```

If you have important uncommitted work:

```text
STOP
```

Do not blindly switch.

Finish the work, commit it, or intentionally stash it.

---

# 29. Never Directly Develop on Main

Avoid:

```bash
git switch main
# edit code
git add .
git commit
git push
```

Instead:

```text
development
    ↓
    PR
testing
    ↓
    PR
main
```

---

# 30. Keep Local Branches Updated

Remember:

```text
GitHub development
       ≠
Local development
```

until you pull.

Same for:

```text
GitHub testing
       ≠
Local testing
```

and:

```text
GitHub main
       ≠
Local main
```

Use:

```bash
git pull origin development
```

```bash
git pull origin testing
```

```bash
git pull origin main
```

as appropriate.

---

# 31. Important: A PR Does Not Automatically Update Every Local Branch

Example:

You merge:

```text
development → testing
```

on GitHub.

That does NOT mean your local `testing` branch automatically changes.

You must run:

```bash
git switch testing
git pull origin testing
```

Likewise, after:

```text
testing → main
```

update local main:

```bash
git switch main
git pull origin main
```

---

# 32. Git Status — Your First Debugging Tool

Whenever something looks wrong:

```bash
git status
```

Then:

```bash
git branch
```

Then:

```bash
git log --oneline --graph --decorate --all
```

These commands tell you where you are and what Git knows.

---

# 33. If Local Development Is Behind GitHub

You may see:

```text
Your branch is behind 'origin/development'
```

Run:

```bash
git pull origin development
```

---

# 34. If Local Development Is Ahead

You may see:

```text
Your branch is ahead of 'origin/development'
```

If the commits are intended:

```bash
git push origin development
```

---

# 35. If Branches Have Diverged

You may see:

```text
Your branch and 'origin/development' have diverged
```

STOP.

Do not immediately use:

```bash
git push --force
```

Inspect:

```bash
git status
git branch -vv
git fetch origin
git log --oneline --graph --decorate --all
```

Understand the situation before changing history.

---

# 36. Important Commands

Check current branch:

```bash
git branch
```

Check status:

```bash
git status
```

Switch branch:

```bash
git switch development
```

Pull:

```bash
git pull origin development
```

View changes:

```bash
git diff
```

Stage:

```bash
git add .
```

View staged changes:

```bash
git diff --staged
```

Commit:

```bash
git commit -m "message"
```

Push:

```bash
git push origin development
```

History:

```bash
git log --oneline
```

Full branch graph:

```bash
git log --oneline --graph --decorate --all
```

---

# 37. Emergency Rule

When Git gives an unexpected result:

```text
STOP
 ↓
git status
 ↓
git branch
 ↓
git fetch origin
 ↓
git branch -vv
 ↓
git log --oneline --graph --decorate --all
 ↓
UNDERSTAND
 ↓
THEN ACT
```

Do not use random Git commands.

Especially avoid blindly using:

```bash
git reset --hard
```

or:

```bash
git push --force
```

These can destroy work or rewrite history.

---

# 38. Professional Commit Examples

Use:

```text
Add OCR keyword extraction
Fix invoice amount extraction
Add image upload validation
Update PostgreSQL configuration
Improve API error handling
Refactor OCR processing
Remove unused utility
Add request validation
Update project documentation
```

Avoid:

```text
update
changes
final
done
test
asdf
```

---

# 39. Final Branch Model

Your repository should look like:

```text
                    ┌──────────┐
                    │   main   │
                    │  STABLE  │
                    └────▲─────┘
                         │
                         │ PR
                         │
                    ┌────┴─────┐
                    │ testing  │
                    │  VERIFY  │
                    └────▲─────┘
                         │
                         │ PR
                         │
                 ┌───────┴────────┐
                 │  development   │
                 │     CODE       │
                 └────────────────┘
                         ▲
                         │
                       LOCAL
```

---

# 40. Golden Rule

Your normal development cycle is:

```text
PULL
 ↓
CODE
 ↓
TEST
 ↓
DIFF
 ↓
ADD
 ↓
COMMIT
 ↓
PUSH
 ↓
PR
 ↓
TEST
 ↓
PR
 ↓
MAIN
```

Remember:

```text
development = I work here
testing     = I verify here
main        = I release here
```

---

# 41. Final Mental Model

Think of the branches as three environments:

```text
┌────────────────────────────────────┐
│ DEVELOPMENT                        │
│ "I am building it."                │
└────────────────┬───────────────────┘
                 │
                 │ Pull Request
                 ▼
┌────────────────────────────────────┐
│ TESTING                            │
│ "I am verifying it."               │
└────────────────┬───────────────────┘
                 │
                 │ Pull Request
                 ▼
┌────────────────────────────────────┐
│ MAIN                               │
│ "This is the stable version."      │
└────────────────────────────────────┘
```

For local work:

```text
START
 ↓
Local development
 ↓
Pull latest
 ↓
Code
 ↓
Commit
 ↓
Push
 ↓
GitHub development
 ↓
PR
 ↓
GitHub testing
 ↓
Local testing (when needed)
 ↓
Test
 ↓
PR
 ↓
GitHub main
 ↓
Local main (when needed)
 ↓
Back to development
```

**The most important rule:**

```text
DO NOT ASK:
"What Git command should I run?"

FIRST ASK:
"Which branch am I on?"
"Is my local branch updated?"
"What does git status say?"
"What changed?"

THEN run the command.
```
