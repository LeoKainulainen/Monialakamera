#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 08, 2019 07:29:48 AM EET  platform: Linux

import sys
import UI_functions
from UI_functions import Clock
# from UI_functions import Ticking

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

def set_Tk_var():
    global StripScrollbarNumFrames
    StripScrollbarNumFrames = tk.DoubleVar()
    global CaptureSensitivityScale
    CaptureSensitivityScale = tk.DoubleVar()
    global FinishDirection
    FinishDirection = tk.StringVar()
    global che88
    che88 = tk.StringVar()
    global IDSFramerateScale
    IDSFramerateScale = tk.DoubleVar()

def k5FramesGoBack():
    print('UI_Page_support.k5FramesGoBack')
    sys.stdout.flush()

def k5FramesGoForward():
    print('UI_Page_support.k5FramesGoForward')
    sys.stdout.flush()

def CapturePauseResume():
    print('UI_Page_support.CapturePauseResume')
    sys.stdout.flush()

def FinishDirectionLtoR():
    print('UI_Page_support.FinishDirectionLtoR')
    sys.stdout.flush()

def FinishDirectionRtoL():
    print('UI_Page_support.FinishDirectionRtoL')
    sys.stdout.flush()

def IDSStartPreview():
    print('UI_Page_support.IDSStartPreview')
    sys.stdout.flush()

def IDSStopPreview():
    print('UI_Page_support.IDSStopPreview')
    sys.stdout.flush()

def LoadParticipantsCSV():
    print('UI_Page_support.LoadParticipantsCSV')
    sys.stdout.flush()

def SaveResultsCSV():
    print('UI_Page_support.SaveResultsCSV')
    sys.stdout.flush()

def StripDetectYoloV3():
    print('UI_Page_support.StripDetectYoloV3')
    sys.stdout.flush()

def StripGoLeft():
    print('UI_Page_support.StripGoLeft')
    sys.stdout.flush()

def StripGoRight():
    print('UI_Page_support.StripGoRight')
    sys.stdout.flush()

def StripShowNormal():
    print('UI_Page_support.StripShowNormal')
    sys.stdout.flush()

def TimerStart():
    print('UI_Page_support.TimerStart')
    sys.stdout.flush()
    # Timerstarted = 1
    TimerTime = Clock(w)
    TimerTime.TimerStart()
    # TimerTime.TimerTick()
    

def TimerStop():
    print('UI_Page_support.TimerStop')
    sys.stdout.flush()
    Clock(w).TimerStop()
    print("testing")

def OneTimerStartStop():
    TimerTime = Clock(w)
    TimerTime.TimerStart()




def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    Clock(w).Ticking()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import UI_Page
    UI_Page.vp_start_gui()
    



