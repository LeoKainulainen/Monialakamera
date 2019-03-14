"""
Functions in this file

Ticking()
TimerStart()
TimerStop()
CapturePause()
TimerTick()


"""
from pathlib import Path
import os
import sys
import time
import numpy
import cv2
from PIL import Image, ImageTk
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

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from LinescanRecord import splicer_shelve


global Timerstarted
Timerstarted = False

class Clock:
    def __init__(self, w):
        print("Clock started")
        global Timerstarted
        Timerstarted = 0
        self.w = w
        # self.top = top
    def PreviewCanvasTest(self):
        data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
        self.im=Image.frombytes('L', (data.shape[1],data.shape[0]), data.astype('b').tostring())
        self.photo = ImageTk.PhotoImage(image=self.im)
        self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
    # def PreviewCanvasTest(self):
    #     # data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
    #     # self.im=Image.frombytes('L', (data.shape[1],data.shape[0]), data.astype('b').tostring())
    #     self.im = splicer_shelve.join_splices_from_shelve(0, 10)
    #     self.im = Image.fromarray(self.im)
    #     self.photo = ImageTk.PhotoImage(image=self.im)
    #     self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
    # def PreviewCanvasTest(self):
    #     self.data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
    #     self.im=Image.frombytes('L', (self.data.shape[1],self.data.shape[0]), self.data.astype('b').tostring())
    #     # self.photo = ImageTk.PhotoImage(image=Image.fromarray(data))
    #     self.photo = Image.fromarray(self.im)
    #     self.photo = ImageTk.PhotoImage(image=self.im)
    #     self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
    def Ticking(self):
        # get the current local time from the PC
        self.time1 = time.strftime('%H:%M:%S')
        # if time string has changed, update it
        # clock.config(text=time2)name
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

        # print("Timertick", Timerstarted)

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
        self.w.StripCanvas1.configure(background="grey")
        self.w.StripCanvas1.delete("all")
