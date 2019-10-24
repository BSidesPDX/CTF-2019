# This is by far the worst code I have ever written in my entire life
# Please don't hold this against me
import subprocess
import gpiozero
import math
import os, time
import threading

pin_rotaryenable = 17
pin_countrotary = 22
pin_hook = 27

bouncetime_enable = 0.01
bouncetime_rotary = 0.01
bouncetime_hook = 0.01


rotaryenable = gpiozero.DigitalInputDevice(pin_rotaryenable, pull_up=True, bounce_time=bouncetime_enable)
countrotary = gpiozero.DigitalInputDevice(pin_countrotary, pull_up=True, bounce_time=bouncetime_rotary)
hook = gpiozero.DigitalInputDevice(pin_hook, pull_up=True, bounce_time=bouncetime_hook)


class Dial():
        def __init__(self, expectedDigits = -1, callback = None):
                self.pulses = 0
                self.number = ""
                self.counting = True
                self.calling = False
                self.timer = threading.Timer(0.2, self.fixRotaryDisable)
                self.switch_hook_timer = threading.Timer(0.7, self.switchHookEnd)
                self.switch_hook_dial = threading.Timer(0.3, self.switchHookDial)
                self.expected_digits = expectedDigits
                self.initial_pickup = None
                self.callback = callback

                self.setup()

        def startcalling(self):
            if self.switch_hook_timer.is_alive():
                self.switch_hook_timer.cancel()
                self.pulses += 2
                if self.switch_hook_dial.is_alive():
                    self.switch_hook_dial.cancel()
                self.switch_hook_dial = threading.Timer(0.6, self.switchHookDial)
                self.switch_hook_dial.start()

            self.calling = True
            if self.initial_pickup == None:
                self.initial_pickup = True

        def switchHookDial(self):
            self.stopcounting()

        def switchHookEnd(self):
            self.calling = False
            self.reset()
            self.initial_pickup = True

        def stopcalling(self):
            if self.switch_hook_timer.is_alive():
                self.switch_hook_timer.cancel()
            self.switch_hook_timer = threading.Timer(0.7, self.switchHookEnd)
            self.switch_hook_timer.start()

            if self.initial_pickup == True:
                self.initial_pickup = False
            self.is_receiver_down = True

        def firstPickup(self):
            if self.pulses == 0 and self.number == "" and self.initial_pickup == True and self.calling == True:
                return True
            return False

        def startcounting(self):
            self.counting = self.calling

        def stopcounting(self):
            self.counting = False
            if self.calling:
                if self.pulses > 0:
                    if math.floor(self.pulses / 2) == 10:
                        self.number += "0"
                    else:
                        self.number += str(int(math.floor(self.pulses / 2)))
                    self.pulses = 0

        def addpulse(self):
                if self.counting:
                    if self.timer.is_alive():
                        self.timer.cancel()
                    self.pulses += 1
                    self.timer = threading.Timer(0.2, self.fixRotaryDisable)
                    self.timer.start()


        def getnumber(self):
                return self.number

        def done(self):
            if self.expected_digits >= 0 and len(self.number) >= self.expected_digits:
                return True

            return False


        def reset(self):
                self.pulses = 0
                self.number = ""
                if self.callback is not None:
                    self.callback()

        def fixRotaryDisable(self):
            if self.counting == True:
                self.stopcounting()


        def setup(self):
            countrotary.when_deactivated = self.addpulse
            countrotary.when_activated = self.addpulse
            rotaryenable.when_activated = self.startcounting
            rotaryenable.when_deactivated = self.stopcounting

            #backwards intentionally due to how switch works
            hook.when_deactivated = self.stopcalling
            hook.when_activated = self.startcalling

            if(hook.value == 1):
                self.startcalling()

if __name__ == "__main__":
        
        dial = Dial()
        dial.setup()
        while True:
            time.sleep(1)
