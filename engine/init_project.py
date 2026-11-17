"""
Project Initialization Tool
Usage:
    python engine/init_project.py --name <project_slug> [--title <english_or_hindi_title>] [--format <shorts|landscape>]

Creates standard modular project structure with automated sequential prefix numbering:
    <NN_project_slug>/
    ├── project_config.json
    ├── 01_script_and_storyboard.md
    ├── sample_images/
    ├── generated_clips/
    ├── audio/
    ├── final_output/
    └── youtube_writeups/
"""

import os
import sys
import argparse
import json
import re
from pathlib import Path
from datetime import datetime

def get_next_project_prefix(base_path):
    """Scan base directory for existing NN_ project directories and return the next formatted number string."""
    existing_nums = []
    for item in base_path.iterdir():
        if item.is_dir() and item.name not in ("engine", "rules", ".git", ".gemini"):
            m = re.match(r"^(\d+)_(.+)$", item.name)
            if m:
                existing_nums.append(int(m.group(1)))
    
    next_num = max(existing_nums) + 1 if existing_nums else 1
    return f"{next_num:02d}"

def init_project(name, title=None, base_dir=".", format_type="shorts"):
    base_path = Path(base_dir).resolve()

    # Check if name already has a numeric prefix (e.g. 01_project or 07_project)
    if re.match(r"^\d+_", name):
        folder_name = name
    else:
        prefix = get_next_project_prefix(base_path)
        folder_name = f"{prefix}_{name}"

    project_dir = base_path / folder_name

    if project_dir.exists():
        print(f"⚠️ Warning: Directory '{project_dir}' already exists.")
    else:
        project_dir.mkdir(parents=True)
        print(f"📁 Created project folder: {folder_name} ({project_dir})")

    # Standard subdirectories
    subdirs = [
        "sample_images",
        "generated_clips",
        "audio",
        "final_output",
        "youtube_writeups"
    ]
    for sub in subdirs:
        (project_dir / sub).mkdir(parents=True, exist_ok=True)
        print(f"   └── {sub}/")

    # Default settings based on format
    is_shorts = format_type.lower() == "shorts"
    aspect_ratio = "9:16" if is_shorts else "16:9"
    resolution = "1080x1920" if is_shorts else "1920x1080"
    target_shots = 6 if is_shorts else 18
    target_duration = 40 if is_shorts else 180

    # Project config template
    config = {
        "project_name": folder_name,
        "title": title or folder_name.split("_", 1)[-1].replace("_", " ").title(),
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "channel": "Dream Byte",
        "channel_handle": "@DreamByte-y3h",
        "format": "YouTube Shorts" if is_shorts else "YouTube Landscape",
        "target_shots": target_shots,
        "target_duration_sec": target_duration,
        "aspect_ratio": aspect_ratio,
        "resolution": resolution,
        "fps": 30,
        "character_consistency_reference": None,
        "shot_durations": []
    }

    config_path = project_dir / "project_config.json"
    if not config_path.exists():
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"   └── project_config.json")

    # Storyboard & Script template
    storyboard_template = f"""# 🎬 {config['title']} — Script & Storyboard
**Target Duration:** ~{target_duration}s ({target_shots} Shots × ~6-7s) | **Aspect Ratio:** {aspect_ratio}

## 🎭 Characters & Setting
- **Main Character:** 
- **Supporting Character:** 
- **Setting / Environment:** 
- **Master Reference Image (Rule #0):** `sample_images/shot_master_character.png`

---

## 📋 Micro-Chunk Breakdown
*(Mandatory Laws: 100% Genuine Video Motion | Snappy Fast-Paced Action | Zero Static Slideshows)*

### Shot 01: [VIRAL COLD OPEN HOOK — First 0-3 Seconds]
- **Hook Purpose:** Intense curiosity / shocking visual to ensure >75% "Stayed to Watch"
- **Visual Prompt (Fast 3D Motion):** 
- **Hindi Script (Spoken Voiceover):** 
- **Target Duration:** ~6.5s

### Shot 02: [Inciting Incident / Discovery]
- **Visual Prompt:** 
- **Hindi Script:** 
- **Target Duration:** ~6.5s

### Shot 03: [Rising Action / Magical Event]
- **Visual Prompt:** 
- **Hindi Script:** 
- **Target Duration:** ~6.5s

### Shot 04: [Turning Point / Greed or Conflict]
- **Visual Prompt:** 
- **Hindi Script:** 
- **Target Duration:** ~6.5s

### Shot 05: [Climax / Crucial Consequence]
- **Visual Prompt:** 
- **Hindi Script:** 
- **Target Duration:** ~6.5s

### Shot 06: [CLIMAX + ENDING ENGAGEMENT QUESTION]
- **Engagement Purpose:** Pose a viewer dilemma/question in final 3-5s to trigger hundreds of comments
- **Visual Prompt:** 
- **Hindi Script:** 
- **Target Duration:** ~6.5s
"""
    sb_path = project_dir / "01_script_and_storyboard.md"
    if not sb_path.exists():
        with open(sb_path, "w", encoding="utf-8") as f:
            f.write(storyboard_template)
        print(f"   └── 01_script_and_storyboard.md")

    print(f"\n✅ Project '{folder_name}' initialized successfully following Master Standards!")
    return project_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize new animation project with auto-numbering")
    parser.add_argument("--name", required=True, help="Folder slug for project (e.g. mendhakraj_aur_naag)")
    parser.add_argument("--title", default=None, help="Display title")
    parser.add_argument("--format", default="shorts", choices=["shorts", "landscape"], help="Project format")
    parser.add_argument("--base-dir", default=".", help="Base workspace directory")
    args = parser.parse_args()

    init_project(args.name, args.title, args.base_dir, args.format)
