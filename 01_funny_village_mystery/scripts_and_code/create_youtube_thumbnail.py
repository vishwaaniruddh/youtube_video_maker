import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

BASE_DIR = r"F:\YouTube\funny_village_mystery"
IMG_CHINTU = os.path.join(BASE_DIR, "sample_images", "shot_08.png")
IMG_MONKEY = os.path.join(BASE_DIR, "sample_images", "shot_15.png")
OUT_THUMB = os.path.join(BASE_DIR, "final_output", "thumbnail_youtube_ready.jpg")
FONT_PATH = r"C:\Windows\Fonts\NirmalaB.ttf"

def make_thumbnail():
    # 1. Base Canvas 1280x720
    canvas = Image.new("RGB", (1280, 720), (10, 10, 20))
    
    # 2. Right Half: Monkey Climax (Shot 15)
    im_monkey = Image.open(IMG_MONKEY).convert("RGB")
    im_monkey = im_monkey.resize((750, 720), Image.Resampling.LANCZOS)
    canvas.paste(im_monkey, (530, 0))
    
    # 3. Left Half: Detective Chintu (Shot 08)
    im_chintu = Image.open(IMG_CHINTU).convert("RGB")
    im_chintu = im_chintu.resize((650, 720), Image.Resampling.LANCZOS)
    
    # Create soft gradient mask for smooth cinematic split
    mask = Image.new("L", (650, 720), 255)
    for x in range(500, 650):
        alpha = int(255 * (1 - (x - 500) / 150))
        for y in range(720):
            mask.putpixel((x, y), alpha)
            
    canvas.paste(im_chintu, (0, 0), mask)
    
    # 4. Color pop and contrast boost
    enhancer = ImageEnhance.Color(canvas)
    canvas = enhancer.enhance(1.25)
    enhancer2 = ImageEnhance.Contrast(canvas)
    canvas = enhancer2.enhance(1.15)
    
    draw = ImageDraw.Draw(canvas)
    
    # 5. Top Headline Banner
    # Dark shadow band for high text legibility
    shadow_band = Image.new("RGBA", (1280, 150), (0, 0, 0, 190))
    canvas.paste(shadow_band, (0, 10), shadow_band)
    
    font_main = ImageFont.truetype(FONT_PATH, 56)
    font_sub = ImageFont.truetype(FONT_PATH, 42)
    font_badge = ImageFont.truetype(FONT_PATH, 28)
    
    # Top Text: गाँव का जलेबी चोर पकड़ा गया!
    text_top = "गाँव का जलेबी चोर पकड़ा गया! 😱"
    # Draw stroke / outline
    for dx in range(-4, 5):
        for dy in range(-4, 5):
            draw.text((640 + dx, 75 + dy), text_top, font=font_main, fill="black", anchor="mm")
    draw.text((640, 75), text_top, font=font_main, fill="#FFE600", anchor="mm") # bright yellow
    
    # 6. Bottom Banner: जासूस चीकू का धमाकेदार खुलासा!
    bottom_band = Image.new("RGBA", (1280, 110), (0, 0, 0, 210))
    canvas.paste(bottom_band, (0, 610), bottom_band)
    
    text_bottom = "जासूस चीकू का धमाकेदार खुलासा | FULL 3D MOVIE"
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            draw.text((640 + dx, 665 + dy), text_bottom, font=font_sub, fill="black", anchor="mm")
    draw.text((640, 665), text_bottom, font=font_sub, fill="#FFFFFF", anchor="mm") # crisp white
    
    # 7. Channel Badge: DREAM BYTE
    draw.rounded_rectangle([30, 25, 230, 65], radius=8, fill="#FF0000", outline="white", width=2)
    draw.text((130, 44), "DREAM BYTE", font=font_badge, fill="white", anchor="mm")
    
    # 8. Save Thumbnail (<2MB standard JPEG)
    canvas.save(OUT_THUMB, "JPEG", quality=92, optimize=True)
    print(f"YouTube Thumbnail created: {OUT_THUMB}")
    print("Size:", os.path.getsize(OUT_THUMB), "bytes")

if __name__ == "__main__":
    make_thumbnail()

