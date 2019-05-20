from pynput import keyboard
from threading import Thread
import time

class ArduinoRead:

    def __init__(self):
        self.status = ''
    
    def on_press(key):
        try:
            status = key.char
            print(status)
        except AttributeError:
            print('special key {0} paressed'.format(
                key))

    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def read_status(self):
        return self.status

    # Collect events until release
    def start_status():
        print("iniciado thread")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def _run(self):
        print("Chamando Função")
        Thread(target=self.start_status, args=()).start()
        return self
