"""
Functions in this file

ShelveExplorer()


"""
from pathlib import Path
import os
import sys
import time
import numpy
import threading
import cv2
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from timeit import default_timer as timer
from tkinter import BOTH, END, LEFT
from tkintertable import TableCanvas, TableModel

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


class ShelveExplorer():
    def __init__(self, w):
        self.w = w

        global value, im, width, height, stamp_list, line_list, tulos_lista, time_list
        value = 1
        im = Image.open(Path("test_images") / "1-peloton-finishlynx.jpg")
        date = datetime.now()
        stamp_list = []
        line_list = []
        tulos_lista = []
        time_list = []
        width, height = im.size
        for i in range (width):
            date_combo = date + timedelta(milliseconds=i)
            time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
            stamp_list.append(time_stamp)


        # global stamp_list   
        print(len(stamp_list))
    
    
    
    def explore(self):
            print(value)
            pic = ImageTk.PhotoImage(im.crop((0, 0, 1000, height)))
            self.w.ShelveExplorerCanvas3.create_image(0, 0, image=pic, anchor="nw")
            self.w.ShelveExplorerCanvas3.image = pic
            
            
    def goRight(self):

     global value, width
     
     print(width)
     if value > width/1000:
         print("Cant go right")
     else:
         print("Going right")
         print(value)
         self.w.ShelveExplorerCanvas3.delete("all")
         pic = ImageTk.PhotoImage(im.crop(((value*1000), 0, ((1+value)*1000), height)))
         self.w.ShelveExplorerCanvas3.create_image(0, 0, image=pic, anchor="nw")
         self.w.ShelveExplorerCanvas3.image = pic
         value += 1
         self.keepLines()

    def goLeft(self):
        global value, width
        if value == 1:
            print("Cant go left")
            
            

        else:
            value -= 1
            print("Going left")
            self.w.ShelveExplorerCanvas3.delete("all")
            pic = ImageTk.PhotoImage(im.crop(((value*1000-1000), 0, (value*1000), height)))
            self.w.ShelveExplorerCanvas3.create_image(0, 0, image=pic, anchor="nw")
            self.w.ShelveExplorerCanvas3.image = pic
            
            print(value)
            self.keepLines()

    def leftClick(self, event):
        global line_list, value, time_list
        
        self.w.ShelveExplorerCanvas3.create_line(event.x, 0, event.x, height, tag='line')
        line_list.append(event.x+(value*1000))
        print(line_list)
        time_list.append(self.motion(event))

        # no listing kept other than table, future use should be with lists
        self.times = self.motion(event)

        self.tableFiller()
        
    def tableFiller(self):
        global time_list
        data = self.w.ExplorerResultsLabelframe1.table.model.data
        cols = self.w.ExplorerResultsLabelframe1.table.model.columnNames #get the current columns
        
        #data[row][col] = value #use row and column names, not cell coordinates
        print(cols)
        # self.w.ExplorerResultsLabelframe1.table.clearData()
        # self.w.ExplorerResultsLabelframe1.table.new
        # self.w.ExplorerResultsLabelframe1.table.redrawTable()
        # for times in time_list:
        #     # check if time already on table here
        #     self.w.ExplorerResultsLabelframe1.table.addRow(Time=times)
        self.w.ExplorerResultsLabelframe1.table.addRow(Time=self.times)
        self.w.ExplorerResultsLabelframe1.table.redrawTable()
        # self.w.ExplorerResultsLabelframe1.table.adjustColumnWidths()
        # self.w.ExplorerResultsLabelframe1.table.autoResizeColumns()
        
        




    def deleteLines(self):
        global line_list
        line_list = []
        time_list.clear()
        print("Deleted lines")
        self.w.ShelveExplorerCanvas3.delete('line')

    def keepLines(self):
        global line_list, value, working_line_list
        line_list.sort()
        print(line_list)
        print("value is " + str(value))
        value_thousands = 1000*value
        print("valuethousands is " + str(value_thousands))
        for items in line_list:
            if items > value_thousands and items < value_thousands+1000:
                self.w.ShelveExplorerCanvas3.create_line(items-value_thousands, 0, items-value_thousands, height, tag='line')
                print(items)
            
           
        
        

    def motion(self, event):
      global stamp_list
      try:
        working_list = stamp_list[value*1000:value*1000+1000]
        x = event.x
        self.w.LineTimeText1.delete('1.0', END)
        self.w.LineTimeText1.insert('1.0', "Time of the frame is " + str(working_list[event.x]))
        self.w.ShelveExplorerCanvas3.delete('constant')
        self.w.ShelveExplorerCanvas3.create_line(event.x, 0, event.x, height, tag='constant')
        
        return working_list[event.x]
      except IndexError:
        pass


    def addTimes(self):
        global time_list
        model = self.w.ExplorerResultsLabelframe1.table.model
        #model.importDict(data) 
       # table.redraw()