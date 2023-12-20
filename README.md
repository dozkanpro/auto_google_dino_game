# Chrome Dinosaur Game Automator 
  This Python script automates playing the Chrome Dinosaur Game using image recognition and keyboard simulation.

 ## Technology Used:
 - Selenium library
 - pyautogui library
 - PIL (Python Imaging Library)
 - Chrome WebDriver

## Getting Started
 - **Fork the repository:** You should **fork the repository** and then **clone it** so you can manage your own repo and use this only as a template.
    ```
    $ git clone https://github.com/your_username/your-flask-project.git
    ```
 - **Install dependencies:**
  
    ```
    pip install -r requirements.txt
 - **Download and install Chrome WebDriver**: [Chrome WebDriver](https://chromedriver.chromium.org/downloads)

 - **Run the Application:**
  
      ```
       python main.py
      ```
-  The script will open the Chrome Dinosaur Game in a new Chrome window/tab and automatically play the game.
-  To exit the game, press the Enter key.

## How It Works
- The script uses image recognition techniques via the Pillow library to analyze screenshots of the game window.
- It scans specific regions of the screen for obstacles (cacti and birds) and simulates key presses (up and down) using pyautogui to make the dinosaur jump or duck accordingly.

## Customization
- Adjust the threshold value in the script to fine-tune obstacle detection based on your screen's contrast and brightness.
- Modify the region coordinates (rect_for_cactii and rect_for_birds) to fit your screen size or game window position if needed.
