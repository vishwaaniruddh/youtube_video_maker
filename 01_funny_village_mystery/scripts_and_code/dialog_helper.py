import time
import pyautogui

time.sleep(2.5)
video_path = r"F:\YouTube\funny_village_mystery\100_percent_real_motion_cartoon_movie.mp4"
pyautogui.write(video_path, interval=0.01)
time.sleep(0.5)
pyautogui.press('enter')
print("SUBMITTED_FILE_DIALOG")

