import webview
from pynput import keyboard


window = webview.create_window(
    "My Webview",
    url="index.html",
    fullscreen=True,
)


def on_press(key):
    if key == keyboard.Key.enter:
        print("Enter erkannt – Reload", flush=True)
        window.evaluate_js("location.reload()")


listener = keyboard.Listener(on_press=on_press)
listener.daemon = True
listener.start()

webview.start()
