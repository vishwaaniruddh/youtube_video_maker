# 📜 Production Rules & Master Guidelines

## 🌟 Rule #0: Master Character Consistency Lock (Option A Locked)
- **Master Character Reference:** `sample_images/shot_08.png` (Cute boy detective Chintu with round sunglasses, trench coat, vintage bicycle).
- **Enforcement:** Detective Chintu वाले सभी वीडियो शॉट्स (Shot 08, 09, 10, 12, 18) **केवल Image-to-Video (I2V)** तकनीक से ही बनेंगे।
- कभी भी Chintu के लिए बिना `shot_08.png` रेफरेंस अटैच किए टेक्स्ट-टू-वीडियो प्रॉम्प्ट नहीं भेजा जाएगा, ताकि हर सीन में Chintu का चेहरा, चश्मा, कोट और स्टाइल 100% एक जैसा (Identical) रहे।

## 🛑 Rule #1: No Premature Assembly (कड़ाई से लागू)
- **जब तक प्रोजेक्ट की सारी 18 की 18 genuine AI motion clips पूरी तरह generate होकर `generated_clips/` फोल्डर में सेव और verify नहीं हो जातीं, तब तक फाइनल वीडियो assemble नहीं किया जाएगा।**
- कोई आधा-अधूरा ड्राफ्ट या प्री-मैच्योर रेंडर नहीं बनेगा।
- केवल तब ही assembly trigger होगी जब Shot 01 से लेकर Shot 18 तक के सभी वीडियो फाइल्स मौजूद हों:
  1. `generated_clips/shot_01_veo.mp4`
  2. `generated_clips/shot_02_veo.mp4`
  3. `generated_clips/shot_03_veo.mp4`
  4. `generated_clips/shot_04_veo.mp4`
  5. `generated_clips/shot_05_veo.mp4`
  6. `generated_clips/shot_06_veo.mp4`
  7. `generated_clips/shot_07_veo.mp4`
  8. `generated_clips/shot_08_veo.mp4` (Consistent Chintu)
  9. `generated_clips/shot_09_veo.mp4` (Consistent Chintu)
  10. `generated_clips/shot_10_veo.mp4` (Consistent Chintu)
  11. `generated_clips/shot_11_veo.mp4` (Syrup prints)
  12. `generated_clips/shot_12_veo.mp4` (Consistent Chintu)
  13. `generated_clips/shot_13_veo.mp4` (Banyan tree)
  14. `generated_clips/shot_14_veo.mp4` (Canopy eyes)
  15. `generated_clips/shot_15_veo.mp4` (Gappu monkey)
  16. `generated_clips/shot_16_hailuo.mp4` (Monkey eating jalebis)
  17. `generated_clips/shot_17_veo.mp4` (Village celebration)
  18. `generated_clips/shot_18_veo.mp4` (Consistent Chintu victory)

## 🎥 Rule #2: 100% Real Motion Animation Only
- किसी भी क्लिप में static photo slideshow या 2.5D camera zoom का इस्तेमाल नहीं होगा।
- हर माइक्रो-शॉट के लिए असली AI Motion Video Clip होना अनिवार्य है।

## 🎙️ Rule #3: Single Master Audio Mapping
- ElevenLabs का Master Voiceover ही फाइनल वीडियो के ऑडियो ट्रैक में सीधे mux होगा (strict 44100Hz Stereo AAC)।
