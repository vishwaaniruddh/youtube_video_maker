"""
Production & Calendar Status Sync Tool
Usage:
    python content_planner/sync_status.py

Automatically inspects workspace project folders and syncs status in:
    content_planner/30_days_content_tracker.csv
"""

import os
import sys
import csv
import glob
from pathlib import Path

def get_project_status(folder_path):
    if not folder_path.exists():
        return "Pending"
    
    final_output = list((folder_path / "final_output").glob("*.mp4"))
    clips = list((folder_path / "generated_clips").glob("*.mp4"))
    audio = list((folder_path / "audio").glob("*.mp3"))
    script = folder_path / "01_script_and_storyboard.md"

    if final_output:
        return "Video Completed"
    elif len(clips) >= 6:
        return "Clips Ready (Awaiting Assembly)"
    elif len(clips) > 0:
        return f"Clips Generating ({len(clips)}/10)"
    elif audio:
        return "Audio Ready"
    elif script.exists():
        return "Script Ready"
    else:
        return "Initialized"

def sync_tracker():
    base_path = Path(".").resolve()
    csv_path = base_path / "content_planner" / "30_days_content_tracker.csv"

    if not csv_path.exists():
        print(f"❌ Error: {csv_path} not found!")
        return

    rows = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for r in reader:
            rows.append(r)

    updated_count = 0
    status_summary = {}

    for row in rows:
        folder_name = row.get("Project_Folder", "").strip()
        folder_path = base_path / folder_name

        current_status = row.get("Status", "Pending")
        # Preserve manual Uploaded or Scheduled status if already marked
        if current_status not in ("Uploaded", "Scheduled"):
            detected = get_project_status(folder_path)
            if detected != current_status:
                row["Status"] = detected
                updated_count += 1
        
        stat = row.get("Status", "Pending")
        status_summary[stat] = status_summary.get(stat, 0) + 1

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\n========================================================")
    print("📊 30-DAY CONTENT TRACKER SYNC SUMMARY")
    print("========================================================")
    print(f"Total Stories Planned: {len(rows)}")
    for k, v in sorted(status_summary.items()):
        print(f"  • {k}: {v}")
    print(f"\n✅ Updated {updated_count} status entries in {csv_path.name}!")
    print("========================================================\n")

if __name__ == "__main__":
    sync_tracker()
