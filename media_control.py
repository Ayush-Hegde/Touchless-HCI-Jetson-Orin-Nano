from pynput.keyboard import Controller, Key

keyboard = Controller()

def play_pause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def volume_up():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.release(Key.ctrl)

def volume_down():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.release(Key.ctrl)

def next_track():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.release(Key.ctrl)

def stop():
    keyboard.press('s')
    keyboard.release('s')
