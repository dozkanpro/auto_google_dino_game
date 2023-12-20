from selenium import webdriver
import pyautogui as gui
from PIL import Image
import time
import keyboard

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

keep = True


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


# Inject JavaScript to create a div element to display the message
driver.execute_script("""
    var messageDiv = document.createElement('div');
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '10px';
    messageDiv.style.left = '80px';
    messageDiv.style.backgroundColor = 'white';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '9999';
    document.body.appendChild(messageDiv);
    window.messageDiv = messageDiv
""")

while keep:
    # Update the message in the div element using JavaScript
    driver.execute_script("""
                window.messageDiv.innerText = "Press Enter key to Exit the game.";
            """)
    if keyboard.is_pressed('enter'):
        keep = False

    driver.save_screenshot('output.png')
    img = Image.open('output.png')
    is_collision(img)




driver.quit()
