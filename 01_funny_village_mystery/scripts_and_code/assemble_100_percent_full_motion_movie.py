import os
import subprocess
import imageio_ffmpeg

BASE_DIR = r"F:\YouTube\funny_village_mystery"
CLIPS_DIR = os.path.join(BASE_DIR, "generated_clips")
AUDIO_FILE = os.path.join(BASE_DIR, "audio", "elevenlabs_master_voiceover.mp3")
FINAL_OUT = os.path.join(BASE_DIR, "final_output", "100_percent_real_motion_cartoon_movie.mp4")
TEMP_DIR = os.path.join(BASE_DIR, "temp_segments_final_100_percent")
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "final_output"), exist_ok=True)

ff = imageio_ffmpeg.get_ffmpeg_exe()

# Exact dialogue timestamps matching ElevenLabs voiceover sentence boundaries
# 100% of all 18 shots are REAL AI MOTION VIDEOS!
SHOTS = [
    {"id": 1, "fn": "shot_01_veo.mp4", "dur": 5.93, "desc": "Morning village establishing drone pan"},
    {"id": 2, "fn": "shot_02_veo.mp4", "dur": 6.56, "desc": "Halwai frying golden jalebis in wok"},
    {"id": 3, "fn": "shot_03_veo.mp4", "dur": 7.64, "desc": "Empty silver tray mystery push-in"},
    {"id": 4, "fn": "shot_04_veo.mp4", "dur": 8.78, "desc": "Halwai giant shock facial reaction"},
    {"id": 5, "fn": "shot_05_veo.mp4", "dur": 8.18, "desc": "Villagers running in panic"},
    {"id": 6, "fn": "shot_06_veo.mp4", "dur": 7.64, "desc": "Sarpanch trembling on wooden cot"},
    {"id": 7, "fn": "shot_07_veo.mp4", "dur": 7.95, "desc": "Villagers pointing at dark spooky forest"},
    {"id": 8, "fn": "shot_08_veo.mp4", "dur": 7.74, "desc": "Detective Chintu bicycle hero entry (Option A Consistent)"},
    {"id": 9, "fn": "shot_09_veo.mp4", "dur": 12.38, "desc": "Chintu holding magnifying glass Case Accepted!"},
    {"id": 10, "fn": "shot_10_veo.mp4", "dur": 7.72, "desc": "Chintu crawling & scanning ground (Option A Consistent)"},
    {"id": 11, "fn": "shot_11_veo.mp4", "dur": 9.31, "desc": "Sticky orange syrup pawprints camera tracking"},
    {"id": 12, "fn": "shot_12_veo.mp4", "dur": 5.88, "desc": "Chintu clever smirk & realization (Option A Consistent)"},
    {"id": 13, "fn": "shot_13_veo.mp4", "dur": 6.96, "desc": "Massive ancient banyan tree tilt-up to canopy"},
    {"id": 14, "fn": "shot_14_veo.mp4", "dur": 7.17, "desc": "Leaves parting reveal curious monkey face"},
    {"id": 15, "fn": "shot_15_veo.mp4", "dur": 10.49, "desc": "Gappu monkey wearing Sarpanch royal turban on branch"},
    {"id": 16, "fn": "shot_16_hailuo.mp4", "dur": 7.89, "desc": "Monkey caught red-handed stuffing jalebis into cheeks"},
    {"id": 17, "fn": "shot_17_veo.mp4", "dur": 7.83, "desc": "Sarpanch slaps forehead, villagers laughing hysterically"},
    {"id": 18, "fn": "shot_18_veo.mp4", "dur": 8.80, "desc": "Halwai rewards Chintu with jalebi box, victory celebration (Option A Consistent)"}
]

def render_segment(shot, out_path):
    src = os.path.join(CLIPS_DIR, shot["fn"])
    dur_str = f"{shot['dur']:.2f}"
    print(f"Encoding Shot {shot['id']:02d}: {shot['fn']} -> {dur_str}s ({shot['desc']})...")
    
    cmd = [
        ff, "-y",
        "-stream_loop", "-1",
        "-i", src,
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-an",
        "-t", dur_str,
        out_path
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        print(f"Error encoding shot {shot['id']}:", proc.stderr[-400:])
        raise RuntimeError(f"Encoding failed for shot {shot['id']}")

def main():
    print("=" * 60)
    print("🎬 MASTER FINAL CUT: 100% REAL AI MOTION MOVIE (18/18 SHOTS)")
    print("=" * 60)
    
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
    print("\nConcatenating all 18 Real Motion Video segments into single master track...")
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
    print("=" * 60)
    print(f"🎉 MASTER CARTOON MOVIE ASSEMBLED SUCCESSFULLY: {FINAL_OUT}")
    print(f"Final File Size: {os.path.getsize(FINAL_OUT):,} bytes")
    print("=" * 60)

if __name__ == "__main__":
    main()

