import pyautogui
from PIL import Image
import numpy as np
import os
import time
import winsound

# Set the region of interest (ROI) coordinates
x1, y1, x2, y2 = 0, 0, 1920, 1080  # capture the entire screen

# Set the directory path where screenshots will be saved
screenshot_dir = "D:\\screenshots"

# Create the directory if it doesn't exist
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

def take_screenshot():
    # Play a short, quiet sound when the script starts
    winsound.Beep(2500, 100)  # 2500 Hz frequency, 100 ms duration

    # Take an initial screenshot of the ROI
    initial_screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    # Convert the screenshot to a numpy array
    initial_array = np.array(initial_screenshot)

    screenshot_count = 1205

    while True:
        # Take a new screenshot of the ROI
        new_screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

        # Convert the new screenshot to a numpy array
        new_array = np.array(new_screenshot)

        # Check if the new screenshot is different from the initial screenshot
        if not np.array_equal(initial_array, new_array):
            # Take a screenshot of the entire screen
            full_screenshot = pyautogui.screenshot()
            filename = f"screenshot_{screenshot_count}.png"
            full_screenshot.save(os.path.join(screenshot_dir, filename))
            print(f"Screenshot saved as {os.path.join(screenshot_dir, filename)}")
            screenshot_count += 1

        # Update the initial screenshot
        initial_array = new_array

        # Add a small delay to avoid taking screenshots too quickly
        time.sleep(0.5)

take_screenshot()