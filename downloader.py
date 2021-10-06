import pyautogui as agui
import time


next_photo_coordinate = (1500, 500)
current_photo_coordinate = (1000, 500)
photo_prefix = "2021-09-03"
n_photos = 159

for count in range(109, n_photos):
    agui.click(next_photo_coordinate)
    time.sleep(1)
    agui.rightClick(current_photo_coordinate)
    time.sleep(0.5)
    agui.click(current_photo_coordinate + (30, 60))
    time.sleep(3)
    agui.write(photo_prefix + "-" + str(count))
    time.sleep(0.5)
    agui.press("enter")
    time.sleep(0.5)
