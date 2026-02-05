
<img width="711" height="340" alt="Screenshot 2026-02-04 at 10 57 54 AM" src="https://github.com/user-attachments/assets/72e4b3c5-586d-47c1-949e-34c3f26390b8" />

<img width="1198" height="375" alt="Screenshot 2026-02-04 at 11 00 24 AM" src="https://github.com/user-attachments/assets/ed2239f5-668c-488d-82c7-24c32c7b891a" />


<img width="962" height="169" alt="Screenshot 2026-02-04 at 11 00 48 AM" src="https://github.com/user-attachments/assets/792f07f5-5805-41f5-b1ae-33676e9782a7" />

---

```markdown
# 📂 Python File Management: `os` & `shutil` Cheat Sheet

A quick reference guide for interacting with the operating system and managing files in Python.

## ⚡ Core Differences

| Module | Full Name | Primary Use Case |
| :--- | :--- | :--- |
| **`os`** | **Operating System** | Low-level interface. Best for directory navigation, environment variables, and creating/deleting single items. |
| **`shutil`** | **Shell Utilities** | High-level interface. Best for "heavy lifting" like copying files, archiving, and recursive moves/deletes. |

---

## 1. The `os` Module
> **Import:** `import os`

### 🔹 Key Attributes
| Attribute | Description |
| :--- | :--- |
| `os.name` | The name of the OS dependent module (e.g., `'posix'`, `'nt'`). |
| `os.environ` | A dictionary of environment variables (e.g., `os.environ['HOME']`). |
| `os.getcwd()` | Returns the **Current Working Directory** as a string. |
| `os.linesep` | The string used to terminate lines (`\n` on Unix, `\r\n` on Windows). |

### 🔹 File & Directory Methods
```python
os.chdir(path)      # Change current working directory
os.listdir(path)    # List all files/folders in a directory
os.mkdir(path)      # Create a SINGLE directory
os.makedirs(path)   # Create a directory AND any missing parent directories (Recursive)
os.remove(path)     # Delete a FILE
os.rmdir(path)      # Delete an EMPTY directory
os.rename(src, dst) # Rename a file/directory
os.walk(top)        # Generate filenames in a directory tree (root, dirs, files)

```

### 🔹 The `os.path` Submodule

Essential for cross-platform path manipulation.

| Method | Description |
| --- | --- |
| `os.path.join(a, b)` | Joins paths intelligently (handles `/` or `\` automatically). |
| `os.path.exists(path)` | Returns `True` if path exists. |
| `os.path.isfile(path)` | Returns `True` if path is a regular file. |
| `os.path.isdir(path)` | Returns `True` if path is a directory. |
| `os.path.basename(path)` | Returns the filename component of the path. |
| `os.path.split(path)` | Splits path into `(head, tail)`. |

---

## 2. The `shutil` Module

> **Import:** `import shutil`

### 🔹 Copying Files

| Method | Preserves Metadata? | Destination | Note |
| --- | --- | --- | --- |
| `shutil.copyfile(src, dst)` | ❌ No | File | Copies contents only. |
| `shutil.copy(src, dst)` | ✅ Permissions | File/Dir | Copies data & permission bits. |
| `shutil.copy2(src, dst)` | ✅ All Metadata | File/Dir | **Recommended.** Preserves timestamps & permissions. |
| `shutil.copytree(src, dst)` | ✅ All Metadata | Dir | Recursively copies an entire directory tree. |

### 🔹 Moving & Deleting

```python
# Move a file or directory (Recursively)
shutil.move(src, dst)  

# DANGEROUS: Recursively delete a directory and ALL contents
shutil.rmtree(path)    

```

### 🔹 System & Archiving

* **`shutil.disk_usage(path)`**: Return disk usage statistics (total, used, free).
* **`shutil.which(cmd)`**: Return the path to an executable (like UNIX `which`).
* **`shutil.make_archive(base_name, format, root_dir)`**: Create a zip/tar archive.

---

## 📌 Summary: When to use what?

* **Where am I?** → `os.getcwd()`
* **Build a path** → `os.path.join()`
* **Create folders** → `os.makedirs()`
* **Copy a file** → `shutil.copy2()`
* **Delete a folder** → `shutil.rmtree()`

















