import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"F:\YouTube\funny_village_mystery"
IMAGES_DIR = os.path.join(BASE_DIR, "sample_images")
CLIPS_DIR = os.path.join(BASE_DIR, "generated_clips")
AUDIO_FILE = os.path.join(BASE_DIR, "audio", "elevenlabs_master_voiceover.mp3")
FINAL_OUT = os.path.join(BASE_DIR, "final_output", "100_percent_real_motion_cartoon_movie.mp4")
TEMP_DIR = os.path.join(BASE_DIR, "temp_segments_v2")
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "final_output"), exist_ok=True)

ff = imageio_ffmpeg.get_ffmpeg_exe()

# Exact dialogue timestamps based on ElevenLabs silence midpoints
# 11 REAL MOTION CLIPS + 7 high-impact micro-shots
SHOTS = [
    {
        "id": 1,
        "name": "shot_01_morning_village",
        "dur": 5.93,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_01_veo.mp4")
    },
    {
        "id": 2,
        "name": "shot_02_halwai_frying",
        "dur": 6.56,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_02_veo.mp4")
    },
    {
        "id": 3,
        "name": "shot_03_empty_tray",
        "dur": 7.64,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_03_veo.mp4")
    },
    {
        "id": 4,
        "name": "shot_04_halwai_shock",
        "dur": 8.78,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_04_veo.mp4")
    },
    {
        "id": 5,
        "name": "shot_05_villagers_panic",
        "dur": 8.18,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_05_veo.mp4")
    },
    {
        "id": 6,
        "name": "shot_06_sarpanch_trembling",
        "dur": 7.64,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_06_veo.mp4")
    },
    {
        "id": 7,
        "name": "shot_07_spooky_forest_pointing",
        "dur": 7.95,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_07_veo.mp4")
    },
    {
        "id": 8,
        "name": "shot_08_chintu_bicycle_entry",
        "dur": 7.74,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_08_pixverse.mp4"),
        "fallback_img": os.path.join(IMAGES_DIR, "shot_08.png")
    },
    {
        "id": 9,
        "name": "shot_09_case_accepted",
        "dur": 12.38,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_09.png"),
        "vf": "scale=2200:-2,crop=1920:1080:(in_w-out_w)/2:(in_h-out_h)*(t/12.38),fps=30,format=yuv420p"
    },
    {
        "id": 10,
        "name": "shot_10_crawling_investigation",
        "dur": 7.72,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_10.png"),
        "vf": "scale=-2:1200,crop=1920:1080:(in_w-out_w)*(t/7.72):0,fps=30,format=yuv420p"
    },
    {
        "id": 11,
        "name": "shot_11_syrup_pawprints",
        "dur": 9.31,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_11.png"),
        "vf": "scale=2150:-2,crop=1920:1080:(in_w-out_w)*(t/9.31):(in_h-out_h)*(t/9.31),fps=30,format=yuv420p"
    },
    {
        "id": 12,
        "name": "shot_12_chintu_smirk",
        "dur": 5.88,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_12.png"),
        "vf": "scale=2100:-2,crop=1920:1080:(in_w-out_w)*(t/5.88):(in_h-out_h)/2,fps=30,format=yuv420p"
    },
    {
        "id": 13,
        "name": "shot_13_ancient_banyan_tree",
        "dur": 6.96,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_13.png"),
        "vf": "scale=-2:1300,crop=1920:1080:(in_w-out_w)/2:(in_h-out_h)*(1-t/6.96),fps=30,format=yuv420p"
    },
    {
        "id": 14,
        "name": "shot_14_eyes_in_canopy",
        "dur": 7.17,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_14.png"),
        "vf": "scale=2200:-2,crop=1920:1080:(in_w-out_w)/2:(in_h-out_h)*(t/7.17),fps=30,format=yuv420p"
    },
    {
        "id": 15,
        "name": "shot_15_monkey_sarpanch_turban",
        "dur": 10.49,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_15_veo.mp4")
    },
    {
        "id": 16,
        "name": "shot_16_monkey_stuffing_jalebis",
        "dur": 7.89,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_16_hailuo.mp4")
    },
    {
        "id": 17,
        "name": "shot_17_sarpanch_villagers_laughing",
        "dur": 7.83,
        "type": "video",
        "src": os.path.join(CLIPS_DIR, "shot_17_veo.mp4")
    },
    {
        "id": 18,
        "name": "shot_18_chintu_reward_case_closed",
        "dur": 8.80,
        "type": "motion_image",
        "src": os.path.join(IMAGES_DIR, "shot_18.png"),
        "vf": "scale=2200:-2,crop=1920:1080:(in_w-out_w)*(1-t/8.80):(in_h-out_h)*(1-t/8.80),fps=30,format=yuv420p"
    }
]

def render_segment(shot, out_path):
    dur = shot["dur"]
    dur_str = f"{dur:.2f}"
    
    if shot["type"] == "video" and os.path.exists(shot["src"]):
        print(f"Rendering Real Motion Video Clip for Shot {shot['id']} ({dur_str}s)...")
        # Loop video if shot duration is slightly longer than clip
        cmd = [
            ff, "-y",
            "-stream_loop", "-1",
            "-i", shot["src"],
            "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-an",
            "-t", dur_str,
            out_path
        ]
    else:
        src_img = shot["src"] if shot["type"] == "motion_image" else shot.get("fallback_img")
        print(f"Rendering 2.5D Animated Motion for Shot {shot['id']} ({dur_str}s)...")
        vf = shot.get("vf")
        cmd = [
            ff, "-y",
            "-loop", "1", "-i", src_img,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-an",
            "-t", dur_str,
            out_path
        ]
        
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        print(f"Error rendering shot {shot['id']}:", proc.stderr[-500:])
        raise RuntimeError(f"Shot {shot['id']} render failed")

def main():
    segment_files = []
    for shot in SHOTS:
        seg_out = os.path.join(TEMP_DIR, f"seg_{shot['id']:02d}.mp4")
        render_segment(shot, seg_out)
        segment_files.append(seg_out)
        
    concat_list_path = os.path.join(TEMP_DIR, "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for p in segment_files:
            safe_p = p.replace("\\", "/")
            f.write(f"file '{safe_p}'\n")
            
    temp_concat_video = os.path.join(TEMP_DIR, "concat_raw.mp4")
    print("\nConcatenating all 18 segments into unified video track...")
    concat_cmd = [
        ff, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        temp_concat_video
    ]
    subprocess.run(concat_cmd, check=True)
    
    print("\nMuxing with ElevenLabs Master Voiceover (strict 44100Hz stereo AAC)...")
    final_mux_cmd = [
        ff, "-y",
        "-i", temp_concat_video,
        "-i", AUDIO_FILE,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",
        "-ac", "2",
        "-shortest",
        "-movflags", "+faststart",
        FINAL_OUT
    ]
    subprocess.run(final_mux_cmd, check=True)
    print(f"\n Master Cartoon Movie successfully assembled: {FINAL_OUT}")
    print("File size:", os.path.getsize(FINAL_OUT), "bytes")

if __name__ == "__main__":
    main()
