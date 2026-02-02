import os
import shutil

def get_category(extension, file_types):
    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_folder(folder_path, file_types, preview=False):
    if not os.path.isdir(folder_path):
        raise ValueError("Invalid folder path")

    moved = 0
    skipped = 0

    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)

        if not os.path.isfile(source):
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext, file_types)

        target_dir = os.path.join(folder_path, category)
        destination = os.path.join(target_dir, filename)

        if preview:
            print(f"[PREVIEW] {filename} → {category}/")
            continue

        os.makedirs(target_dir, exist_ok=True)

        if not os.path.exists(destination):
            shutil.move(source, destination)
            moved += 1
        else:
            skipped += 1

    return moved, skipped
