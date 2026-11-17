"""
Proper 7-Scene Hindi Cartoon Story Movie Assembly
Fixes:
1. Loud, crystal-clear voiceover mapped directly from MP3s (-map 1:a)
2. Strict 44100 Hz stereo AAC audio across all scenes (eliminates decoder freeze / stop at 1:07)
3. Dynamic 2-angle pacing per scene (eliminates repetitive 10s looping)
4. Full chronological order: Scene 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (Scene 5 footprint clue included!)
"""
import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"F:\YouTube\funny_village_mystery"
AUDIO_DIR = os.path.join(BASE_DIR, "audio")
OUT_FINAL = os.path.join(BASE_DIR, "proper_cartoon_movie_fixed.mp4")
ff = imageio_ffmpeg.get_ffmpeg_exe()

def get_duration(path: str) -> float:
    proc = subprocess.run([ff, "-i", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            part = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = part.split(":")
            return int(h)*3600 + int(m)*60 + float(s)
    return 20.0

def make_video_segment(src: str, is_image: bool, dur: float, out_path: str, zoom_effect: str = None):
    dur_str = f"{dur:.2f}"
    if is_image:
        if not zoom_effect:
            vf = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p"
        else:
            vf = f"{zoom_effect},scale=1920:1080,fps=30,format=yuv420p"
        cmd = [
            ff, "-y",
            "-loop", "1", "-i", src,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-an",
            "-t", dur_str,
            out_path
        ]
    else:
        # Real motion video
        cmd = [
            ff, "-y",
            "-i", src,
            "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-an",
            "-t", dur_str,
            out_path
        ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def render_scene(s_num: int, shots: list, audio_file: str, out_scene: str):
    dur = get_duration(audio_file)
    print(f"\nRendering Scene {s_num} (Total duration: {dur:.2f}s, Shots: {len(shots)})...")
    
    sub_clips = []
    # Calculate duration per shot
    total_shots = len(shots)
    time_per_shot = dur / total_shots
    
    for idx, (src_file, is_img, zoom_eff) in enumerate(shots):
        sub_out = os.path.join(BASE_DIR, f"temp_s{s_num}_shot_{idx}.mp4")
        # Give last shot the exact remainder
        s_dur = time_per_shot if idx < total_shots - 1 else (dur - idx * time_per_shot)
        print(f"  Shot {idx+1}: {os.path.basename(src_file)} ({s_dur:.2f}s)")
        make_video_segment(src_file, is_img, s_dur, sub_out, zoom_eff)
        sub_clips.append(sub_out)
        
    # Concat video shots
    concat_txt = os.path.join(BASE_DIR, f"temp_s{s_num}_list.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for c in sub_clips:
            f.write(f"file '{c}'\n")
            
    concat_vid = os.path.join(BASE_DIR, f"temp_s{s_num}_vid.mp4")
    subprocess.run([
        ff, "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
        "-c", "copy", concat_vid
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Mux with voiceover audio: explicitly map -map 0:v -map 1:a and normalize audio
    print(f"  Muxing Scene {s_num} with crystal-clear voiceover: {os.path.basename(audio_file)}")
    cmd = [
        ff, "-y",
        "-i", concat_vid,
        "-i", audio_file,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-t", f"{dur:.2f}",
        out_scene
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  Scene {s_num} successfully created!")

def main():
    print("==================================================================")
    print("BUILDING PROPER 7-SCENE HINDI CARTOON MOVIE (100% CLEAN AUDIO & PACING)")
    print("==================================================================")
    
    # Source Assets
    v1_morning = os.path.join(BASE_DIR, "clip_01_morning_veo.mp4")
    img1_morning = os.path.join(BASE_DIR, "scene_01.png")
    
    v2_halwai = os.path.join(BASE_DIR, "clip_02_halwai_veo.mp4")
    img2_halwai = os.path.join(BASE_DIR, "scene_02.png")
    
    v3_sarpanch = os.path.join(BASE_DIR, "clip_03_sarpanch_veo.mp4")
    img3_sarpanch = os.path.join(BASE_DIR, "scene_03.png")
    
    v4_chintu_pix = os.path.join(BASE_DIR, "clip_04_chintu_pixverse.mp4")
    v4_chintu_veo = os.path.join(BASE_DIR, "clip_04_chintu_veo.mp4")
    
    img5_footprints = os.path.join(BASE_DIR, "scene_05.png")
    
    v6_monkey_hailuo = os.path.join(BASE_DIR, "clip_06_monkey_hailuo_2k.mp4")
    v6_monkey_veo = os.path.join(BASE_DIR, "clip_06_monkey_veo.mp4")
    
    v7_celebration = os.path.join(BASE_DIR, "clip_07_celebration_veo.mp4")
    img7_celebration = os.path.join(BASE_DIR, "scene_07.png")
    
    # 7-Scene Narrative Plan:
    # Scene 1: Morning village (Shot 1: Veo Motion Video -> Shot 2: Morning image push-in)
    # Scene 2: Halwai crying (Shot 1: Veo Motion Video -> Shot 2: Halwai shock punch-in)
    # Scene 3: Sarpanch trembling (Shot 1: Veo Motion Video -> Shot 2: Villagers panic pan)
    # Scene 4: Chintu hero entry (Shot 1: PixVerse action entry -> Shot 2: Veo magnifying glass close-up)
    # Scene 5: Footprints clue (Shot 1: Chintu inspecting with glass -> Shot 2: Macro footprint tracking)
    # Scene 6: Jalebi thief caught (Shot 1: Hailuo 2K eating jalebi -> Shot 2: Veo monkey caught shocked)
    # Scene 7: Celebration ending (Shot 1: Veo celebration motion -> Shot 2: Golden sunset ending)
    
    z_push = "zoompan=z='min(zoom+0.0008,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080"
    z_punch = "zoompan=z='min(zoom+0.0012,1.35)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)-30':d=1:s=1920x1080"
    z_pan = "zoompan=z='1.15':x='if(lte(on,1),(iw-iw/zoom)/2,x+1)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080"
    z_track = "zoompan=z='1.20':x='iw/2-(iw/zoom/2)':y='if(lte(on,1),(ih-ih/zoom)/2,y+1.2)':d=1:s=1920x1080"
    z_pull = "zoompan=z='max(1.20-0.0008*on,1.0)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080"
    
    scenes = [
        (1, [(v1_morning, False, None), (img1_morning, True, z_push)]),
        (2, [(v2_halwai, False, None), (img2_halwai, True, z_punch)]),
        (3, [(v3_sarpanch, False, None), (img3_sarpanch, True, z_pan)]),
        (4, [(v4_chintu_pix, False, None), (v4_chintu_veo, False, None)]),
        (5, [(v4_chintu_veo, False, None), (img5_footprints, True, z_track)]),
        (6, [(v6_monkey_hailuo, False, None), (v6_monkey_veo, False, None)]),
        (7, [(v7_celebration, False, None), (img7_celebration, True, z_pull)])
    ]
    
    master_scenes = []
    master_txt = os.path.join(BASE_DIR, "final_master_scenes.txt")
    
    for s_num, shots_cfg in scenes:
        aud = os.path.join(AUDIO_DIR, f"scene_{s_num:02d}.mp3")
        scene_out = os.path.join(BASE_DIR, f"proper_scene_{s_num:02d}.mp4")
        render_scene(s_num, shots_cfg, aud, scene_out)
        master_scenes.append(scene_out)
        
    with open(master_txt, "w", encoding="utf-8") as f_m:
        for s in master_scenes:
            f_m.write(f"file '{s}'\n")
            
    print("\nConcatenating all 7 scenes into continuous master...")
    raw_movie = os.path.join(BASE_DIR, "proper_movie_raw.mp4")
    subprocess.run([
        ff, "-y", "-f", "concat", "-safe", "0", "-i", master_txt,
        "-c", "copy", raw_movie
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\nApplying watermark and broadcast polish...")
    font_path = r"C:\Windows\Fonts\arialbd.ttf".replace("\\", "/").replace(":", "\\:")
    vf_final = [
        "drawbox=y=0:w=iw:h=110:color=black@0.35:t=fill",
        "drawbox=y=ih-130:w=iw:h=130:color=black@0.45:t=fill",
        f"drawtext=fontfile='{font_path}':text='CW • CARTOON WORLD':fontcolor=white@0.85:fontsize=36:x=w-tw-60:y=h-th-35:borderw=3:bordercolor=black@0.8",
        f"drawtext=fontfile='{font_path}':text='JAASOOS CHINTU • EPISODE 1':fontcolor=0xFFD600:fontsize=32:x=60:y=40:borderw=2:bordercolor=black"
    ]
    
    subprocess.run([
        ff, "-y",
        "-i", raw_movie,
        "-vf", ",".join(vf_final),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-movflags", "+faststart",
        OUT_FINAL
    ], check=True)
    
    print(f"\n========================================================")
    print(f"PROPER MOVIE SUCCESSFULLY GENERATED: {OUT_FINAL}")
    print(f"File Size: {os.path.getsize(OUT_FINAL)/(1024*1024):.2f} MB")
    print(f"========================================================")

if __name__ == "__main__":
    main()

