# 📂 Duplicate Intelligence Suite

A powerful, two-step Python utility designed to reclaim storage space by identifying and managing duplicate files. This suite is optimized for speed, using a **1KB Header Hashing** method that allows it to scan thousands of files in seconds without high CPU overhead.

## ✨ Features
- **Fast Indexing:** Only reads the first 1KB of data to verify file identity.
- **Safety First:** Read-only hashing ensures your original data is never corrupted.
- **Non-Destructive:** The cleaner moves files to a recovery folder rather than deleting them instantly.
- **Desktop Reporting:** Automatically generates easy-to-read text reports on your Desktop.

---

## 🚀 How to Run (For New Users)

You don't need to be a programmer to use these tools. Follow these steps:

### Step 1: Install Python
Ensure you have Python installed on your computer. 
- **Windows:** Download from [Python.org](https://www.python.org/) or the Microsoft Store.
- **Mac/Linux:** Usually comes pre-installed.

### Step 2: Download the Scripts
Download the `.py` files from this repository to a folder on your computer.

### Step 3: Open the Terminal or Command Prompt
1. Open your "Command Prompt" (Windows) or "Terminal" (Mac).
2. Type `python` followed by a space.
3. Drag and drop the script file (`dupe_report_master.py` or `dupe_recovery_cleaner.py`) into the window. It will look something like this:
   `python C:\Users\YourName\Desktop\dupe_report_master.py`
4. Press **Enter**.

### Step 4: Paste your Folder Path
The script will ask you to "Paste the folder path." 
- Go to the folder you want to scan.
- Copy the address bar at the top of your file explorer.
- Paste it into the black window and press **Enter**.

---

## 🛠 Which Tool Should I Use?

### 1. The Scanner (`dupe_report_master.py`)
**Best for:** Auditing. 
This script scans your folder and creates a report on your Desktop showing exactly how much space you could save and where the duplicates are located. It **does not move or change** any files.

### 2. The Cleaner (`dupe_recovery_cleaner.py`)
**Best for:** Action.
This script finds the duplicates and moves them into a new folder named `RECOVERY_[FolderName]`. This allows you to double-check the files before you hit the delete button.

---

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.