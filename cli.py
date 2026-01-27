import os
from automation_suite import organize_folder

print("Smart File Organizer")
print("Paste the full folder path to organize")

path = input("Folder path: ").strip()

if not os.path.isdir(path):
    print("Invalid path. Please try again.")
    exit()

preview_choice = input("Preview before organizing? (y/n): ").strip().lower()

preview = preview_choice == "y"

moved, categories = organize_folder(path, preview=preview)

if preview:
    print("\nPreview complete. No files were moved.")

if not preview:
    print("\nSummary")
    print("-" * 20)
    print(f"Files moved       : {moved}")
    print(f"Categories created:  {categories}")