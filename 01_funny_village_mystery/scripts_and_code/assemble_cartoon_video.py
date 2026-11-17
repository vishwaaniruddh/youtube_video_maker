"""Assemble the 7-scene 3-minute cinematic Hindi cartoon video with dynamic motion, subtitles, and audio synchronization."""
import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"f:\YouTube\funny_village_mystery"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
OUT_VIDEO = os.path.join(BASE_DIR, "jalebi_chor_ka_raaz_full_movie.mp4")
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
    print("Preparing 7 scenes with cinematic camera movement & audio sync...")
    
    scene_clips = []
    concat_list = os.path.join(BASE_DIR, "concat_scenes.txt")
    
    # Motion styles: alternating gentle push-in, push-out, subtle drift
    motions = [
        # Scene 1: Gentle slow zoom-in on village
        "zoompan=z='min(zoom+0.0004,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30",
        # Scene 2: Dramatic push into the shocked Halwai's face
        "zoompan=z='min(zoom+0.0006,1.20)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-20':d=1:s=1920x1080:fps=30",
        # Scene 3: Wide camera drift across the panicking villagers
        "zoompan=z='1.10':x='if(lte(on,-1),(x-1),x+0.5)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30",
        # Scene 4: Heroic slow push into Detective Chintu
        "zoompan=z='min(zoom+0.0005,1.18)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-30':d=1:s=1920x1080:fps=30",
        # Scene 5: Macro camera tilt & zoom along the syrupy footprints
        "zoompan=z='min(zoom+0.0006,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)+40':d=1:s=1920x1080:fps=30",
        # Scene 6: Dramatic reveal push into the cheeky monkey in the banyan tree
        "zoompan=z='min(zoom+0.0007,1.22)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-20':d=1:s=1920x1080:fps=30",
        # Scene 7: Joyful slow pull-back revealing the whole celebrating village
        "zoompan=z='max(1.15-0.0004*on,1.0)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=30"
    ]
    
    with open(concat_list, "w", encoding="utf-8") as f_concat:
        for i in range(1, 8):
            img_path = os.path.join(BASE_DIR, f"scene_{i:02d}.png")
            audio_path = os.path.join(AUDIO_DIR, f"scene_{i:02d}.mp3")
            dur = get_duration(audio_path) + 0.35
            out_clip = os.path.join(BASE_DIR, f"scene_{i:02d}_motion.mp4")
            
            motion_filter = motions[i-1]
            dur_str = f"{dur:.2f}"
            
            print(f"Rendering Scene {i} Motion Clip ({dur_str}s)...")
            cmd = [
                ff, "-y",
                "-loop", "1", "-i", img_path,
                "-i", audio_path,
                "-vf", f"{motion_filter},format=yuv420p",
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "20",
                "-c:a", "aac", "-b:a", "192k",
                "-t", dur_str,
                out_clip
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            f_concat.write(f"file '{out_clip}'\n")
            scene_clips.append(out_clip)
            print(f"  Scene {i} motion clip ready!")

    print("\nConcatenating all 7 scenes into continuous movie track...")
    concat_raw = os.path.join(BASE_DIR, "full_movie_raw.mp4")
    subprocess.run([
        ff, "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c", "copy", concat_raw
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Concatenation complete!")

    # Final Pass: Overlay Watermark & Vignette as taught in Chapter 5
    font_path = r"C:\Windows\Fonts\arialbd.ttf".replace("\\", "/").replace(":", "\\:")
    vf_final = [
        "drawbox=y=0:w=iw:h=120:color=black@0.35:t=fill",
        "drawbox=y=ih-140:w=iw:h=140:color=black@0.45:t=fill",
        # Watermark in bottom-right corner as taught in Chapter 5
        f"drawtext=fontfile='{font_path}':text='CW • CARTOON WORLD':fontcolor=white@0.85:fontsize=36:x=w-tw-60:y=h-th-40:borderw=3:bordercolor=black@0.8",
        # Subtle episode header on top
        f"drawtext=fontfile='{font_path}':text='JAASOOS CHINTU • EPISODE 1':fontcolor=0xFFD600:fontsize=32:x=60:y=45:borderw=2:bordercolor=black"
    ]

    print("\nEncoding final polished master video...")
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
    print(f"MASTER MOVIE RENDERED: {OUT_VIDEO}")
    print(f"File Size: {os.path.getsize(OUT_VIDEO)/(1024*1024):.2f} MB")
    print(f"==========================================")

if __name__ == "__main__":
    main()

