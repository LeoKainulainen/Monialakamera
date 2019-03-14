"""
Functions in this file

UpdateStripCanvas()


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



class Strip:
    def __init__(self, w):
        self.w = w
    def UpdateStripCanvas(self, stripPosition):
        # self.stripPosition = stripPosition
        # self.w.StripCanvas1.configure(background="blue")
        self.w.StripCanvas1.delete("all")
        print(type(stripPosition), stripPosition)
        stripPositionSplice = stripPosition + 10
        
        self.im = splicer_shelve.join_splices_from_shelve(stripPositionSplice-10, stripPositionSplice)
        # self.im = splicer_shelve.join_splices_from_shelve(0, 10)
        self.im = Image.fromarray(self.im)
        # self.photo = ImageTk.PhotoImage(image=self.im)
        # self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
        # self.data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
        # self.im=Image.frombytes('L', (self.data.shape[1],self.data.shape[0]), self.data.astype('b').tostring())
        self.photo = ImageTk.PhotoImage(image=self.im)
        self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
        print(stripPositionSplice-10, stripPositionSplice)
        joo
        ei
        # print("Update StripCanvas1")
        # while True:
            # cv2.imshow('frame',self.ph)
            # key = cv2.waitKey(0) & 0xff
            # if key == 27:
            #     print("Update StripCanvas1")
            #     break
    def UpdateCanvas():
        pass
