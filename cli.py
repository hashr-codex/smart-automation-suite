import argparse
import json
import logging
import os

from organizer import organize_folder
from utils.logger import setup_logger


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)
    
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

    args = parser.parse_args()

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
