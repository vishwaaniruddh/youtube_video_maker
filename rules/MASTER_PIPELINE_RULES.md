# 📜 MASTER REPOSITORY PRODUCTION RULES & STANDARDS
**Workspace:** `F:\YouTube`  
**Purpose:** Universal Autonomous 3D Cartoon & Animation Production Engine

---

## 🏛️ ARCHITECTURE OVERVIEW: ENGINE vs PROJECTS

To maintain a clean, reusable repository:
1. **Central Engine (`engine/`):** Contains all universal scripts, video normalization, FFmpeg assembly, and SEO kit generators. No project-specific hardcoding.
2. **Central Rules (`rules/` & `GEMINI.md`):** Contains all operational rules, quality thresholds, and browser automation guidelines.
3. **Project Folders (`<project_slug>/`):** Contains ONLY project-specific content and generated media. No loose code files.

```text
F:\YouTube\
├── engine/                                  <-- UNIVERSAL TOOLS (Used for all projects)
│   ├── assemble_movie.py                    <-- Automatic 1080p assembly, retiming & audio mux
│   ├── init_project.py                      <-- Scaffolds new projects in 1-click
│   └── generate_youtube_kit.py              <-- Generates 5-part YouTube upload package
│
├── rules/                                   <-- REPOSITORY LAWS & GUIDES
│   ├── MASTER_PIPELINE_RULES.md             <-- THIS LAW BOOK
│   ├── CARTOON_SYSTEM_OPERATING_MANUAL.md   <-- Browser SOP for Gemini, Veo, ElevenLabs
│   └── MASTER_CARTOON_SYSTEM_GUIDE.md       <-- Theoretical chapters 1-6 summary
│
├── GEMINI.md                                <-- Auto-loaded root agent instructions
│
└── <project_name>/                          <-- PROJECT CONTENT ONLY (e.g. funny_village_mystery)
    ├── project_config.json                  <-- Metadata, target shots, aspect ratio
    ├── 01_script_and_storyboard.md          <-- Narrative, prompts, dialogue
    ├── sample_images/                       <-- Master character reference & shot stills
    ├── generated_clips/                     <-- 100% genuine AI motion video clips (.mp4)
    ├── audio/                               <-- Clean master voiceover (.mp3)
    ├── final_output/                        <-- Master Full HD video & ready thumbnail
    └── youtube_writeups/                    <-- Upload kit (Titles, Description, Tags, Endscreen)
```

---

## ⚖️ THE 6 IRON RULES OF PRODUCTION

### 🔴 RULE #0: CHARACTER CONSISTENCY LOCK (I2V MASTER REFERENCE)
* **Problem:** AI image/video generators create different facial structures or clothing for the same character across different prompts.
* **The Law:**
  1. In Phase 1/2, generate master reference shots and select **Option A** (Master Character Lock).
  2. Save this image permanently as `sample_images/shot_master_character.png`.
  3. Every subsequent shot featuring this character **MUST** use Image-to-Video (I2V) or paste this master reference image into Google Veo / Gemini prompt box before prompting action.
  4. Never generate blind Text-to-Video (T2V) for recurring characters.

---

### 🔴 RULE #1: ZERO PREMATURE ASSEMBLY (THE 100% CLIP LAW)
* **Problem:** Assembling the timeline when only 4 or 8 out of 18 clips are ready results in static freeze-frames or broken pacing.
* **The Law:**
  1. If a story has 18 shots, **ALL 18 CLIPS** must exist, be verified >100KB, and pass duration checks in `generated_clips/` BEFORE touching FFmpeg or video editors.
  2. The universal assembly script (`engine/assemble_movie.py`) will automatically abort with an error if any clip is missing.

---

### 🔴 RULE #2: 100% REAL VIDEO MOTION (ZERO SLIDESHOWS / ZERO FAKE PANS)
* **Problem:** Substituting still images with camera pan/zoom ("Ken Burns effect") degrades animation quality and violates production standards.
* **The Law:**
  1. Every single shot must be a genuine motion video clip (`.mp4`) generated via Google Gemini / Veo or Meta AI.
  2. Living motion must be visible: characters walking, blinking, smiling, water ripples, camera movement, or atmospheric particles.
  3. Never assemble a project using simulated still zooms or static images.

---

### 🔴 RULE #3: CLEAN MASTER AUDIO VIA ELEVENLABS (ZERO SPOKEN EMOTION TAGS)
* **Problem:** Text-to-Speech engines read bracketed instructions like `[Calm, Warm Tone]` aloud if not using Eleven v3 alpha.
* **The Law:**
  1. Master voiceover must be produced via ElevenLabs (`Eleven v3 alpha` or designated Hindi voice).
  2. All bracketed directives must be strictly stripped from the script before sending to TTS (unless using v3 alpha tag parsing).
  3. Master audio must be saved as `audio/master_voiceover.mp3` and verified clean before timing clips to it.

---

### 🔴 RULE #4: MODULAR PROJECT ISOLATION
* **The Law:**
  1. Never put custom python scripts inside project folders.
  2. Run `python engine/assemble_movie.py --project-dir <project_name>` from workspace root.
  3. Project folders must remain portable: transferring a project folder copies only creative content, assets, and metadata.

---

### 🔴 RULE #5: MULTI-ACCOUNT QUOTA ROTATION PROTOCOL
* **The Law:**
  1. When media generation quota is exhausted on the active account, switch to secondary accounts in Google Chrome:
     - `vishwaaniruddh@gmail.com`
     - `aniruddhvishwa@gmail.com`
     - `newaniruddh7@gmail.com`
     - `artivishwakarma1234@gmail.com`
  2. Maintain clip naming consistency (`shot_01_veo.mp4`, `shot_02_veo.mp4` ...) regardless of which account generated it.

---

### 🔴 RULE #6: STANDARDIZED YOUTUBE PACKAGING
* **The Law:** Every completed project must generate a standardized `youtube_writeups/` folder containing:
  1. `01_TITLE_OPTIONS.txt` (Minimum 3 high-CTR titles)
  2. `02_DESCRIPTION_AND_CHAPTERS.txt` (Synopsis, moral, and exact chapter timestamps matching audio duration)
  3. `03_TAGS_AND_HASHTAGS.txt` (400-500 character tag string ready for 1-click paste + hashtags)
  4. `04_CARDS_ENDSCREEN_SETTINGS.txt` (Category, Made for Kids = "No", 15s Endscreen window)
  5. `MASTER_YOUTUBE_UPLOAD_KIT.md` (All-in-one markdown reference)
  6. `thumbnail.jpg` (1280x720 HD)

---

### 🔴 RULE #7: 0–3s STARTING VIRAL HOOK (HIGH RETENTION LOCK)
* **Problem:** In YouTube Shorts, >40% swipe away in the first 2 seconds if the hook is slow or generic. Reach dies instantly.
* **The Law:**
  1. First 0–3 seconds of video & voiceover MUST start with high-stakes action, shocking visual, or intriguing curiosity hook.
  2. Never start with slow establishing shots (e.g. "एक गांव था..."). Start in medias res: "इस जादुई मुर्गी का पेट चीरने से पहले किसान ने क्या देखा?! 😱".
  3. Maintain "Stayed to Watch" >75% to trigger YouTube's algorithmic discovery pool.

---

### 🔴 RULE #8: ENDING ENGAGEMENT QUESTION (COMMENT & ALGORITHM DRIVER)
* **Problem:** 0 comments and 0 shares keep videos stuck at ~1.4K views even with decent retention.
* **The Law:**
  1. The final 3–5 seconds MUST pose an engaging moral dilemma, viewer debate, or choice.
  2. Example: "अगर आपके पास ये मुर्गी होती, तो आप क्या करते? लालच या समझदारी? नीचे कमेंट में बताओ! 👇".
  3. Drive viewer interaction to boost the video from Phase 1 (1.4K) to Phase 2 (10K–100K+).

---

### 🔴 RULE #9: OPTIMAL SHORTS DURATION (35–45s TARGET) & FAST MOTION
* **Problem:** 80-second shorts suffer retention drop-offs (<65% APV). YouTube algorithm strongly rewards >90–100% APV.
* **The Law:**
  1. Standard target duration for all YouTube Shorts is strictly **35–45 seconds** (5–6 shots × ~6–7s each).
  2. **Dynamic Fast Motion:** Prompt AI video models for fast-paced 3D animation, snappy character movements, and energetic camera pushes. Avoid slow cinematic drifts.
  3. Apply 1.15x–1.25x speed multiplier during final FFmpeg assembly to keep the pacing brisk, engaging, and tight.

---

### 🔴 RULE #10: EXACT-MATCH IMAGE-TO-VIDEO (I2V) PIPELINE
* **Problem:** Text-to-Video in Google Flow creates different random characters that do not match the approved storyboard or thumbnail.
* **The Law:**
  1. **Step 1 (Meta AI Keyframes):** Use Meta AI (`https://www.meta.ai/`) for rapid, superior-quality character and scene images using consistent detailed prompt descriptions.
  2. **Step 2 (Keyframe Coverage):** Generate one detailed keyframe image for every major scene/cut.
  3. **Step 3 (True I2V Animation):** In Google Flow (or video tool), upload the Meta AI image as the starting frame / reference (Image-to-Video / I2V) so the generated video 100% matches the character's facial structure, clothing, and environment.
  4. **Step 4 (High-CTR Thumbnail):** Use the highest-quality Meta AI hero image / collage with bold text overlays for the final YouTube Thumbnail.

---

### 🔴 RULE #11: MANDATORY 1.25X PACING & SPEED LAW
* **Problem:** Normal AI speech and video motion feel sluggish on mobile Shorts feeds, resulting in swipe-aways.
* **The Law:**
  1. All final videos and voiceovers MUST be rendered with a **1.25X speed multiplier** (`setpts=PTS/1.25` and `atempo=1.25`).
  2. Video pacing must remain snappy, high-tempo, and engaging from the very first frame to the ending comment question.

---

## 🚀 NEW PROJECT WORKFLOW (WHEN USER GIVES A NEW TOPIC)

When the user gives a new topic (e.g., *"Make a video on Haunted Old Haveli"*):
1. **Initialize Project:**
   ```powershell
   python engine/init_project.py --name "haunted_haveli_mystery" --title "हवेली का डरावना रहस्य"
   ```
2. **Draft Script & Micro-Chunks:**
   - Write `01_script_and_storyboard.md` in the project folder with 14-18 micro-chunk scenes.
3. **Lock Master Character (Rule #0):**
   - Generate character visual in Gemini/ChatGPT, present Option A, and save as `sample_images/shot_master_character.png`.
4. **Generate Clean Voiceover (Rule #3):**
   - Strip all bracketed tags. Generate master audio in ElevenLabs and save in `audio/master_voiceover.mp3`.
5. **Generate All Motion Video Clips (Rules #1, #2):**
   - Generate 18/18 clips using I2V with master reference. Save all in `generated_clips/`.
6. **Execute Universal Engine Assembly:**
   ```powershell
   python engine/assemble_movie.py --project-dir "haunted_haveli_mystery"
   ```
7. **Generate YouTube Kit:**
   ```powershell
   python engine/generate_youtube_kit.py --project-dir "haunted_haveli_mystery"
   ```

