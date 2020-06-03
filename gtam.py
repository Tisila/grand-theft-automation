#Grand Theft AutoMation
from pynput import keyboard
from time import sleep
import threading
from directkeys import PressKey, ReleaseKey, W, A, S, D
# Tutorials used in the making of this
# To change, read here https://pypi.org/project/pynput/
#https://python-forum.io/Thread-Keypress-when-running-a-python-app-in-a-console-on-windows
#https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
#https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
#https://docs.python.org/3/library/threading.html#timer-objects

class CaptureKeys:
    def __init__(self):
        self._combinations = {keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.page_up}
        self._current = set()
        self._user = keyboard.Controller()
        self._timer = 2.0 #change here, time in seconds
        self._task = threading.Timer(self._timer, self.execute)
        self._btn_hold = 0.76 #change here, time in seconds

    def execute(self):
        """ My function to execute when a combination is pressed """
        #print("it worked!")
        #self._user.press('t')
        PressKey(S)
        sleep(self._btn_hold)
        ReleaseKey(S)
        #self._user.release('t')

        #Defining new timer because the first one has already been used
        self._task = threading.Timer(self._timer, self.execute)
        #self._btn_hold=float(input("\nFor how long should I hold the key next time?(seconds)> "))
        #print("Saved hold key for {} seconds\nWaiting for command...".format(self._btn_hold))

 
    def get_hold_time(self):
        return self._btn_hold

    def on_press(self, key):
        #print('{0} was pressed'.format(key))
        if key in self._combinations:
            self._current.add(key)
        if self._combinations == self._current:
            #Combination was pressed
            print("Combination was pressed, deploy in {} seconds".format(self._timer))
            self._task.start()
 
    def on_release(self, key):
        #print('{0} was released'.format(key))
        if key in self._combinations:
            self._current.remove(key)
        #if key == keyboard.Key.esc:
            #ReleaseKey(S)
            ## Stop listener
            return False
 
    # Collect events until released
    def main(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
 
    def start_listener(self):
        keyboard.Listener.start
        self.main()

if __name__ == '__main__':
    print(" ____________________________________________ ")
    print("|                                            |")
    print("|        Welcome to wheel of fortune!        |")
    print("|____________________________________________|")
    print("         Here, we make our own luck\n")
    ck = CaptureKeys()
    print("Hold key set for {} seconds".format(ck.get_hold_time()))
    print("Waiting for command...")
    ck.start_listener()
