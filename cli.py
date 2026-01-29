import os
from automation_suite import organize_folder
import json

with open("config.json", "r") as f:
    config = json.load(f)

default_preview = config.get("default_preview", False)


print("Smart File Organizer")
print("Paste the full folder path to organize")

path = input("Folder path: ").strip()

if not os.path.isdir(path):
    print("Invalid path. Please try again.")
    exit()

preview_input = input(f"Preview before organizing? (y/n) [defualt: {'y' if default_preview else 'n'}]: ").strip().lower()

if preview_input == "":
    preview = default_preview
else:
    preview = preview_input == "y"

moved, categories = organize_folder(path, preview=preview)

if preview:
    print("\nPreview complete. No files were moved.")

if not preview:
    print("\nSummary")
    print("-" * 20)
    print(f"Files moved       : {moved}")
    print(f"Categories created:  {categories}")