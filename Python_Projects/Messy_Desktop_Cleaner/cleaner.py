import os 
import shutil
import sys 

#---configuration---
if len(sys.argv) > 1:
    SOURCE_DIR = sys.argv[1]
else:
    SOURCE_DIR = input("Enter full path of folder to clean: ").strip()

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

def clean_folder():
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory '{SOURCE_DIR}' does not exist.")
        return
    
    # Define the main folder where everything will go
    clean_root = os.path.join(SOURCE_DIR, "clean&tidy")
    
    #---Logic---
    for filename in os.listdir(SOURCE_DIR):
        if filename.startswith("."):
            continue

        name, ext = os.path.splitext(filename)
        ext = ext.lower() 

        target_folder = None
        for folder, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                target_folder = folder
                break
        
        if target_folder:
            # Change: Join clean_root (not SOURCE_DIR) with the target folder
            new_folder_path = os.path.join(clean_root, target_folder)

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            src_path = os.path.join(SOURCE_DIR, filename)
            dest_path = os.path.join(new_folder_path, filename)

            try:
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename} -> clean&tidy/{target_folder}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    clean_folder()