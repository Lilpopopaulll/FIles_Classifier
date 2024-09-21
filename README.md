# Files Classifier

This Python script organizes files by their extensions into corresponding folders. It scans a directory and automatically moves files into folders based on their file types (extensions).

## Features
- Automatically organizes files into folders based on their extensions.
- Creates folders dynamically for each file type found.
- Works for any kind of file extension (e.g., `.jpg`, `.pdf`, `.zip`).

## Requirements
- Python 3.x
- `shutil` and `os` libraries (included with Python by default)

## How to Use

1. **Create a `download` Folder:**

   Inside the root directory (where the Python script is located), create a folder called `download`. This folder is where you will place all the files you want to organize.

   ```bash
   mkdir download

2. **Add Files to Organize:**

   Move or copy the files you want to organize into the download folder. You can place any type of file (e.g., .jpg, .png, .pdf, .txt, .zip, etc.).
