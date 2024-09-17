import keyboard
import time
import pyautogui
import threading

keyboard_hook = True  # This flag starts the main loop
z_pressed = False

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
    if not z_pressed:  # Press 'z' if it's not already pressed
        keyboard.press("z")
        z_pressed = True
    for key in '1234567890':
        keyboard.press_and_release(key)
    keyboard.press_and_release('tab')
    time.sleep(1)

def secondary_loop():
    # Simulate space press
    time.sleep(0.3)
    keyboard.press_and_release('space')

# Flags to control the loops
main_loop_active = False
secondary_loop_active = False
hooked = True  # Flag to check if the keyboard is hooked

def start_stop_loop(e):
    global main_loop_active, secondary_loop_active, z_pressed

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'z':
            z_pressed = not z_pressed  # Toggle the z_pressed loop flag
            print(f"z_pressed: {z_pressed}")
        elif e.name == ',':
            main_loop_active = not main_loop_active  # Toggle the main loop flag
            print(f"main_loop_active: {main_loop_active}")
        elif e.name == '.':
            secondary_loop_active = not secondary_loop_active  # Toggle the secondary loop flag
            print(f"secondary_loop_active: {secondary_loop_active}")

def rehook_keyboard():
    global hooked
    if not hooked:
        keyboard.hook(start_stop_loop)
        hooked = True
        print("Keyboard rehooked. Listening for key events again.")

def unhook_keyboard():
    global hooked
    if hooked:
        keyboard.unhook_all()
        hooked = False
        print("Keyboard unhooked to prevent typing delay.")

# Hook the keyboard once
keyboard.hook(start_stop_loop)

def loop_manager():
    # This function runs continuously to manage the loops
    while keyboard_hook:
        if main_loop_active:
            main_loop()
        if secondary_loop_active:
            secondary_loop()
        time.sleep(1)

# Run the loop_manager in a separate thread
loop_thread = threading.Thread(target=loop_manager)
loop_thread.start()

try:
    while keyboard_hook:
        # Console input for manual rehook/unhook
        user_input = input("Type 'rehook' to enable or 'unhook' to disable the keyboard listener: ")
        if user_input == "rehook":
            rehook_keyboard()
        elif user_input == "unhook":
            unhook_keyboard()

except KeyboardInterrupt:
    pass
finally:
    # Cleanup: Unhook all listeners (in case something is still hooked)
    if hooked:
        keyboard.unhook_all()
    keyboard_hook = False
    loop_thread.join()  # Wait for the loop thread to finish
