import argparse
import json
import logging
import os

from smart_automation_suite.organizer import organize_folder
from smart_automation_suite.utils.logger import setup_logger
from smart_automation_suite.utils.history import load_last_run, save_history

def load_config():
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError("config.json not found in package directory")

    with open(config_path, "r") as f:
        config = json.load(f)

    if "file_types" not in config:
        raise KeyError("config.json is missing 'file_types'")

    return config


def main():
    config = load_config()

    parser = argparse.ArgumentParser(
        description="Smart Automation Suite – File Organizer"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Full path of the folder to organize"
    )

    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview changes without moving files"
    )

    parser.add_argument(
        "--undo",
        action="store_true",
        help="Undo the last organization run"
    )



    args = parser.parse_args()
    
    if args.undo:
        try:
            last_run, remaining_history = load_last_run()
            restored = 0

            for move in last_run["moves"]:
                if os.path.exists(move["destination"]):
                    os.makedirs(os.path.dirname(move["source"]), exist_ok=True)
                    os.rename(move["destination"], move["source"])
                    restored += 1

            save_history(remaining_history)
            logging.info(f"Last run undone successfully. Restored {restored} files.")
            return

        except Exception as e:
            print(f"Error during undo: {e}")
            return

    setup_logger()

    preview_mode = args.preview or config.get("default_preview", False)

    logging.info("Starting Smart File Organizer")

    try:
        moved, skipped = organize_folder(
            folder_path=args.path,
            file_types=config["file_types"],
            preview=preview_mode
        )

        if preview_mode:
            logging.info("Preview completed (no files moved)")
        else:
            logging.info(f"Completed: {moved} files moved, {skipped} skipped")

    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
