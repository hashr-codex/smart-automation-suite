import os
import shutil
FILE_TYPE = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio/Music": [".mp3", ".wav"],
}

IGNORE_FOLDER = {
    "Images",
    "Documents",
    "Videos",
    "Audio",
    "Archives",
    "Others",
    ".git",
    "__pycache__",
}

def get_category(extension):
    for categroy, extensions in FILE_TYPE.items():
        if extension.lower() in extensions:
            return categroy
    return "Others"

def organize_folder(folder_path, preview=False):
    if not os.path.isdir(folder_path):
        raise ValueError("Invalid folder path")
    
    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)

        if not os.path.isfile(source):
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext)

        target_dir = os.path.join(folder_path, category)
        destination = os.path.join(target_dir, filename)

        if preview:
            print(f"[PREVIEW] {filename} - {category}/")
            continue

        os.makedirs(target_dir, exist_ok=True)

        

        if not os.path.exists(destination):
            shutil.move(source, destination)
            print(f"Moved: {filename} - {category}/")

        