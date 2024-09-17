import keyboard
import time
import pyautogui

keyboard_hook = False
z_pressed = False

def start_keyboard(input_text):
    try: 
        if(input_text == "start"):
            print(f"Starting keyboard hook")
        elif(input_text == "stop"):
            print(f"Stopping keyboard hook")
    except Exception as e:
        print(f"Word not found, type either start or stop (case-sensitive)")

def find_image(image_path):
    try:
        # Locate the image on the screen
        image_location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=0.8, region=(700,480,40,40))
        return image_location
    except Exception as e:
        print(f"Error finding image: {e}")
        return None
    
def click_key(key):
    try:
        # Click the specified key
        keyboard.press_and_release(key)
        print(f"Key '{key}' pressed.")
        time.sleep(0.2)
    except Exception as e:
        print(f"Error pressing key: {e}")    

def main_loop():
    global z_pressed
    if z_pressed == False:
        keyboard.press("z")
        z_pressed = True
    keyboard.press_and_release('1')
    keyboard.press_and_release('2')
    keyboard.press_and_release('3')
    keyboard.press_and_release('4')
    keyboard.press_and_release('5')
    keyboard.press_and_release('6')
    keyboard.press_and_release('7')
    keyboard.press_and_release('8')
    keyboard.press_and_release('9')
    keyboard.press_and_release('0')
    keyboard.press_and_release('tab')
    time.sleep(1)
# Set the flag to control the loop
main_loop_active = False

def secondary_loop():
    #keyboard.press_and_release('c')
    time.sleep(0.3)
    keyboard.press_and_release('space')
#Set the flag to control the loop
secondary_loop_active = False

def start_stop_loop(e):
    global main_loop_active
    global secondary_loop_active
    global z_pressed
    # global zx_loop_active

    if e.event_type == keyboard.KEY_DOWN and e.name == 'z':
        z_pressed = not z_pressed # Toggle the z_pressed loop flag
    if e.event_type == keyboard.KEY_DOWN and e.name == ',':
        main_loop_active = not main_loop_active  # Toggle the main loop flag
    if e.event_type == keyboard.KEY_DOWN and e.name == '.':
        secondary_loop_active = not secondary_loop_active  # Toggle the main loop flag
    # if e.event_type == keyboard.KEY_DOWN and e.name == '-': 
    #   zx_loop_active = not zx_loop_active
        
# Register the callback for the key press

try:
    while(keyboard_hook):
        keyboard.hook(start_stop_loop)
        while True:
            if main_loop_active:
                main_loop()
            if secondary_loop_active:
                secondary_loop()
            # if zx_loop_active:
            #     zx_loop()
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    keyboard.unhook_all()