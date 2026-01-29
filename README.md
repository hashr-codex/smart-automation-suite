# Smart Automation Suite

## Overview

Smart Automation Suite is a long-term, evolving Python project focused on building practical automation tools with clean architecture and real-world usability in mind.

The project is designed to grow over time, with each feature added incrementally and documented as part of the development journey.

---

## Why This Project Exists

Many automation scripts solve a single problem and are then discarded.
This project takes a different approach:

- Build reusable automation modules
- Improve them incrementally
- Apply clean architecture from the start
- Document decisions, not just code

The goal is to simulate how real-world software grows over time.

---

## Project Structure

```text
smart-automation-suite/
├── automation_suite/
│   ├── __init__.py
│   └── file_organizer.py
│
├── cli.py
├── CHANGELOG.md
└── README.md
```
## Current Modules

### File Organizer(v1.0)

Organizes files inside a given directory into categorized folders based on file extensions.

### Features
- File type detection
- Automatic folder creation
- safe file movement (no overwriting)
- Clean sepration between logic and CLI

## Development Log

### Day 1 - Project Fondation
- Definedlong-term project vision
- Ceated modular folder structure
- Implemented File Organzier as first core module
- Separated CLI from logic

> Focus: clean architecture and future scalability.

### Day 2 - Preview Mode Added
- Added dry-run (preview) functionality
- Users can safely see changes before files are moved
- Improved real-world usability of the tool

### Day 3 - Safety & Polish

- Added Ignore rules to prevent re-organizing output folders
- Implemented file movement summary
- Improved overall robustness and user experience

## Configuration

Project behavior is controlled using `config.json`.

- `ignore-folders`: folders thatwill not be processed.
- `file_types`: file extensions to category mappings.
- `default_preview`: default behavior for preview mode.

This allows customization without modifying source code.