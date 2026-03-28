# Basic Linux + Treasure Hunt

> **Audience:** Classroom beginners + HPC onboarding (SDSC Expanse)  
> **Goal:** Build confidence in the terminal: create files/directories, navigate with `cd`, use **absolute** & **relative** paths, and edit text with **nano**.

This exercise is intended to help you achieve the following learning objective:
* Navigate directories, organize files, and execute programs on a command-line terminal.

---

## HPC context

On SDSC Expanse (and most clusters), you’ll often:

- log in to a **login node** to manage files and edit text,
- navigate deep project directories,
- read/edit configuration files,
- use correct paths (absolute/relative) so commands work from anywhere.

✅ In this lab, you only do *lightweight* commands (safe on login nodes).  
❌ Don’t run heavy computations here—those belong on compute nodes later.

---

## Quick command cheat‑sheet

- `pwd` — print current directory (where am I?)
- `ls` — list files
- `ls -a` — include hidden files (names starting with `.`)
- `ls -lh` — human‑readable sizes
- `cd DIR` — change directory
- `cd ..` — go up (parent)
- `cd ~` — go home
- `mkdir -p` — make directories (including parents)
- `touch FILE` — create empty file
- `echo "text" > FILE` — write/overwrite file
- `echo "text" >> FILE` — append to file
- `cat FILE` — show contents
- `less FILE` — view long files (press `q` to quit)
- `cp SRC DST` — copy
- `mv SRC DST` — move/rename
- `rm -i FILE` — delete (asks first)
- `wc -l FILE` — count lines
- `find PATH -name "pattern"` — find files

---

## Nano mini‑cheat‑sheet (you can use this on Expanse)

Start editing:

```bash
nano filename
```

Useful keys (`^` means **Ctrl**):

- **Save:** `Ctrl + O` (then press **Enter**)
- **Exit:** `Ctrl + X`
- **Search:** `Ctrl + W`
- **Cut line:** `Ctrl + K`
- **Paste line:** `Ctrl + U`

> Tip: nano shows shortcuts at the bottom of the screen.

---

# Part 0 — Create a safe playground

1) Log in to the [SDSC Expanse User Portal](https://portal.expanse.sdsc.edu/) and select **expanse Shell access**. You will do the rest of this exercise in the shell.

2) Go to your home folder:

```bash
cd ~
```

3) Create and enter the lab folder:

```bash
mkdir -p linux-beginner-lab
cd linux-beginner-lab
```

4) Confirm where you are:

```bash
pwd
```

✅ **Checkpoint:** your path ends with `linux-beginner-lab`.

---

# Part 1 — Look around

### 1. List files and hidden files

```bash
ls
ls -a
ls -la
```

**Questions:**
1. What does `-a` change? A: Shows hidden files.
2. What do you think `.` and `..` represent? A: The current directory and the parent directory, respectively.

---

# Part 2 — Build a small HPC‑style project layout

Create this structure:

```
linux-beginner-lab/
  README.md
  docs/
  data/
    raw/
    processed/
  results/
  scratch/
```

### 2. Make directories

```bash
mkdir -p docs data/raw data/processed results scratch
```

### 3. Create starter files

```bash
touch README.md docs/notes.txt
```

### 4. Verify your tree

```bash
ls
find . -maxdepth 2 -type d
find . -maxdepth 2 -type f
```

✅ **Checkpoint:** you should see the folders above and the files `README.md`, `docs/notes.txt`.

---

# Part 3 — Edit with nano

### 5. Edit the README

Open `README.md` in nano:

```bash
nano README.md
```

Type the following (or similar):

```text
# Expanse Linux Beginner Lab

This folder contains practice files for learning Linux navigation, paths, and editing.
```

Save and exit (`Ctrl+O`, Enter, `Ctrl+X`).

View it:

```bash
cat README.md
```

### 6. Edit notes with nano

Open `docs/notes.txt` and add **two** bullet points about what you’ve learned so far.

```bash
nano docs/notes.txt
```

Example content:

```text
- I can list files with ls.
- I can move around with cd.
```

Save and exit, then verify:

```bash
cat docs/notes.txt
```

---

# Part 4 — Absolute vs Relative Paths

### 7. Relative path practice

From the lab root, read `docs/notes.txt` using a relative path:

```bash
cat docs/notes.txt
```

Go into `data/raw` and read the README using `..` (the parent directory):

```bash
cd data/raw
cat ../../README.md
```

Return to the lab root:

```bash
cd ../..
```

### 8. Absolute path practice

Print your absolute path:

```bash
pwd
```

Use that output to build an absolute path to `README.md` and view it:

```bash
cat /your/absolute/path/linux-beginner-lab/README.md
```

> Replace the placeholder with your real path.

✅ **Checkpoint:** In one sentence, define:
- **Absolute path:**
- **Relative path:**

---

# Part 5 — Copy, move, and rename

> **Make sure you are at the lab root first:**

```bash
cd ~/linux-beginner-lab
```
(`~/` indicates your home directory)

### 9. Copy a file

Copy your README into `docs` as a backup:

```bash
cp README.md docs/README.backup.md
ls -l docs
```

### 10. Rename a file

Rename `docs/notes.txt` to `docs/lab-notes.txt`:

```bash
mv docs/notes.txt docs/lab-notes.txt
ls docs
```

---

# Extended Mini Treasure Hunt 🧩💎 (15 clues)

You’ll create clue files, then follow them using Linux commands. The hunt makes you:

- use `ls -a` (hidden clues),
- move around with `cd` and `..`,
- use both relative and absolute paths,
- edit multiple files with **nano**,
- use `find` and `wc`.

## Treasure Hunt Setup (creates all clues)

> Start from the lab root:

```bash
cd ~/linux-beginner-lab
```

Copy/paste **all** commands below:

```bash
# Ensure a clean hunt folder
mkdir -p hunt/{trail,locks,answers}

# CLUE 0: Starting map
cat > hunt/trail/start.txt << 'EOF'
CLUE 1: Read docs/README.backup.md (yes, the backup). It tells you where to go next.
EOF

# Overwrite the backup with the first instruction for the hunt
cat > docs/README.backup.md << 'EOF'
# Backup README

CLUE 2: Go to hunt/trail and list ALL files (including hidden). Read the hidden clue.
EOF

# Hidden clue in hunt/trail
cat > hunt/trail/.clue2 << 'EOF'
CLUE 3: From hunt/trail, open the file at ../locks/lock1.txt
EOF

# Lock 1 (forces relative path with ..)
cat > hunt/locks/lock1.txt << 'EOF'
CLUE 4: The next clue is inside docs.
From hunt/locks, go to ../../docs and read clue4.txt
EOF

# Clue in docs (keeps this script‑free)
cat > docs/clue4.txt << 'EOF'
CLUE 5: Use nano to create docs/answer1.txt containing: "I can use nano."
Then read hunt/locks/lock2.txt
EOF

# Lock 2
cat > hunt/locks/lock2.txt << 'EOF'
CLUE 6: Open data/raw/sample.txt in nano and add EXACTLY 3 lines.
Then read hunt/trail/step6.txt
EOF

# Step6 points to creating a new tree
cat > hunt/trail/step6.txt << 'EOF'
CLUE 7: Create a new directory tree: forest/cave/deep
Then read hunt/trail/step7.txt
EOF

# Step7 requires nano to create a map
cat > hunt/trail/step7.txt << 'EOF'
CLUE 8: Use nano to create forest/cave/deep/treasure-map.txt.
Put ONE line: "Next: use an absolute path to read this file."
Then read hunt/trail/step9.txt
EOF

# Step9 (absolute path)
cat > hunt/trail/step9.txt << 'EOF'
CLUE 9: Use pwd to build an ABSOLUTE path to forest/cave/deep/treasure-map.txt and read it.
Then read hunt/trail/step10.txt
EOF

# Hidden clue again
cat > hunt/trail/step10.txt << 'EOF'
CLUE 10: In hunt/trail there is a hidden file .clue10. Find and read it.
EOF

cat > hunt/trail/.clue10 << 'EOF'
CLUE 11: Copy data/raw/sample.txt to data/processed/sample.cleaned.txt
Then read hunt/locks/lock3.txt
EOF

# Lock 3 uses wc and redirect
cat > hunt/locks/lock3.txt << 'EOF'
CLUE 12: Count lines in data/processed/sample.cleaned.txt using wc -l.
Save ONLY the number into docs/linecount.txt.
Hint: wc -l < file prints only a number.
Then read hunt/trail/step12.txt
EOF

# Step12 uses mv and scratch
cat > hunt/trail/step12.txt << 'EOF'
CLUE 13: Move data/processed/sample.cleaned.txt into scratch/ using mv.
Then read hunt/trail/step13.txt
EOF

# Step13 uses rename directory
cat > hunt/trail/step13.txt << 'EOF'
CLUE 14: Rename the directory results/ to output/ using mv.
Then read hunt/trail/step14.txt
EOF

# Step14 uses find
cat > hunt/trail/step14.txt << 'EOF'
CLUE 15: Use find to locate final-treasure.txt somewhere under forest/.
Then open it with cat.
EOF

# Final treasure file (placed deeper)
mkdir -p forest/cave/deep/secret
cat > forest/cave/deep/secret/final-treasure.txt << 'EOF'
YOU FOUND IT! 💎
EXPANSE PASSCODE: CLUSTER-READY

Final task (nano): create docs/answer2.txt and write ONE thing you learned today.
EOF

# Create the sample file placeholder
: > data/raw/sample.txt
```

✅ **Checkpoint (optional):**

```bash
ls hunt/trail
ls -a hunt/trail
ls hunt/locks
```

---

## Treasure Hunt Tasks (complete in order)

> If you get lost at any point:
>
> ```bash
> cd ~/linux-beginner-lab
> pwd
> ls
> ```

### CLUE 1

```bash
cat hunt/trail/start.txt
```

### CLUE 2

```bash
cat docs/README.backup.md
```

### CLUE 3 (hidden)

```bash
cd hunt/trail
ls -a
cat .clue2
```

### CLUE 4

```bash
cat ../locks/lock1.txt
```

### CLUE 5 (nano)

```bash
cd ../../docs
cat clue4.txt
nano answer1.txt
cat answer1.txt
```

Then:

```bash
cat ../hunt/locks/lock2.txt
```

### CLUE 6 (nano)

```bash
nano ../data/raw/sample.txt
cat ../data/raw/sample.txt
```

Then:

```bash
cat ../hunt/trail/step6.txt
```

### CLUE 7 (mkdir)

```bash
cd ..
cd ~/linux-beginner-lab
mkdir -p forest/cave/deep
cat hunt/trail/step7.txt
```

### CLUE 8 (nano)

```bash
nano forest/cave/deep/treasure-map.txt
```

Then:

```bash
cat hunt/trail/step9.txt
```

### CLUE 9 (absolute path)

```bash
pwd
# Build an absolute path, for example:
# cat /home/yourname/linux-beginner-lab/forest/cave/deep/treasure-map.txt
cat hunt/trail/step10.txt
```

### CLUE 10 (hidden)

```bash
cd hunt/trail
ls -a
cat .clue10
```

### CLUE 11 (copy)

```bash
cp ../../data/raw/sample.txt ../../data/processed/sample.cleaned.txt
ls -l ../../data/processed
cat ../locks/lock3.txt
```

### CLUE 12 (wc + redirect)

From the lab root:

```bash
cd ../..
wc -l < data/processed/sample.cleaned.txt > docs/linecount.txt
cat docs/linecount.txt
cat hunt/trail/step12.txt
```

### CLUE 13 (move into scratch)

```bash
mv data/processed/sample.cleaned.txt scratch/
ls scratch
cat hunt/trail/step13.txt
```

### CLUE 14 (rename results → output)

```bash
mv results output
ls
cat hunt/trail/step14.txt
```

### CLUE 15 (find the treasure)

```bash
find forest -name "final-treasure.txt"
# Use the path you found:
cat forest/cave/deep/secret/final-treasure.txt
```

Final nano task:

```bash
nano docs/answer2.txt
cat docs/answer2.txt
```

**Celebrate!** 🎉

---

## Grading

To receive a satisfactory for this exercise, submit your answers for the following questions on Canvas.

1) What does `pwd` show?
2) What is the difference between `ls` and `ls -a`?
3) What does `..` mean?
4) Give one absolute path you used.
5) Give one relative path you used.
6) In nano, what do `Ctrl+O` and `Ctrl+X` do?
7) What did `find` help you do?
8) What is the output of `cat docs/answer*.txt`?

---

## Expanse‑friendly habits

- Keep notes and documentation in `docs/`
- Keep raw data in `data/raw/`
- Keep processed data in `data/processed/`
- Use `scratch/` for temporary files
- Prefer **absolute paths** when you’re not sure where a command will run from

---

## Cleanup (optional)

After Exercise 0 is submitted and graded, you may delete the lab:

```bash
cd ~
rm -ri linux-beginner-lab
```

## Instructor notes

- If learners get lost, reset with:

```bash
cd ~/linux-beginner-lab
pwd
ls
```

- Common stuck points:
  - Hidden files require `ls -a`
  - `..` means “parent directory”
  - Absolute paths start with `/`
  - In nano: `Ctrl+O` saves, `Ctrl+X` exits

