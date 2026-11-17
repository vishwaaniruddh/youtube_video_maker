# Antigravity Workspace Configuration & Production Directives

Welcome to the YouTube 3D Cartoon & Animation Production Repository (`F:\YouTube`).

## 🚨 MANDATORY REPOSITORY LAWS & PRODUCTION PIPELINE

All AI video generation tasks in this repository MUST strictly follow the codified production rules defined in `rules/MASTER_PIPELINE_RULES.md`.

### Core Directives:
1. **Engine Separation:**
   - Universal tools live exclusively in `F:\YouTube\engine/` (`init_project.py`, `assemble_movie.py`, `generate_youtube_kit.py`).
   - Never write loose scripts inside individual project folders.
   - Assemble movies using `python engine/assemble_movie.py --project-dir <project_name>`.
2. **Rule #0: Character Consistency Lock:**
   - For any recurring character, lock an approved Master Reference image (`sample_images/shot_master_character.png`) and strictly use Image-to-Video (I2V) in Google Veo / Gemini / Meta AI.
3. **Rule #1: Zero Premature Assembly:**
   - Never stitch, compile, or assemble a movie until 100% of the planned video clips exist and are verified in `<project_name>/generated_clips/`.
4. **Rule #2: 100% Real Video Motion (Zero Slideshows/Fake Pans):**
   - Every single shot must be a genuine AI motion video clip generated in Google Gemini / Veo or Meta AI.
   - Absolutely zero still image pan/zoom ("Ken Burns effect") simulations. Living physics must be visible.
5. **Rule #3: Clean Audio Narration via ElevenLabs:**
   - Master voiceover must be produced via ElevenLabs (`Eleven v3 alpha` or Indian Hindi voice).
   - Strip all bracketed emotion tags from speech scripts unless using v3 alpha tag parsing. Master file: `audio/master_voiceover.mp3`.
6. **Rule #4: Standardized YouTube Upload Kit:**
   - Every completed project must generate the 5 standard writeups in `<project_name>/youtube_writeups/` using `python engine/generate_youtube_kit.py --project-dir <project_name>`.

### When the User Provides a New Video Topic:
1. Initialize the project: `python engine/init_project.py --name <slug> --title <title>`
2. Create `01_script_and_storyboard.md` with scene breakdown & prompts.
3. Lock Master Character Image in `sample_images/shot_master_character.png` & generate scene stills.
4. Produce master voiceover in `audio/master_voiceover.mp3` via ElevenLabs.
5. Generate 100% genuine AI motion clips in `generated_clips/` via Google Gemini / Veo / Meta AI.
6. Run assembly (`python engine/assemble_movie.py --project-dir <slug>`) and YouTube kit (`python engine/generate_youtube_kit.py --project-dir <slug>`).

