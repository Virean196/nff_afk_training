import pyautogui
import time

def find_image(image_path):
    try:
        # Locate the image on the screen
        image_location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.8)
        return image_location
    except Exception as e:
        print(f"Error finding image: {e}")
        return None

def click_key(key):
    try:
        # Click the specified key
        pyautogui.press(key)
        print(f"Key '{key}' pressed.")
        # Add a short delay after pressing the key
        time.sleep(0.5)
    except Exception as e:
        print(f"Error pressing key: {e}")

def main():
    # Specify the image file paths using raw strings
    x_path = r"Images\xsmall.png"
    z_path = r"Images\zsmall.png"

    # Specify the keys to press when the respective images are found
    x_key = "x"  
    z_key = "z"  

    try:
        while True:
            # Check if the first image is found on the screen
            x_location = find_image(x_path)

            if x_location:
                # Click the key associated with the first image
                click_key(x_key)

            # Check if the second image is found on the screen
            z_location = find_image(z_path)

            if z_location:
                # Click the key associated with the second image
                click_key(z_key)

            # Pause for a moment before checking again
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()