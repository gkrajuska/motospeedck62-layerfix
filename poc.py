
import keyboard
import sys
from time import sleep

def debug():

    def printInfo(event):
        print(event.to_json())

    keyboard.hook(printInfo)

    keyboard.wait('ctrl+alt+q')
    print('Ending debug mode')
    sys.exit()

def start(debugFlag=False) -> None:
    def endRoutine():
        keyboard.unhook_all()
        print('Unhooking all...')
        sys.exit()

    if debugFlag == True:
        debug()

    # Remapping block
    keyboard.remap_hotkey('alt+a', 'left arrow')
    keyboard.remap_hotkey('alt+s', 'down arrow')
    keyboard.remap_hotkey('alt+w', 'up arrow')
    keyboard.remap_hotkey('alt+d', 'right arrow')
    keyboard.remap_hotkey('right ctrl+1', 'F1')
    keyboard.remap_hotkey('right ctrl+2', 'F2')
    keyboard.remap_hotkey('right ctrl+3', 'F3')
    keyboard.remap_hotkey('right ctrl+4', 'F4')
    keyboard.remap_hotkey('right ctrl+5', 'F5')
    keyboard.remap_hotkey('right ctrl+6', 'F6')
    keyboard.remap_hotkey('right ctrl+7', 'F7')
    keyboard.remap_hotkey('right ctrl+8', 'F8')
    keyboard.remap_hotkey('right ctrl+9', 'F9')
    keyboard.remap_hotkey('right ctrl+0', 'F10')
    keyboard.remap_hotkey('right ctrl+-', 'F11')
    keyboard.remap_hotkey('right ctrl+=', 'F12')
    keyboard.remap_hotkey

    keyboard.wait('left ctrl+left alt+q', suppress=True)
    endRoutine()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            start(True)
    else:
        start()