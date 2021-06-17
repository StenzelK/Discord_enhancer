import win32gui
import time
from pynput import mouse, keyboard

flag = 0

'''
For some reason Discord removed the option of sending messeges via GUI, requiring users to press a key on a keyboard
This function listens for a doubleclick of a left mouse button and simulates the user pressing Enter
Works only if Discord window is selected

'''
def on_click(x, y, button, pressed):
    keyboardCon = keyboard.Controller()

    global flag
    if button == mouse.Button.left and not pressed:

        flag += 1

    elif not pressed:

        flag = 0

    if flag == 2:

        keyboardCon.press(keyboard.Key.enter)
        keyboardCon.release(keyboard.Key.enter)
        flag = 0


    if not pressed:
        # Stop listener
        return False
'''
Listens for specific voice commands and translates them into instructions for a Discord bot
Speech-to-text conversion proved unreliable and I abandoned the idea

'''
def main():

    w = win32gui
    while True:
        time.sleep(0.01)
        if("{}".format(w.GetWindowText(w.GetForegroundWindow())).endswith('Discord')):
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()

            with sr.Microphone() as source:

                audio = r.listen(source)
                try:
                    if r.recognize_google(audio) == 'Alexa':

                        keyboard.press('!')
                        keyboard.release('!')
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        for i in command:
                            keyboard.press(i)
                            keyboard.release(i)

                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)
                        time.sleep(.7)
                        if 'play' in command:
                            choice = '!play 1'

                            for i in choice:
                                keyboard.press(i)
                                keyboard.release(i)

                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)


                except:
                    pass

if __name__ == "__main__":
    main()

