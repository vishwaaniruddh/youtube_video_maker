"""
Master Multi-Cut Motion Video Assembly
Combines genuine AI motion video clips (Google Veo 10s, Hailuo 2K, PixVerse)
Synchronized with full Hindi storytelling narration, cinematic cuts, and broadcast watermark.
Zero static slideshow feel - multi-shot dynamic pacing.
"""
import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"F:\YouTube\funny_village_mystery"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
OUT_FINAL = os.path.join(BASE_DIR, "100_percent_real_motion_cartoon_movie.mp4")
ff = imageio_ffmpeg.get_ffmpeg_exe()

def get_duration(path: str) -> float:
    proc = subprocess.run([ff, "-i", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            part = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = part.split(":")
            return int(h)*3600 + int(m)*60 + float(s)
    return 20.0

def build_scene(scene_num: int, video_sources: list, audio_path: str, out_path: str):
    dur = get_duration(audio_path) + 0.35
    dur_str = f"{dur:.2f}"
    print(f"Building Scene {scene_num} ({dur_str}s) with {len(video_sources)} AI motion sources...")

    # We scale and pad all motion clips to 1920x1080 30fps
    if len(video_sources) == 1:
        src = video_sources[0]
        # Smooth loop with ping-pong or stream loop
        cmd = [
            ff, "-y",
            "-stream_loop", "-1", "-i", src,
            "-i", audio_path,
            "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-t", dur_str,
            out_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # Multi-cut between the video sources (e.g. shot 1 for first half, shot 2 for second half)
        half_dur = dur / len(video_sources)
        sub_clips = []
        for idx, src in enumerate(video_sources):
            sub_out = os.path.join(BASE_DIR, f"temp_scene_{scene_num}_sub_{idx}.mp4")
            s_dur = f"{half_dur + 0.1:.2f}"
            c_cmd = [
                ff, "-y",
                "-stream_loop", "-1", "-i", src,
                "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
                "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-an",
                "-t", s_dur,
                sub_out
            ]
            subprocess.run(c_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            sub_clips.append(sub_out)
        
        # Concat sub clips
        sub_list_txt = os.path.join(BASE_DIR, f"temp_list_{scene_num}.txt")
        with open(sub_list_txt, "w", encoding="utf-8") as f_sub:
            for s in sub_clips:
                f_sub.write(f"file '{s}'\n")
        
        concat_raw = os.path.join(BASE_DIR, f"temp_scene_{scene_num}_concat.mp4")
        subprocess.run([
            ff, "-y", "-f", "concat", "-safe", "0", "-i", sub_list_txt,
            "-c", "copy", concat_raw
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Mux with scene audio
        cmd = [
            ff, "-y",
            "-i", concat_raw,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k",
            "-t", dur_str,
            out_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  Scene {scene_num} complete!")

def main():
    print("==================================================================")
    print("ASSEMBLING 100% REAL MOTION CARTOON MOVIE (GOOGLE VEO + HAILUO 2K)")
    print("==================================================================")

    # All genuine AI motion sources
    v1_morning = os.path.join(BASE_DIR, "clip_01_morning_veo.mp4")
    v2_halwai = os.path.join(BASE_DIR, "clip_02_halwai_veo.mp4")
    v3_sarpanch = os.path.join(BASE_DIR, "clip_03_sarpanch_veo.mp4")
    v4_chintu_veo = os.path.join(BASE_DIR, "clip_04_chintu_veo.mp4")
    v4_chintu_pix = os.path.join(BASE_DIR, "clip_04_chintu_pixverse.mp4")
    v6_monkey_veo = os.path.join(BASE_DIR, "clip_06_monkey_veo.mp4")
    v6_monkey_hailuo = os.path.join(BASE_DIR, "clip_06_monkey_hailuo_2k.mp4")
    v7_celebration = os.path.join(BASE_DIR, "clip_07_celebration_veo.mp4")

    # Multi-cut arrangement:
    # Scene 1: Morning village (Veo 10s motion)
    # Scene 2: Halwai crying empty wok (Veo 10s motion)
    # Scene 3: Sarpanch trembling on cot (Veo 10s motion)
    # Scene 4: Chintu hero entry (Cut 1: PixVerse action smirk -> Cut 2: Veo close-up magnifying glass)
    # Scene 5: Investigation (Cut 1: Chintu tracking -> Cut 2: Morning village path)
    # Scene 6: The Reveal (Cut 1: Hailuo 2K eating jalebis -> Cut 2: Veo caught red-handed monkey)
    # Scene 7: Village Celebration (Veo 10s celebration motion)

    scenes_config = [
        (1, [v1_morning]),
        (2, [v2_halwai]),
        (3, [v3_sarpanch]),
        (4, [v4_chintu_pix, v4_chintu_veo]),
        (5, [v4_chintu_veo, v1_morning]),
        (6, [v6_monkey_hailuo, v6_monkey_veo]),
        (7, [v7_celebration])
    ]

    scene_clips = []
    concat_list = os.path.join(BASE_DIR, "concat_100_motion.txt")

    with open(concat_list, "w", encoding="utf-8") as f_out:
        for s_num, srcs in scenes_config:
            aud = os.path.join(AUDIO_DIR, f"scene_{s_num:02d}.mp3")
            out_c = os.path.join(BASE_DIR, f"motion_master_scene_{s_num:02d}.mp4")
            build_scene(s_num, srcs, aud, out_c)
            f_out.write(f"file '{out_c}'\n")
            scene_clips.append(out_c)

    # Concat all scenes
    print("\nConcatenating all scenes into master sequence...")
    concat_raw = os.path.join(BASE_DIR, "concat_motion_raw.mp4")
    subprocess.run([
        ff, "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
        "-c", "copy", concat_raw
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Burn cinematic watermark & broadcast badge
    font_path = r"C:\Windows\Fonts\arialbd.ttf".replace("\\", "/").replace(":", "\\:")
    vf_final = [
        "drawbox=y=0:w=iw:h=110:color=black@0.35:t=fill",
        "drawbox=y=ih-130:w=iw:h=130:color=black@0.45:t=fill",
        f"drawtext=fontfile='{font_path}':text='CW • CARTOON WORLD':fontcolor=white@0.85:fontsize=36:x=w-tw-60:y=h-th-35:borderw=3:bordercolor=black@0.8",
        f"drawtext=fontfile='{font_path}':text='JAASOOS CHINTU • EPISODE 1':fontcolor=0xFFD600:fontsize=32:x=60:y=40:borderw=2:bordercolor=black"
    ]

    print("\nEncoding final polished broadcast movie...")
    subprocess.run([
        ff, "-y",
        "-i", concat_raw,
        "-vf", ",".join(vf_final),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "copy",
        "-movflags", "+faststart",
        OUT_FINAL
    ], check=True)

    print(f"\n========================================================")
    print(f"100% REAL MOTION CARTOON MOVIE ASSEMBLED: {OUT_FINAL}")
    print(f"File Size: {os.path.getsize(OUT_FINAL)/(1024*1024):.2f} MB")
    print(f"========================================================")

if __name__ == "__main__":
    main()

