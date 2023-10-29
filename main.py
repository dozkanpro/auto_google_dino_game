import pyautogui
from selenium import webdriver
import pyautogui as gui
from PIL import Image
import time


URL = "https://elgoog.im/dinosaur-game/"

# Keep Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# open game on the Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(3)

# start the game
gui.press('up')

time.sleep(3)


def is_collision(img):
    # Define region for cactii and birds
    rect_for_cactii = (86, 673, 137, 713)
    rect_for_birds = (264, 608, 329, 677)

    # Crop the image to the cactus and bird regions
    cactii_cropped = img.crop(rect_for_cactii)
    birds_cropped = img.crop(rect_for_birds)

    # Convert the cropped images to grayscale
    cactii_cropped = cactii_cropped.convert('L')
    birds_cropped = birds_cropped.convert('L')

    threshold = 83  # Adjust to define black

    # Check if any pixel in the cropped images is below the thresholds
    for pixel in cactii_cropped.getdata():
        if pixel < threshold:
            gui.press('up')
    for pixel in birds_cropped.getdata():
        if pixel < threshold:
            gui.press('down')


while True:
    driver.save_screenshot('output.png')
    img = Image.open('output.png')
    is_collision(img)

