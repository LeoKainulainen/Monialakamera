"""
Functions in this file

UpdateStripCanvas()


"""
from pathlib import Path
import os
import sys
import time
import numpy
import threading
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
        threading.Thread.__init__(self)
        self.w = w
    def UpdateStripCanvas(self, stripPosition):
        self.w.StripCanvas1.delete("all")
        print(type(stripPosition), stripPosition)
        
        strip_image_height = 1000

        canvas_geo = [self.w.StripCanvas1.winfo_height(), self.w.StripCanvas1.winfo_width()]

        strip_scale_resolution = 100

        # stripPositionSplice = stripPosition + 10
        stripPositionSplice = int(canvas_geo[1])*(strip_image_height/canvas_geo[0])*((stripPosition+1*strip_scale_resolution)/strip_scale_resolution)
        # 1086 * 10
        stripPositionSpliceStart = int(canvas_geo[1])*(strip_image_height/canvas_geo[0])*((stripPosition+(1-1)*strip_scale_resolution)/strip_scale_resolution)
        
        print("Canvas Size: ", type(canvas_geo[0]),canvas_geo[0],canvas_geo[1])
        
        
        self.im = splicer_shelve.join_splices_from_shelve_columns(stripPositionSpliceStart, stripPositionSplice)
        
        
        print("stripPositionSpliceStart: ", stripPositionSpliceStart, stripPositionSplice)
        
        
        self.im = Image.fromarray(self.im)
        
        self.im.thumbnail((canvas_geo[1], canvas_geo[0]), Image.ANTIALIAS)



        # self.photo = ImageTk.PhotoImage(image=self.im)
        # self.w.StripCanvas1.create_image(0,0,image=self.photo,anchor=tk.NW)
        # self.data=numpy.array(numpy.random.random((400,500))*100,dtype=int)
        # self.im=Image.frombytes('L', (self.data.shape[1],self.data.shape[0]), self.data.astype('b').tostring())
        
        
        photo = ImageTk.PhotoImage(image=self.im)
        self.w.StripCanvas1.create_image(0,0,image=photo,anchor=tk.NW)
        self.w.StripCanvas1.image = photo

        # print("Update StripCanvas1")
        # while True:
            # cv2.imshow('frame',self.ph)
            # key = cv2.waitKey(0) & 0xff
            # if key == 27:
            #     print("Update StripCanvas1")
            #     break
    def UpdateCanvas():
        pass
