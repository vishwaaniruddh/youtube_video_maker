import os
import sys
import argparse
import subprocess
from PIL import Image

def generate_shorts_thumbnail(project_dir, bg_image=None, title_main="चालाक लोमड़ी", title_sub="जैसी करनी वैसी भरनी! 😱", badge_text="सारस का अनोखा बदला! ⚡", output_name="thumbnail_shorts.jpg"):
    base_dir = os.path.abspath(project_dir)
    final_output_dir = os.path.join(base_dir, "final_output")
    os.makedirs(final_output_dir, exist_ok=True)
    
    sample_images_dir = os.path.join(base_dir, "sample_images")
    if not bg_image:
        candidates = [
            os.path.join(sample_images_dir, "hero_thumbnail_artwork.jpg"),
            os.path.join(sample_images_dir, "scene_04_saaras_ki_chaal.jpg"),
            os.path.join(sample_images_dir, "scene_01_discovery.jpg"),
            os.path.join(sample_images_dir, "shot_master_character.png"),
        ]
        for c in candidates:
            if os.path.exists(c):
                bg_image = c
                break
        if not bg_image:
            # Pick any image in sample_images
            if os.path.exists(sample_images_dir):
                for f in os.listdir(sample_images_dir):
                    if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                        bg_image = os.path.join(sample_images_dir, f)
                        break

    if not bg_image or not os.path.exists(bg_image):
        print(f"Error: background image not found in {sample_images_dir}")
        return False

    bg_url = "file:///" + os.path.abspath(bg_image).replace("\\", "/")
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1080px;
    height: 1920px;
    position: relative;
    overflow: hidden;
    font-family: 'Nirmala UI', 'Segoe UI', Arial, sans-serif;
    background: #000;
  }}
  .bg {{
    position: absolute;
    top: 0;
    left: 0;
    width: 1080px;
    height: 1920px;
    object-fit: cover;
  }}
  .gradient-overlay {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(180deg, rgba(0,0,0,0.82) 0%, rgba(0,0,0,0.05) 25%, rgba(0,0,0,0.05) 72%, rgba(0,0,0,0.88) 100%);
    z-index: 5;
  }}
  .top-banner {{
    position: absolute;
    top: 75px;
    left: 0;
    width: 100%;
    text-align: center;
    z-index: 10;
  }}
  .title-main {{
    font-size: 130px;
    font-weight: 900;
    color: #FFE600;
    text-shadow: 
      0 0 35px #FF3300,
      6px 6px 0 #7A0000,
      -6px -6px 0 #7A0000,
      6px -6px 0 #7A0000,
      -6px 6px 0 #7A0000,
      0 15px 30px rgba(0,0,0,0.9);
    letter-spacing: 2px;
    line-height: 1.15;
  }}
  .title-sub {{
    display: inline-block;
    margin-top: 25px;
    background: linear-gradient(135deg, #FF0033, #80001A);
    color: #FFFFFF;
    font-size: 68px;
    font-weight: 900;
    padding: 18px 55px;
    border-radius: 60px;
    border: 5px solid #FFD700;
    box-shadow: 0 15px 35px rgba(0,0,0,0.85), 0 0 35px rgba(255, 0, 50, 0.85);
    text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
  }}
  .bottom-badge {{
    position: absolute;
    bottom: 85px;
    left: 0;
    width: 100%;
    text-align: center;
    z-index: 10;
  }}
  .badge-text {{
    display: inline-block;
    background: linear-gradient(135deg, #FFCC00, #FF6600);
    color: #000000;
    font-size: 62px;
    font-weight: 900;
    padding: 18px 55px;
    border-radius: 50px;
    border: 5px solid #FFFFFF;
    box-shadow: 0 15px 35px rgba(0,0,0,0.9);
    letter-spacing: 1px;
  }}
</style>
</head>
<body>
  <img class='bg' src='{bg_url}'>
  <div class='gradient-overlay'></div>
  <div class='top-banner'>
    <div class='title-main'>{title_main}</div>
    <div class='title-sub'>{title_sub}</div>
  </div>
  <div class='bottom-badge'>
    <div class='badge-text'>{badge_text}</div>
  </div>
</body>
</html>
"""
    temp_html = os.path.join(final_output_dir, "temp_thumb.html")
    temp_png = os.path.join(final_output_dir, "temp_thumb.png")
    final_jpg = os.path.join(final_output_dir, output_name)
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome):
        # Fallback to local appdata chrome
        chrome = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")

    html_file_url = "file:///" + os.path.abspath(temp_html).replace("\\", "/")
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1080,1920",
        "--allow-file-access-from-files",
        f"--screenshot={temp_png}",
        html_file_url
    ]
    subprocess.run(cmd, check=True)
    
    # Convert PNG to high quality JPG
    with Image.open(temp_png) as img:
        rgb_img = img.convert("RGB")
        rgb_img.save(final_jpg, "JPEG", quality=95)
        
    # Cleanup temps
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_png):
        os.remove(temp_png)
        
    print(f"✅ Shorts Thumbnail successfully generated: {final_jpg}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Universal Shorts Thumbnail Generator")
    parser.add_argument("--project-dir", required=True, help="Path to project directory")
    parser.add_argument("--bg-image", default=None, help="Background image path")
    parser.add_argument("--title-main", default="चालाक लोमड़ी", help="Main title (Hindi)")
    parser.add_argument("--title-sub", default="जैसी करनी वैसी भरनी! 😱", help="Sub title / Hook")
    parser.add_argument("--badge-text", default="सारस का अनोखा बदला! ⚡", help="Bottom badge text")
    parser.add_argument("--output-name", default="thumbnail_shorts.jpg", help="Output filename")
    args = parser.parse_args()
    
    generate_shorts_thumbnail(
        project_dir=args.project_dir,
        bg_image=args.bg_image,
        title_main=args.title_main,
        title_sub=args.title_sub,
        badge_text=args.badge_text,
        output_name=args.output_name
    )
