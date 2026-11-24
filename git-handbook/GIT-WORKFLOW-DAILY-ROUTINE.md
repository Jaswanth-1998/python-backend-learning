# Git Workflow – Office Computer ↔ Personal Computer

**Repository\:** `ModeAlpha`
**Branch\:** `main`
**GitHub\:** [https\://github.com/Jaswanth-1998/ModeAlpha](https://github.com/Jaswanth-1998/ModeAlpha)

## 1\. Initial Setup – Personal Computer

(One-time setup)

Your project already exists on your personal computer.

Open terminal inside the project folder\:

```
cd ModeAlpha
```

Initialize Git\:

```
git init
```

Create main branch\:

```
git branch -M main
```

Connect GitHub repository\:

```
git remote add origin https://github.com/Jaswanth-1998/ModeAlpha.git
```

Add and commit project files\:

```
git add .
git commit -m "Initial project upload"
```

Push to GitHub\:

```
git push -u origin main
```

---

## 2\. Initial Setup – Office Computer

(One-time setup)

Open terminal in your project storage folder\:

```
git clone https://github.com/Jaswanth-1998/ModeAlpha.git
```

Enter the project\:

```
cd ModeAlpha
```

Now your project is available on the office computer.

---

## 3\. Daily Workflow – Office Computer

(Every working day)

**Start working**

```
cd ModeAlpha
git pull origin main
```

**Do your coding.**

**Finish working**

```
git add .
git commit -m "Office updates"
git push origin main
```

---

## 4\. GitHub – Main Branch

**GitHub – ModeAlpha**

(main branch)

Central repository – stores the latest committed and pushed code.

---

## 5\. Daily Workflow – Personal Computer

(Every working day)

**Start working**

```
cd ModeAlpha
git pull origin main
```

**Do your coding.**

**Finish working**  

```
git add .
git commit -m "Personal updates"
git push origin main
```

---

## 6\. Next Working Day – Office Computer

Get personal computer updates\:

```
cd ModeAlpha
git pull origin main
```

Continue coding.

Finish working\:

```
git add .
git commit -m "Office updates"
git push origin main
```

---

## Complete workflow diagram

**Office Computer**

Pull → Coding → Add → Commit → Push

**GitHub – main**

Central repository

**Personal Computer**

Pull → Coding → Add → Commit → Push

Repeat the same workflow

## 7\. Important Rules

1. Clone only once on each computer.
2. Always pull before starting work.
3. Always commit and push after finishing work.
4. Push from one computer before switching to the other.
5. Never use `git clone` again if the project folder already exists.
6. If you have uncommitted changes, commit or safely stash them before pulling.

**Your daily routine is simply\:**

```
git pull origin main

# Do your coding

git add .
git commit -m "Your updates"
git push origin main
```

Use the same four commands on both computers.
