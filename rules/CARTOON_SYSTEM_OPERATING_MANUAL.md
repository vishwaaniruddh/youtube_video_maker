# 🚀 CARTOON VIDEO PRODUCTION SYSTEM — MASTER OPERATING MANUAL

> **Operating Standard:** This manual governs the creation of all animated cartoon videos in this workspace. It translates the 6-chapter training curriculum (`chapter 1.mp4` through `CHAPTER 6.mp4`) into a fully operational, browser-driven AI production pipeline.

---

## 🤝 Creative Partnership & Role Definition

1. **Your Role (The Creator):**
   - You provide topic approval, creative direction, and complete portal logins (ChatGPT, Google Gemini, Meta AI, ElevenLabs, YouTube Studio) in Google Chrome.
2. **My Role (Your AI Production Partner & Co-Pilot):**
   - I control the Google Chrome browser and command-line pipelines.
   - I write the scripts, input the prompts, trigger image/video generations, extract voiceovers, assemble and sync the final video, package SEO metadata, and prepare the uploads.
   - I will never leave you stuck. Whenever login or human verification is needed, I will prompt you clearly, wait for your confirmation, and immediately take over the workflow.

---

## 🧭 The 6-Phase Master Execution Pipeline & Generic Architecture

> **Architecture Rule:** All code and assembly tools are centralized in `F:\YouTube\engine/`. Project folders (e.g. `funny_village_mystery/`) contain only creative content and generated media. See `rules/MASTER_PIPELINE_RULES.md` for full rules.

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                           BROWSER-DRIVEN PIPELINE                              │
├─────────────────┬─────────────────┬─────────────────┬──────────────────────────┤
│ 1. CHATGPT      │ 2. GEMINI       │ 3. META / VEO   │ 4. ELEVENLABS            │
│ Script & Prompts│ 16:9 HD Images  │ Motion MP4 Clips│ Clean Voiceover (No tags)│
└────────┬────────┴────────┬────────┴────────┬────────┴────────────┬─────────────┘
         │                 │                 │                     │
         └─────────────────┴────────┬────────┴─────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│ 5. UNIVERSAL ENGINE ASSEMBLY (`engine/assemble_movie.py`)                      │
│ - Strict Rule: Zero Premature Assembly (100% of clips verified before run)    │
│ - Beat-matched scene transitions to narration shifts                           │
│ - Auto 1080p center-crop & framerate normalization                             │
│ - Full HD progressive master export into `final_output/`                       │
└───────────────────────────────────┬────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────────┐
│ 6. UNIVERSAL SEO & YOUTUBE PACK (`engine/generate_youtube_kit.py`)             │
│ - 5 Standardized files in `youtube_writeups/`                                  │
│ - Titles, Description with exact chapter timestamps, Tags & Endscreen guide    │
└────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Phase-by-Phase Standard Operating Procedures (SOP)

### Phase 1: Scripting & Storyboards (ChatGPT Portal)
- **URL:** `https://chatgpt.com/`
- **Authentication:** User logs in once.
- **Story Structure:** 1 Narrator, 3 Minutes target length, 1 Background Visual per Scene.
- **Master Script Prompt:**
  ```text
  i am going to create a cartoon story video in hindi which only have 1 narrator so create a script for my 3 min story video. write scripts in scene because i am going to use 1 photo for each scene. no i mean first give me a prompt to generate the scene photo and just after that give the scene script
  ```
- **Voiceover Tone Variation Prompt:**
  ```text
  {GIVE ME ONLY SCRIPT FOR ELEVEN LABS WITH TONE VARIATIONS}
  ```
  *(Generates `[Calm, Warm Tone]`, `[Surprised, Fast Tone]`, `[Confused Tone]`, `[Confident, Heroic Tone]`).*

---

### Phase 2: Visual Generation (Google Gemini Portal)
- **URL:** `https://gemini.google.com/`
- **Authentication:** User logs in via Google Account.
- **Generation Command Prefix:**
  ```text
  CREATE A 16:9 IMAGE - "<IMAGE PROMPT FROM CHAPTER 1>"
  ```
- **Standard:** Every scene visual must strictly be generated in **16:9 widescreen format** and downloaded as `scene_01.png`, `scene_02.png`, etc.

---

### Phase 3: Motion & Animation (Meta AI Portal)
- **URL:** `https://www.meta.ai/`
- **Authentication:** User logs in via Meta / Facebook / Instagram.
- **Action:**
  1. Click `+` and attach the 16:9 scene image from Gemini.
  2. Input / trigger command:
     ```text
     Create a video from my photo
     ```
  3. Meta AI synthesizes animated cartoon physics (eye blinks, hand gestures, flowing clothes, trees swaying, water ripples).
  4. Download animated MP4 clip as `clip_01.mp4`, `clip_02.mp4`, etc.

---

### Phase 4: Expressive Voiceover (ElevenLabs Portal)
- **URL:** `https://elevenlabs.io/app/speech-synthesis/text-to-speech`
- **Authentication:** User logs in.
- **Settings:**
  - **Voice:** "Harsh - Resonant, Serious and Dramatic" (or chosen Hindi narrator).
  - **Model:** **`Eleven v3 (alpha)`** *(MANDATORY: Model v3 dynamically reads and acts out bracketed tone cues without speaking them)*.
  - **Input:** Paste the tone-tagged script from Phase 1.
  - **Download:** Save the master narration audio (`voiceover.mp3`).

---

### Phase 5: Timeline Assembly & Narration Synchronization
- **Engine:** Direct local automated timeline engine (FFmpeg / VN specification).
- **Assembly Rules:**
  1. Voiceover is placed on the master audio track.
  2. Scene clips cut precisely when the narrator shifts focus or character.
  3. Short motion clips are smoothed and time-stretched (0.3x–0.5x speed) so the visual seamlessly fills the full duration of its narration beat.
  4. Channel Logo watermark is overlaid in the **bottom-right corner** from `00:00` to the final frame.
  5. Rendered to **1080p FHD MP4** (`final_video.mp4`).

---

### Phase 6: Thumbnail, SEO & YouTube Studio Upload
- **Thumbnail Prompt (ChatGPT -> Gemini):**
  ```text
  CREATE A THUMBNAIL PROMPT FOR GEMINI WHICH ALSO HAVE A TEXT AND IN DETAILED THUMBNAILS
  ```
- **File Size Safety:** Compressed under 2MB (via TinyPNG / Canva).
- **SEO Package (ChatGPT):**
  ```text
  Give me high-CTR YouTube title, description with tags for YouTube
  ```
- **YouTube Studio Upload (`studio.youtube.com`):**
  - Drop MP4 video.
  - Apply High-CTR Title, formatted Description, and Tag bundle.
  - Verify Automated Copyright Check: **Restrictions: None (0 copyright strikes)**.
  - Set to **Public**.

---

## 🚦 Interactive Browser Handshake Protocol

When executing each project:
1. I will launch / navigate the browser to the required platform.
2. If authentication is needed, I will ask you:  
   *"Please log into [Platform Name] in the open browser window. Let me know when you're in."*
3. The moment you say "Logged in" (or "Done"), I will immediately resume autonomous control: entering prompts, processing visual and audio generations, and retrieving assets.

