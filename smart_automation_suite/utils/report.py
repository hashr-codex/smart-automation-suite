import json
from datetime import datetime

REPORT_FILE = "dry_running_report.json"

def save_dry_running_report(planned_moves):
    report = {
        "timestamps": datetime.now().isoformat(),
        "total_files": len(planned_moves),
        "planned_moves": planned_moves
    }

    with open(REPORT_FILE, "w") as f:
        json.dump(report, f, indent=2)
        