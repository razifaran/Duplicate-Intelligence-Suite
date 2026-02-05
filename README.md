# 📂 Duplicate Intelligence Suite

A powerful tool to find duplicate files and reclaim your storage space. This suite is designed to be **safe** (it never deletes files) and **fast** (it only reads what it needs to identify a duplicate).

---

## 🚀 1. Setup (One-Time Only)

To run these scripts, your computer needs "Python." Here is the easiest way to get it:

- **Windows:** Open the **Microsoft Store**, search for **"Python 3.12"**, and click **Get**.
- **Mac:** Open your **Terminal** (Press Cmd + Space, type "Terminal"), type `python3`, and follow the prompt to install.

---

## 💻 2. How to Run the Scripts

You do not need to write any code. Just follow these steps:

1. **Open your Command Line:**
   - **Windows:** Press the `Windows Key`, type `cmd`, and press Enter.
   - **Mac:** Press `Cmd + Space`, type `Terminal`, and press Enter.

2. **The Drag-and-Drop Method:**
   - Type the word `python` followed by a **space**.
   - Drag the script file (like `dupe_report.py`) from your folder and drop it right into the black window.
   
   **It should look like this before you press Enter:**
   `C:\> python "C:\Users\Name\Desktop\dupe_report.py"`

3. **Press Enter.**

---

## 🛠 Which Tool Should I Use?

### 🔎 Step 1: The Scanner (`dupe_report.py`)
Run this first. It scans your folder and puts a **Report** on your Desktop. It shows you exactly how much space you are wasting and where the duplicates are. **It does not move any files.**

### 🧹 Step 2: The Cleaner (`dupe_cleaner.py`)
Run this to take action. It finds the duplicates and moves them into a new folder called **RECOVERY**. This allows you to double-check them before you delete them yourself.

> **💡 Pro Tip:** When the script asks you to "Paste the folder path," you can **drag and drop the target folder** into the window just like you did with the script!
