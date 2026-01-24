# Smart Automation Suite

## Overview

Smart Automation Suite is a long-term Python project focused on building
modular, practical automation tools for everyday system tasks.

Instead of creating many small, disconnected scripts, this project is
designed to evolve gradually — with each module building on top of
previous ideas, design decisions, and lessons learned.

This repository reflects continuous development rather than one-time
solutions.

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
