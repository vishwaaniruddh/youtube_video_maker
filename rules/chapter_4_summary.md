# Chapter 4 Summary: Expressive Voiceover Generation with ElevenLabs

**Source File:** `rules/chapter 4.mp4`  
**Duration:** 2 minutes 47 seconds  
**Creator / Course:** HuslersWay (Cartoon Video Bundle System)  
**Tools Used:** ChatGPT, ElevenLabs (`elevenlabs.io`)

---

## 1. Executive Summary

Chapter 4 demonstrates how to turn plain Hindi story scripts into high-engagement, **emotionally varied voiceover narration** using **ElevenLabs** and prompt engineering with tone cue tags.

---

## 2. Step-by-Step Workflow

1. **Reformat Script for Voiceover in ChatGPT:**
   - Return to the ChatGPT chat containing your scene script.
   - Send the specialized prompt:
     ```text
     {GIVE ME ONLY SCRIPT FOR ELEVEN LABS WITH TONE VARIATIONS}
     ```

2. **The Output: Emotion & Tone Direction Tags:**
   ChatGPT outputs the script formatted with bracketed voice-acting cues:
   - `[Calm, Warm Tone]` (Used for village exposition and morning setting)
   - `[Surprised, Fast Tone]` (Used when the missing cap or stolen sweets are discovered)
   - `[Confused Tone]` (Used for puzzled villagers)
   - `[Confident, Heroic Tone]` (Used when the protagonist Golu steps forward as detective)
   - `[Curious Investigative Tone]` (Used when inspecting footprints and clues)

3. **Configure ElevenLabs:**
   - Navigate to `https://elevenlabs.io` and open **Text to Speech**.
   - **Voice Selection:** Choose a deep, resonant Hindi/Indian narrator (e.g., *"Harsh - Resonant, Serious and Dramatic"*).
   - **Model Selection:** Select **`Eleven v3 (alpha)`**.
     > **Why `Eleven v3` is critical:** The v3 model is designed to read bracketed instructions like `[Surprised, Fast Tone]` and alter its pitch, speed, and emotional inflection dynamically without speaking the bracketed words.

4. **Paste and Generate:**
   - Paste the full tone-tagged script into the text editor.
   - Adjust the **Stability** slider towards expressive/creative.
   - Click **Generate Speech**.

5. **Review & Download:**
   - Listen to the preview.
   - ElevenLabs generates variations (e.g., Generation 1, Generation 2).
   - Click the download icon to save the master voiceover audio file (`.mp3`).

---

## 3. Bridge to Chapter 5
With both the animated video clips (from Meta AI) and the master voiceover track (from ElevenLabs) ready, **Chapter 5** shows how to import everything into the video editing suite (CapCut) to assemble, synchronize, add speech bubbles, and produce the final cartoon video.

