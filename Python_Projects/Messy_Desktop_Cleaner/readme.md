
<img width="711" height="340" alt="Screenshot 2026-02-04 at 10 57 54 AM" src="https://github.com/user-attachments/assets/72e4b3c5-586d-47c1-949e-34c3f26390b8" />

<img width="1198" height="375" alt="Screenshot 2026-02-04 at 11 00 24 AM" src="https://github.com/user-attachments/assets/ed2239f5-668c-488d-82c7-24c32c7b891a" />


<img width="962" height="169" alt="Screenshot 2026-02-04 at 11 00 48 AM" src="https://github.com/user-attachments/assets/792f07f5-5805-41f5-b1ae-33676e9782a7" />


Core Difference

    os (Operating System): A low-level interface for interacting with the operating system. It handles tasks like navigating directories, reading environment variables, and basic file operations.

    shutil (Shell Utilities): A high-level interface focused on file management. It builds upon os to handle complex tasks like copying files, moving directories, and archiving, effectively automating commands you would normally run in a shell (terminal).

1. The os Module

Use this for directory navigation, environment setup, and path manipulation.
Key Attributes
Attribute	Note
os.name	Returns the name of the operating system dependent module imported (e.g., 'posix' for Linux/Mac, 'nt' for Windows).
os.environ	A dictionary object representing the user's environment variables (e.g., accessing PATH or HOME).
os.getcwd()	Returns the Current Working Directory as a string.
os.linesep	The string used to separate (or terminate) lines on the current platform (e.g., \n on Unix, \r\n on Windows).
Key Methods (File & Directory Management)
Method	Short Note
os.chdir(path)	Change Directory. Changes the current working directory to the specified path.
os.listdir(path)	Returns a list of all files and folders in the specified directory.
os.mkdir(path)	Creates a single new directory. Raises an error if the parent directory does not exist.
os.makedirs(path)	Recursive directory creation. Creates the target directory and any missing parent directories.
os.remove(path)	Deletes a file. (Will raise an error if you try to delete a folder).
os.rmdir(path)	Deletes an empty directory.
os.rename(src, dst)	Renames a file or directory. (Note: Can fail if moving across different disk partitions).
os.walk(top)	Generates the file names in a directory tree by walking the tree either top-down or bottom-up.
The os.path Submodule

Strictly speaking a submodule, but essential for working with the os module.

    os.path.join(path, *paths): Intelligently joins one or more path components (adds correct slashes / or \ automatically).

    os.path.exists(path): Returns True if the path exists.

    os.path.isfile(path): Returns True if the path is a regular file.

    os.path.isdir(path): Returns True if the path is a directory.

    os.path.basename(path): Returns the final component of a path (the file name).

    os.path.split(path): Splits the path into a pair (head, tail) where tail is the last pathname component.

2. The shutil Module

Use this for "heavy lifting" file operations like copying, moving, or deleting entire trees.
Key Methods (Copying)
Method	Short Note
shutil.copyfile(src, dst)	Copies the contents of a file to a destination file. No metadata (permissions/timestamps) is preserved.
shutil.copy(src, dst)	Copies file data and file permissions. Destination can be a file or a directory.
shutil.copy2(src, dst)	Identical to copy(), but also attempts to preserve all metadata (creation time, modification time, etc.). Best for backups.
shutil.copytree(src, dst)	Recursively copies an entire directory and all its contents to a new location.
Key Methods (Moving & Deleting)
Method	Short Note
shutil.move(src, dst)	Recursively moves a file or directory to another location. (Equivalent to "cut and paste").
shutil.rmtree(path)	Dangerous: Recursively deletes a directory and all of its contents (subfolders and files).
Key Methods (System & Archiving)
Method	Short Note
shutil.disk_usage(path)	Returns disk usage statistics (total, used, free) for the given path.
shutil.which(cmd)	Finds the path to an executable (like the which command in UNIX).
shutil.make_archive(base_name, format, root_dir)	Creates an archive file (e.g., zip, tar) from a directory.
Summary: When to use which?
Task	Use Module	Function
Check where you are	os	os.getcwd()
Join file paths safely	os.path	os.path.join()
Create a folder structure	os	os.makedirs()
Copy a file	shutil	shutil.copy2()
Delete a huge folder	shutil	shutil.rmtree()
Rename/Move a file	shutil	shutil.move() (More robust than os.rename)
















