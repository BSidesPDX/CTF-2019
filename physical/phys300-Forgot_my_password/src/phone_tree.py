# This is by far the worst code I have ever written in my entire life
# Please don't hold this against me

import subprocess
import time
import signal
import sys
import threading
import Queue
import select
from dial import *

dial_results = Queue.Queue()

stop_threads = False

class Person:
    def __init__(self, eid, access_card, audio_file):
        self.eid = eid
        self.access_card = access_card
        self.audio_file = audio_file

authorized_users = [Person("12345", "0014360458", "timzen.wav"), Person("70463", "0014353332", "carl.wav"), Person("01507", "0014358641", "strange.wav"), Person("86753", "0014340151", "harding.wav"), Person("31337", "0014359089", "gallagher.wav")]

class PhoneTree:
    def __init__(self, audio_file = "", tree_options = None):
        self.audio_file = audio_file
        self.tree_options = tree_options

    def play(self, file=None, wait=False):
        if file is None:
            file = self.audio_file

        self.player = subprocess.Popen(["aplay", file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if wait:
            self.player.wait()

        return

    def reset(self):
        try:
            self.player.kill()
        except:
            pass

class ResetPasswordTree:
    def __init__(self, callback):
        self.tree = PhoneTree()
        self.dial = Dial(5, callback=callback)
        self.eid = None
        self.player = None
    
    def start(self): 
        global stop_threads
        
        self.player = subprocess.Popen(["aplay", "password_reset_1.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        while not stop_threads and self.dial.done() != True:
            time.sleep(0.5)

        try:
            self.player.kill()
        except:
            pass

        if stop_threads:
            dial_results.put(None)
            sys.exit(0)

        person = None
        for p in authorized_users:
            if p.eid == self.dial.getnumber():
                person = p
                break

        if person is not None:
            self.eid = self.dial.getnumber()
            self.player = subprocess.Popen(["aplay", person.audio_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while self.player.poll() is None and not stop_threads:
                time.sleep(0.5)
        else:
            self.player = subprocess.Popen(["aplay", "bad_eid.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            while not stop_threads:
                time.sleep(0.5)


        
        if stop_threads:
            try:
                self.player.kill()
            except:
                pass

            dial_results.put(None)
            sys.exit(0)

        self.readBadge()

        self.player = subprocess.Popen(["mpg123", "-q", "modem.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while self.player.poll() is None and not stop_threads:
            time.sleep(0.5)

        if stop_threads:
            try:
                self.player.kill()
            except:
                pass

            dial_results.put(None)
            sys.exit(0)
        
        self.checkBadge()

    def checkBadge(self):
        for p in authorized_users:
            if p.eid == self.eid and p.access_card == self.badge:
                self.player = subprocess.Popen(["aplay", "good_scan_badge.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                while self.player.poll() is None and not stop_threads:
                    time.sleep(0.5)
                
                if stop_threads:
                    try:
                        self.player.kill()
                    except:
                        pass

                    dial_results.put(None)
                    sys.exit(0)

                while True:
                    self.player = subprocess.Popen(["aplay", "flag.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    while self.player.poll() is None and not stop_threads:
                        time.sleep(0.5)
                
                    if stop_threads:
                        try:
                            self.player.kill()
                        except:
                            pass

                        dial_results.put(None)
                        sys.exit(0)

                    time.sleep(3)

        self.player = subprocess.Popen(["aplay", "bad_scan_badge.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while not stop_threads:
            time.sleep(0.5)

        try:
            self.player.kill()
        except:
            pass
        
        dial_results.put(None)
        sys.exit(0)
    
    def readBadge(self):
        global stop_threads

        self.tree.play("scan_badge.wav", True)

        hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

        hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

        fp = open('/dev/hidraw0', 'rb', os.O_RDONLY|os.O_NONBLOCK)
        ss = ""
        shift = False
        done = False

        while not done:
            if stop_threads:
                dial_results.put(None)
                sys.exit(0)

            r, _, _ = select.select([fp],[],[],0)
            if not r:
                time.sleep(0.5)
                continue

            try:
                self.player.kill()
            except:
                pass

            ## Get the character from the HID
            buffer = fp.read(8)

            for c in buffer:
                if ord(c) > 0:
                    ##  40 is carriage return which signifies
                    ##  we are done looking for characters
                    if int(ord(c)) == 40:
                        done = True
                        break;

                    ##  If we are shifted then we have to 
                    ##  use the hid2 characters.
                    if shift: 
                        ## If it is a '2' then it is the shift key
                        if int(ord(c)) == 2 :
                            shift = True

                        ## if not a 2 then lookup the mapping
                        else:
                            ss += hid2[ int(ord(c)) ]
                            shift = False
                    ##  If we are not shifted then use
                    ##  the hid characters

                    else:
                        ## If it is a '2' then it is the shift key
                        if int(ord(c)) == 2 :
                            shift = True

                        ## if not a 2 then lookup the mapping
                        else:
                            ss += hid[ int(ord(c)) ]
                        
        fp.close()
        
        self.badge = ss

        return

    def kill(self):
        try:
            self.player.kill()
        except:
            pass

class NewTicket:
    def __init__(self, callback):
        self.player = None
        self.dial = Dial(callback=callback)

    def start(self):
        self.player = subprocess.Popen(["aplay", "new_ticket.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        global stop_threads
        while not stop_threads:
            time.sleep(0.5)

        dial_results.put(None)
        sys.exit(0)

    def kill(self):
        try:
            self.player.kill()
        except:
            pass

class CheckTicket:
    def __init__(self, callback):
        self.player = None
        self.dial = Dial(callback=callback)

    def start(self):
        self.player = subprocess.Popen(["aplay", "current_ticket.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        global stop_threads
        while not stop_threads:
            time.sleep(0.5)

        dial_results.put(None)
        sys.exit(0)

    def kill(self):
        try:
            self.player.kill()
        except:
            pass
    
class OperatorTree:

    def __init__(self, callback):
        self.player = None
        self.dial = Dial(callback=callback)

    def start(self):
        global stop_threads

        self.player = subprocess.Popen(["aplay", "operator.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while self.player.poll() is None and not stop_threads:
            time.sleep(0.5)

        if stop_threads:
            dial_results.put(None)
            sys.exit(0)


        self.player = subprocess.Popen(["mpg123", "--loop", "-1", "-q", "hold.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while not stop_threads:
            count = 0
            while not stop_threads and count < 30:
                time.sleep(0.5)
                count += 1

            if stop_threads:
                dial_results.put(None)
                sys.exit()

            self.player.send_signal(signal.SIGSTOP)
            self.player2 = subprocess.Popen(["aplay", "continue_holding.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            while not stop_threads and self.player2.poll() is None:
                time.sleep(0.5)
            self.player.send_signal(signal.SIGCONT)
        
        if stop_threads:
            dial_results.put(None)
            sys.exit(0)
        
        
    def kill(self):
        try:
            self.player.kill()
        except:
            pass

        try:
            self.player2.kill()
        except:
            pass

class IntroTree:
    dialOptions = {"1": NewTicket, "2": CheckTicket, "3": OperatorTree, "9": ResetPasswordTree}

    def __init__(self, callback):
        self.dial = Dial(1, callback)
        self.player = None

    def start(self):

        global stop_threads
        while (self.dial.done() != True and not stop_threads):
            if self.player is None:
                self.player = subprocess.Popen(["aplay", "intro.wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(0.5)

        try:
            self.player.kill()
        except:
            pass
        
        if stop_threads:
            dial_results.put(None)
            sys.exit(0)

        if self.dial.getnumber() in IntroTree.dialOptions:
            dial_results.put(IntroTree.dialOptions[self.dial.getnumber()])
        else:
            dial_results.put(BadOption)


class BadOption:

    def __init__(self, callback):
        self.player = None
        self.dial = Dial(callback=callback)

    def start(self):
        self.player = subprocess.Popen(["aplay", "bad_option.wav"])
        global stop_threads

        while not stop_threads:
            time.sleep(0.5)

        dial_results.put(None)

        sys.exit(0)
    
    def kill(self):
        try:
            self.player.kill()
        except:
            pass

class DialTone:
    dialOptions = {"6463725": IntroTree}

    def __init__(self, callback):
        self.player = None
        self.dial = Dial(7, callback)

    def start(self):
        while(self.dial.calling == False):
            time.sleep(0.1)

        global stop_threads 
        while(self.dial.firstPickup() and not stop_threads ):
            if self.player is None:
                self.player = subprocess.Popen(["mpg123", "--loop", "-1", "-q", "dial_tone2.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(0.1)

        try:
            self.player.kill()
        except:
            pass

        if stop_threads:
            dial_results.put(None)
            sys.exit(0)
            return

        while(self.dial.done() != True and not stop_threads):
            time.sleep(0.5)

        if stop_threads:
            dial_results.put(None)
            sys.exit(0)
            return

        if self.dial.getnumber() in DialTone.dialOptions:
            dial_results.put(DialTone.dialOptions[self.dial.getnumber()])
        else:
            dial_results.put(BusyTone)

        sys.exit(0)

    def kill(self):
        try:
            self.player.kill()
        except:
            pass

class BusyTone:
    def __init__(self, callback):
        self.player = None
        self.dial = Dial(callback=callback)

    def start(self):
        self.player = subprocess.Popen(["mpg123", "--loop", "-1", "-q", "busy.mp3"])
        global stop_threads


        while not stop_threads:
            time.sleep(0.5)

        dial_results.put(None)

        sys.exit(0)

    def kill(self):
        try:
            self.player.kill()
        except:
            pass

class Manager:
    def __init__(self):

        self.init = True
        self.currentTree = None
        self.lastNumber = 0

    def callback(self):
        self.lastNumber = 0
        global stop_threads
        stop_threads = True
        try:
            self.currentTree.kill()
        except:
            pass

        sys.exit(0)

    def PlayDialTone(self):
        self.currentTree = DialTone(self.callback)
        self.currentTree.start()

    def PlayIntro(self):
        self.currentTree = IntroTree(self.callback)
        self.currentTree.start()

    def PlayBusyTone(self):
        self.currentTree = BusyTone(self.callback)
        self.currentTree.start()

    def PlayBadOption(self):
        self.currentTree = BadOption(self.callback)
        self.currentTree.start()

    def PlayNewTicket(self):
        self.currentTree = NewTicket(self.callback)
        self.currentTree.start()

    def PlayCheckTicket(self):
        self.currentTree = CheckTicket(self.callback)
        self.currentTree.start()

    def PlayOperatorTree(self):
        self.currentTree = OperatorTree(self.callback)
        self.currentTree.start()

    def PlayResetPasswordTree(self):
        self.currentTree = ResetPasswordTree(self.callback)
        self.currentTree.start()

    def start(self):
        global stop_threads

        while True:
            self.thread = threading.Thread(target=self.PlayDialTone)
            self.thread.daemon = True
            self.thread.start()

            while(self.thread.is_alive()):
                time.sleep(0.5)

            while not stop_threads:
                r = dial_results.get()
                if r is BusyTone:
                    self.thread = threading.Thread(target=self.PlayBusyTone)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is BadOption:
                    self.thread = threading.Thread(target=self.PlayBadOption)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is IntroTree:
                    self.thread = threading.Thread(target=self.PlayIntro)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is NewTicket:
                    self.thread = threading.Thread(target=self.PlayNewTicket)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is CheckTicket:
                    self.thread = threading.Thread(target=self.PlayCheckTicket)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is OperatorTree:
                    self.thread = threading.Thread(target=self.PlayOperatorTree)
                    self.thread.daemon = True
                    self.thread.start()
                elif r is ResetPasswordTree:
                    self.thread = threading.Thread(target=self.PlayResetPasswordTree)
                    self.thread.daemon = True
                    self.thread.start()


            if stop_threads:
                stop_threads = False
    
def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServerExit

if  __name__ == "__main__":

    manager = Manager()
    manager.start()
    
    while True:
        time.sleep(1)

