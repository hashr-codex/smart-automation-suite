import os
import shutil

from smart_automation_suite.utils.history import save_run
from smart_automation_suite.utils.report import save_dry_running_report


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
    move_log = []   # ✅ local, safe

    for filename in os.listdir(folder_path):
        source = os.path.join(folder_path, filename)

        if not os.path.isfile(source):
            continue

        ext = os.path.splitext(filename)[1]
        category = get_category(ext, file_types)

        target_dir = os.path.join(folder_path, category)
        destination = os.path.join(target_dir, filename)

        # 🔍 PREVIEW MODE
        if preview:
            move_log.append({
                "source": source,
                "destination": f"{category}/{filename}"
            })
            print(f"[PREVIEW] {filename} → {category}/")
            continue

        # 🚚 REAL MOVE
        os.makedirs(target_dir, exist_ok=True)

        if not os.path.exists(destination):
            shutil.move(source, destination)
            move_log.append({
                "source": source,
                "destination": destination
            })
            moved += 1
        else:
            skipped += 1

    # ✅ Save history only once
    if not preview and move_log:
        save_run(move_log)

    # ✅ Save dry-run report only in preview
    if preview and move_log:
        save_dry_running_report(move_log)

    return moved, skipped
