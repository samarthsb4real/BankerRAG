import pandas as pd
import time
from pynput import keyboard, mouse

# Store user behavior
keystroke_data = []
mouse_data = []

# Track last key press time
last_key_time = None

def on_press(key):
    global last_key_time, keyboard_listener, mouse_listener
    # Check for ESC key to stop listeners
    if key == keyboard.Key.esc:
        keyboard_listener.stop()
        mouse_listener.stop()
        return False

    try:
        current_time = time.time()
        if last_key_time:
            time_diff = current_time - last_key_time
        else:
            time_diff = 0

        keystroke_data.append({"key": key.char, "time_diff": time_diff})
        last_key_time = current_time
    except AttributeError:
        pass  # Ignore special keys

def on_click(x, y, button, pressed):
    if pressed:
        mouse_data.append({"x": x, "y": y, "timestamp": time.time()})

# Start listeners
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

print("Collecting behavior data... Press ESC to stop.")

keyboard_listener.join()
mouse_listener.join()

# Save to CSV
df_keys = pd.DataFrame(keystroke_data)
df_keys.to_csv("keystroke_data.csv", index=False)

df_mouse = pd.DataFrame(mouse_data)
df_mouse.to_csv("mouse_data.csv", index=False)

print("Data collection completed. Check 'keystroke_data.csv' and 'mouse_data.csv'.")