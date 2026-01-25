import os
from automation_suite.file_organizer import organize_folder

def main():
    print("Smart Automation Suite - File Organizer v1\n")

    while True:
        path = input("Paste folder path to organize: ").strip().strip('"')
        abs_path = os.path.abspath(path)

        if os.path.isdir(abs_path):
            try:
                organize(abs_path)
                print("\n Organization complete.")
                break
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid Path. Try Again. \n")

if __name__ == "__main__":
    main()