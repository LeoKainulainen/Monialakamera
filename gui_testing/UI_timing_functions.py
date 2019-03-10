"""
Functions in this file

Ticking()
TimerStart()
TimerStop()
CapturePause()
TimerTick()


"""
import sys
import time
from datetime import datetime
from timeit import default_timer as timer

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


global Timerstarted
Timerstarted = False

class Clock:
    def __init__(self,w):
        print("Clock started")
        global Timerstarted
        Timerstarted = 0
        self.w = w
        # self.top = top
    def Ticking(self):
        # get the current local time from the PC
        self.time1 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        # clock.config(text=time2)
        self.w.CurrentTimeText2.insert(0.0, "TEST")
        # w.TimerText2.configure(background="blue")
        self.w.CurrentTimeText2.delete(0.0, tk.END)
        self.w.CurrentTimeText2.insert(0.0, self.time1)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
        self.w.CurrentTimeText2.after(200, self.Ticking)
    def TimerTick(self):
    # self.Timerstarted

        print("Timertick", Timerstarted)

        if Timerstarted == True:
            # get the current local time from the PC
            
            # time2 = datetime.now().strftime("%H:%M:%S.%f")
            addtime = timer()
            timer2 = addtime - start
            hours, rem = divmod(addtime-start, 3600)
            minutes, seconds = divmod(rem, 60)
            timer2 = ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
            # print(timer2)
            # if time string has changed, update it
            # clock.config(text=time2)
            # self.CurrentTimeText2.insert(0.0, "")
            self.w.TimerText2.delete(0.0, tk.END)
            self.w.TimerText2.insert(0.0, timer2)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            self.w.TimerText2.after(100, self.TimerTick)
    def TimerStart(self):
        global start
        start = timer()
        self.w.TimerText2.configure(background="blue")
        print(start)
        global Timerstarted
        Timerstarted = True
        self.TimerTick()
        # Timertick2()
        print("Timer Started", Timerstarted)

    def CapturePause(self):
        global start
        start = timer()
        print(start)
        global Timerstarted
        Timerstarted = True
        self.TimerTick()
        print("Timer Started", Timerstarted)

    def TimerStop(self):
        global Timerstarted
        Timerstarted = False
        self.w.TimerText2.configure(background="green")
        self.TimerTick()
        print("Timer Stopped", Timerstarted)
