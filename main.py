import pyautogui
import numpy as np
import cv2
#position of space in front of the dinosaur and image resolution
#for a screen with a resolution of 1920 by 1080
x, y, w, h = 670, 290, 160, 80

#speed
x1 = 0.05

while True:
    image = pyautogui.screenshot(region=(x, y, w, h))
    image1 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    black_pixel_count = np.sum(image1 < 100)
    white_pixel_count = np.sum(image1 > 100)
    if 1200 < white_pixel_count < 30000:
        x += x1
        pyautogui.press('up')
    if 500 < black_pixel_count < 30000 < white_pixel_count:
        x += x1
        pyautogui.press('up')
    if x > 890:
        x = 890

