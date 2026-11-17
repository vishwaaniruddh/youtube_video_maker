"""Assemble the full 3-minute master movie integrating true AI motion video clips for key action scenes, synchronized with Hindi narration and CW watermark."""
import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"f:\YouTube\funny_village_mystery"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
OUT_VIDEO = os.path.join(BASE_DIR, "funny_village_mystery_complete_movie.mp4")
ff = imageio_ffmpeg.get_ffmpeg_exe()

def get_duration(path: str) -> float:
    proc = subprocess.run([ff, "-i", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            part = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = part.split(":")
            return int(h)*3600 + int(m)*60 + float(s)
    return 22.0

def main():
    print("==================================================")
    print("BUILDING COMPLETE MOVIE WITH REAL MOTION AI CLIPS")
    print("==================================================")
    
    concat_list = os.path.join(BASE_DIR, "concat_hybrid.txt")
    
    # 7 scenes definition:
    # Scene 1: Establishing morning (Image + slow push)
    # Scene 2: Shocked Halwai (Image + dramatic push into face)
    # Scene 3: Sarpanch panic (Image + wide pan)
    # Scene 4: REAL MOTION AI CLIP (Detective Chintu from PixVerse)
    # Scene 5: Sticky footprints (Image + macro tilt)
    # Scene 6: REAL MOTION AI CLIP (2K Monkey eating jalebi from Hailuo AI)
    # Scene 7: Village celebration (Image + pull-back)
    
    rendered_clips = []
    
    with open(concat_list, "w", encoding="utf-8") as f_concat:
        for i in range(1, 8):
            audio_path = os.path.join(AUDIO_DIR, f"scene_{i:02d}.mp3")
            dur = get_duration(audio_path) + 0.35
            dur_str = f"{dur:.2f}"
            out_clip = os.path.join(BASE_DIR, f"hybrid_scene_{i:02d}.mp4")
            
            if i == 4:
                # Real AI Motion Clip from PixVerse
                motion_src = os.path.join(BASE_DIR, "scene_04_real_motion.mp4")
                print(f"Integrating Scene 4 REAL AI MOTION CLIP ({dur_str}s)...")
                # Loop the 5s motion clip smoothly to cover the 26s narration
                cmd = [
                    ff, "-y",
                    "-stream_loop", "-1", "-i", motion_src,
                    "-i", audio_path,
                    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k",
                    "-t", dur_str,
                    out_clip
                ]
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
            elif i == 6:
                # Real 2K AI Motion Clip from Hailuo AI
                motion_src = os.path.join(BASE_DIR, "scene_06_real_motion.mp4")
                print(f"Integrating Scene 6 REAL 2K AI MOTION CLIP ({dur_str}s)...")
                # Loop the 5.17s 2K motion clip smoothly to cover the 27.5s narration
                cmd = [
                    ff, "-y",
                    "-stream_loop", "-1", "-i", motion_src,
                    "-i", audio_path,
                    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k",
                    "-t", dur_str,
                    out_clip
                ]
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
            else:
                # Cinematic camera motion on Gemini image
                img_path = os.path.join(BASE_DIR, f"scene_{i:02d}.png")
                print(f"Rendering Scene {i} Cinematic Motion ({dur_str}s)...")
                
                zoom_filter = "zoompan=z='min(zoom+0.0005,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
                if i == 2:
                    zoom_filter = "zoompan=z='min(zoom+0.0006,1.20)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-20':d=1:s=1920x1080:fps=30"
                elif i == 5:
                    zoom_filter = "zoompan=z='min(zoom+0.0006,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+40':d=1:s=1920x1080:fps=30"
                elif i == 7:
                    zoom_filter = "zoompan=z='max(1.15-0.0004*on,1.0)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
                    
                cmd = [
                    ff, "-y",
                    "-loop", "1", "-i", img_path,
                    "-i", audio_path,
                    "-vf", f"{zoom_filter},format=yuv420p",
                    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20",
                    "-c:a", "aac", "-b:a", "192k",
                    "-t", dur_str,
                    out_clip
                ]
                subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
            f_concat.write(f"file '{out_clip}'\n")
            rendered_clips.append(out_clip)
            print(f"  Scene {i} complete!")

    print("\nConcatenating all scenes...")
    concat_raw = os.path.join(BASE_DIR, "hybrid_concat_raw.mp4")
    subprocess.run([
        ff, "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c", "copy", concat_raw
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Final Pass: Burn Watermark & Episode Tag
    font_path = r"C:\Windows\Fonts\arialbd.ttf".replace("\\", "/").replace(":", "\\:")
    vf_final = [
        "drawbox=y=0:w=iw:h=120:color=black@0.35:t=fill",
        "drawbox=y=ih-140:w=iw:h=140:color=black@0.45:t=fill",
        f"drawtext=fontfile='{font_path}':text='CW • CARTOON WORLD':fontcolor=white@0.85:fontsize=36:x=w-tw-60:y=h-th-40:borderw=3:bordercolor=black@0.8",
        f"drawtext=fontfile='{font_path}':text='JAASOOS CHINTU • EPISODE 1':fontcolor=0xFFD600:fontsize=32:x=60:y=45:borderw=2:bordercolor=black"
    ]

    print("\nEncoding final polished broadcast movie...")
    subprocess.run([
        ff, "-y",
        "-i", concat_raw,
        "-vf", ",".join(vf_final),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-movflags", "+faststart",
        OUT_VIDEO
    ], check=True)
    
    print(f"\n==========================================")
    print(f"COMPLETE MOVIE RENDERED: {OUT_VIDEO}")
    print(f"File Size: {os.path.getsize(OUT_VIDEO)/(1024*1024):.2f} MB")
    print(f"==========================================")

if __name__ == "__main__":
    main()

