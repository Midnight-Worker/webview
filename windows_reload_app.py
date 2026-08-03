import webview
import keyboard

window = webview.create_window("My Webview", url="index.html", fullscreen=True)

keyboard.add_hotkey('enter', lambda: window.evaluate_js("location.reload()"))

webview.start()

