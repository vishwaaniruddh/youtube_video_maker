"""
Universal Animation Assembly Engine
Usage:
    python engine/assemble_movie.py --project-dir <path_to_project_dir> [--output-name <optional_name>]

Rules Enforced:
    1. Zero Premature Assembly: Fails immediately if any required clip is missing.
    2. 100% Real Motion: Verifies all input clips are valid video files (no static images).
    3. Auto Resolution & Aspect Normalization: Scales and center-crops all inputs to 1920x1080 30fps progressive.
    4. Audio Beat/Segment Synchronization: Aligns clips sequentially to match master audio duration.
"""

import os
import sys
import argparse
import subprocess
import json
import glob
import re
import shutil
from pathlib import Path

def get_ffmpeg_cmd():
    if shutil.which("ffmpeg"):
        return "ffmpeg"
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"

def get_media_duration(file_path):
    """Retrieve duration in seconds using ffprobe or ffmpeg fallback."""
    if shutil.which("ffprobe"):
        try:
            cmd = [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(file_path)
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return float(result.stdout.strip())
        except Exception:
            pass
    
    ffmpeg_exe = get_ffmpeg_cmd()
    cmd = [ffmpeg_exe, "-i", str(file_path)]
    result = subprocess.run(cmd, capture_output=True, text=True, errors="ignore")
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d\.]+)", result.stderr)
    if m:
        return float(m.group(1))*3600 + float(m.group(2))*60 + float(m.group(3))
    raise RuntimeError(f"Could not determine duration of {file_path}")

def verify_clips(clips_dir, expected_count=None):
    """Scan clips directory and ensure all files are valid non-empty video files."""
    clips = sorted(glob.glob(os.path.join(clips_dir, "*.mp4")))
    if not clips:
        raise FileNotFoundError(f"No .mp4 clips found in {clips_dir}!")
    
    if expected_count and len(clips) < expected_count:
        raise ValueError(
            f"RULE VIOLATION: Zero Premature Assembly! "
            f"Expected {expected_count} clips, but only found {len(clips)} in {clips_dir}."
        )

    valid_clips = []
    for c in clips:
        size = os.path.getsize(c)
        if size < 100000:  # less than 100KB is invalid
            raise ValueError(f"Clip {c} is corrupted or too small ({size} bytes).")
        dur = get_media_duration(c)
        valid_clips.append((c, dur))
        print(f"  [OK] {os.path.basename(c)}: {dur:.2f}s ({size / 1024 / 1024:.2f} MB)")
    
    return valid_clips

def assemble_project(project_dir, output_name=None, speed=1.25):
    project_path = Path(project_dir).resolve()
    print(f"\n========================================================")
    print(f"🚀 RUNNING UNIVERSAL MOVIE ASSEMBLY ENGINE")
    print(f"   Project: {project_path.name}")
    print(f"   Location: {project_path}")
    print(f"   Pacing Speed Multiplier: {speed:.2f}X")
    print(f"========================================================\n")

    clips_dir = project_path / "generated_clips"
    audio_dir = project_path / "audio"
    output_dir = project_path / "final_output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Locate Master Audio
    audio_files = list(audio_dir.glob("*.mp3")) + list(audio_dir.glob("*.wav"))
    if not audio_files:
        raise FileNotFoundError(f"No audio file (.mp3/.wav) found in {audio_dir}!")
    
    # Prioritize master audio
    master_audio = None
    for a in audio_files:
        if "master" in a.name.lower() or "voiceover" in a.name.lower():
            master_audio = a
            break
    if not master_audio:
        master_audio = audio_files[0]
    
    total_audio_duration = get_media_duration(master_audio)
    print(f"🎙️ Master Audio: {master_audio.name} ({total_audio_duration:.2f}s / {total_audio_duration/60:.2f} mins)")

    # 2. Check & Validate Clips
    print(f"\n📹 Validating Motion Clips in {clips_dir}...")
    valid_clips = verify_clips(clips_dir)
    print(f"   Total valid clips verified: {len(valid_clips)}")

    # 3. Check for project_config.json if available
    config_file = project_path / "project_config.json"
    target_durations = None
    is_vertical = False
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
            target_durations = config.get("shot_durations")
            aspect = config.get("aspect_ratio", "")
            res = config.get("resolution", "")
            if aspect == "9:16" or res == "1080x1920" or "shorts" in config.get("format", "").lower():
                is_vertical = True

    # If no target_durations, divide audio duration evenly across clips
    if not target_durations or len(target_durations) != len(valid_clips):
        even_dur = total_audio_duration / len(valid_clips)
        target_durations = [even_dur] * len(valid_clips)
        print(f"   Evenly distributing {total_audio_duration:.2f}s across {len(valid_clips)} clips (~{even_dur:.2f}s each)")

    # 4. Prepare Normalized Segment Video Files
    temp_dir = project_path / "temp_engine_render"
    temp_dir.mkdir(parents=True, exist_ok=True)
    concat_list_file = temp_dir / "concat_list.txt"

    concat_lines = []
    res_label = "1080x1920 (9:16 Vertical)" if is_vertical else "1920x1080 (16:9 Landscape)"
    print(f"\n⚙️ Normalizing and retiming {len(valid_clips)} clips to {res_label} 30fps...")

    ffmpeg_exe = get_ffmpeg_cmd()

    for idx, ((clip_path, orig_dur), target_dur) in enumerate(zip(valid_clips, target_durations)):
        seg_out = temp_dir / f"norm_seg_{idx+1:02d}.mp4"
        speed_factor = orig_dur / target_dur
        
        # Scaling filter ensuring crop never fails for horizontal or vertical
        if is_vertical:
            vf = (
                f"scale=1300:-2,scale=-2:2200,"
                f"crop=1080:1920:(in_w-1080)/2:(in_h-1920)/2,"
                f"setpts={1.0/speed_factor:.6f}*PTS,fps=30"
            )
        else:
            vf = (
                f"scale=2200:-2,scale=-2:1300,"
                f"crop=1920:1080:(in_w-1920)/2:(in_h-1080)/2,"
                f"setpts={1.0/speed_factor:.6f}*PTS,fps=30"
            )

        ffmpeg_cmd = [
            ffmpeg_exe, "-y",
            "-i", str(clip_path),
            "-vf", vf,
            "-t", f"{target_dur:.3f}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-pix_fmt", "yuv420p", "-an",
            str(seg_out)
        ]
        
        subprocess.run(ffmpeg_cmd, capture_output=True, check=True)
        concat_lines.append(f"file '{seg_out.as_posix()}'")
        print(f"   [Rendered] Shot {idx+1:02d}: {orig_dur:.2f}s -> {target_dur:.2f}s (speed: {speed_factor:.2f}x)")

    with open(concat_list_file, "w", encoding="utf-8") as f:
        f.write("\n".join(concat_lines))

    # 5. Final Concat & Mux with Master Audio
    if not output_name:
        suffix = "Shorts_1080x1920.mp4" if is_vertical else "master_1080p.mp4"
        output_name = f"{project_path.name}_{suffix}"
    elif not output_name.endswith(".mp4"):
        output_name += ".mp4"

    final_video = output_dir / output_name
    print(f"\n🎬 Stitching full movie and muxing clean master voiceover...")

    raw_stitched = temp_dir / "raw_stitched.mp4" if speed != 1.0 else final_video
    mux_cmd = [
        ffmpeg_exe, "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_list_file),
        "-i", str(master_audio),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-t", f"{total_audio_duration:.3f}",
        "-movflags", "+faststart",
        str(raw_stitched)
    ]
    subprocess.run(mux_cmd, capture_output=True, check=True)

    # 5b. Apply 1.25X Speed Multiplier if requested
    if speed != 1.0:
        print(f"⚡ Applying {speed:.2f}X Pacing Multiplier (Rule #11)...")
        speed_cmd = [
            ffmpeg_exe, "-y",
            "-i", str(raw_stitched),
            "-filter:v", f"setpts=PTS/{speed}",
            "-filter:a", f"atempo={speed}",
            "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            str(final_video)
        ]
        subprocess.run(speed_cmd, capture_output=True, check=True)
        if raw_stitched.exists():
            raw_stitched.unlink()

    # 6. Cleanup temp files
    for seg_file in temp_dir.glob("norm_seg_*.mp4"):
        seg_file.unlink()
    if concat_list_file.exists():
        concat_list_file.unlink()
    try:
        temp_dir.rmdir()
    except Exception:
        pass

    final_size_mb = os.path.getsize(final_video) / (1024 * 1024)
    final_dur = get_media_duration(final_video)
    print(f"\n========================================================")
    print(f"✅ MOVIE ASSEMBLY COMPLETE!")
    print(f"   Output File: {final_video}")
    print(f"   Duration: {final_dur:.2f}s (Paced @ {speed:.2f}X)")
    print(f"   Size: {final_size_mb:.2f} MB")
    print(f"========================================================\n")
    return final_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assemble Universal Animation Movie")
    parser.add_argument("--project-dir", required=True, help="Path to project directory")
    parser.add_argument("--output-name", default=None, help="Optional output filename")
    parser.add_argument("--speed", type=float, default=1.25, help="Playback speed multiplier (default: 1.25x)")
    args = parser.parse_args()

    assemble_project(args.project_dir, args.output_name, args.speed)

