# 🐍 Week 1 – Python Basics & File Handling

## 📌 Overview
This week focuses on building a strong foundation in Python scripting, logging, and file automation — all structured like a real internship environment.

You’re learning how to:
- ✅ Read and clean files using `open()`
- ✅ Handle errors with `try/except`
- ✅ Write modular functions
- ✅ Use pseudocode to plan scripts
- ✅ Implement logging for traceability
- ✅ Push your work to GitHub

---

## 📂 Folder Structure
```
week_01_python_basics/ 
│── data/ # Contains sample input files 
│── logs/ # Stores runtime logs (ignored by Git) 
│── file_reader_logger.py # Reads a config-style file and logs output 
│── error_log_filter.py # Filters lines that start with "ERROR" and logs them 
│── README.md # This file
```
## ✅ Project Progress

| Script                | Description                                           | Status     |
|-----------------------|-------------------------------------------------------|------------|
| `file_reader_logger.py` | Reads a simple file, strips whitespace, logs actions | ✅ Complete |
| `error_log_filter.py`   | Reads a file, filters lines with `"ERROR"`, logs results | ✅ Complete |
| `empty_line_remover.py` | (Planned) Will remove empty lines from a file         | ⬜ Upcoming |
| `file_merger.py`        | (Planned) Will combine two files into one            | ⬜ Upcoming |

---

## 🧠 Weekly Learning Goals

- [x] Use `open()` to read and process files
- [x] Write functions with clean structure
- [x] Plan logic using pseudocode before coding
- [x] Implement `try/except` for file handling
- [x] Set up a local logging system using `logging`
- [x] Use Git + GitHub to manage and push updates
- [X] Complete all 3–4 coding challenges by end of week
- [ ] Review basic pandas concepts

---

## 📝 Notes

- The `logs/` folder is ignored in Git using `.gitignore`, so log files stay local
- Each script starts with a pseudocode block to simulate pro-level planning
- All work is structured and tracked by week to match your internship prep schedule

---

---

## 🐼 pandas_basic_cleaner.py – CSV Cleanup Tool

### 📌 Purpose
Reads a messy CSV file (e.g., from NetSuite), removes duplicate/missing rows, and saves a cleaned version.

### 📂 Input
- `data/messy_export.csv` ← Uncleaned file

### 📤 Output
- `data/cleaned_export.csv` ← Final cleaned version
- `logs/pandas_cleaner.log` ← Tracks all steps (start, read, clean, save)

### 🛠 Tools Used
- `pandas`
- `logging`
- `os`
- `functions`, `try/except`, pseudocode

### 🔍 Sample Use
```bash
python pandas_basic_cleaner.py

## 🚀 Next Steps

- review pandas