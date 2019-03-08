#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 08, 2019 07:26:51 AM EET  platform: Linux

import sys

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

import UI_Page_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    UI_Page_support.set_Tk_var()
    top = Toplevel1 (root)
    UI_Page_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    UI_Page_support.set_Tk_var()
    top = Toplevel1 (w)
    UI_Page_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font14 = "-family {DejaVu Sans} -size 0"
        font16 = "-family {DejaVu Sans} -size 12"
        font18 = "-family {DejaVu Sans} -size 24 -weight bold"
        font19 = "-family {DejaVu Sans} -size 28 -weight bold"
        font21 = "-family {DejaVu Sans} -size 16"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1351x696+-10+14")
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top, font=('DejaVu Sans', 12, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=0.996
                , relwidth=1.001)
        self.TNotebook1.configure(width=1352)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="CameraUI",compound="left",underline="-1",)
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Shelve Explorer", compound="none"
                ,underline="-1", )
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="IDS Settings", compound="left"
                ,underline="-1", )

        self.StripCanvas1 = tk.Canvas(self.TNotebook1_t0)
        self.StripCanvas1.place(relx=0.0, rely=0.299, relheight=0.643
                , relwidth=0.808)
        self.StripCanvas1.configure(borderwidth="2")
        self.StripCanvas1.configure(relief='ridge')
        self.StripCanvas1.configure(selectbackground="#c4c4c4")
        self.StripCanvas1.configure(width=1091)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.007, rely=0.015, height=28, width=101)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Load Shelve''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.007, rely=0.09, height=28, width=99)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Save Shelve''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.319, rely=0.015, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Button''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.015, rely=0.149, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.378, rely=0.015, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Button''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.437, rely=0.015, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Button''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.281, rely=0.075, height=28, width=119)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.LoadParticipantsCSV)
        self.Button1.configure(text='''Load Participants''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Load the participants csv''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.378, rely=0.075, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Button''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.437, rely=0.075, height=28, width=99)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.SaveResultsCSV)
        self.Button1.configure(text='''Save Results''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Save the results as CSV''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.319, rely=0.134, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.378, rely=0.134, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.437, rely=0.134, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.319, rely=0.209, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.378, rely=0.209, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.526, rely=0.254, height=28, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.StripShowNormal)
        self.Button1.configure(text='''Normal Strip''')
        self.Button1.configure(width=89)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Show the normal strip''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.926, rely=0.015, height=98, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.TimerStop)
        self.Button1.configure(text='''STOP TIMER''')
        self.Button1.configure(wraplength="70")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Stop the timer''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.778, rely=0.015, height=98, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.TimerStart)
        self.Button1.configure(text='''START (TIMER) (CAPTURE)''')
        self.Button1.configure(wraplength="70")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Start the Timer and camera capture''', delay=0.5)

        self.StripScrollScale1 = tk.Scale(self.TNotebook1_t0, from_=0.0, to=100.0)
        self.StripScrollScale1.place(relx=0.007, rely=0.94, relwidth=0.799
                , relheight=0.0, height=64, bordermode='ignore')
        self.StripScrollScale1.configure(activebackground="#f9f9f9")
        self.StripScrollScale1.configure(font=font16)
        self.StripScrollScale1.configure(length="1074")
        self.StripScrollScale1.configure(orient="horizontal")
        self.StripScrollScale1.configure(sliderlength="50")
        self.StripScrollScale1.configure(sliderrelief="groove")
        self.StripScrollScale1.configure(tickinterval="1.0")
        self.StripScrollScale1.configure(troughcolor="#d9d9d9")
        self.StripScrollScale1.configure(variable=UI_Page_support.StripScrollbarNumFrames)
        self.StripScrollScale1.configure(width=20)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.StripScrollScale1, tooltip_font, '''Strip Scrollbar''', delay=0.5)

        self.CaptureSensScale1 = tk.Scale(self.TNotebook1_t0, from_=0.0, to=100.0)
        self.CaptureSensScale1.place(relx=0.007, rely=0.224, relwidth=0.302
                , relheight=0.0, height=40, bordermode='ignore')
        self.CaptureSensScale1.configure(activebackground="#f9f9f9")
        self.CaptureSensScale1.configure(font="-family {DejaVu Sans} -size 12")
        self.CaptureSensScale1.configure(length="404")
        self.CaptureSensScale1.configure(orient="horizontal")
        self.CaptureSensScale1.configure(troughcolor="#d9d9d9")
        self.CaptureSensScale1.configure(variable=UI_Page_support.CaptureSensitivityScale)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.CaptureSensScale1, tooltip_font, '''Capture Sensitivity''', delay=0.5)

        self.BibNumText2 = tk.Text(self.TNotebook1_t0)
        self.BibNumText2.place(relx=0.733, rely=0.239, relheight=0.054
                , relwidth=0.079)
        self.BibNumText2.configure(background="white")
        self.BibNumText2.configure(font=font19)
        self.BibNumText2.configure(selectbackground="#c4c4c4")
        self.BibNumText2.configure(width=106)
        self.BibNumText2.configure(wrap='word')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.BibNumText2, tooltip_font, '''Input Bib number of participant with corresponding line''', delay=0.5)

        self.StripTimeText2 = tk.Text(self.TNotebook1_t0)
        self.StripTimeText2.place(relx=0.615, rely=0.239, relheight=0.054
                , relwidth=0.116)
        self.StripTimeText2.configure(background="white")
        self.StripTimeText2.configure(font=font18)
        self.StripTimeText2.configure(selectbackground="#c4c4c4")
        self.StripTimeText2.configure(width=156)
        self.StripTimeText2.configure(wrap='word')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.StripTimeText2, tooltip_font, '''Time of the line on the strip''', delay=0.5)

        self.TimerText2 = tk.Text(self.TNotebook1_t0)
        self.TimerText2.place(relx=0.652, rely=0.037, relheight=0.054
                , relwidth=0.116)
        self.TimerText2.configure(background="white")
        self.TimerText2.configure(font=font18)
        self.TimerText2.configure(selectbackground="#c4c4c4")
        self.TimerText2.configure(width=156)
        self.TimerText2.configure(wrap='word')

        self.CurrentTimeText2 = tk.Text(self.TNotebook1_t0)
        self.CurrentTimeText2.place(relx=0.533, rely=0.037, relheight=0.054
                , relwidth=0.116)
        self.CurrentTimeText2.configure(background="white")
        self.CurrentTimeText2.configure(font=font19)
        self.CurrentTimeText2.configure(selectbackground="#c4c4c4")
        self.CurrentTimeText2.configure(width=156)
        self.CurrentTimeText2.configure(wrap='word')

        self.SaveShelveEntry1 = tk.Entry(self.TNotebook1_t0)
        self.SaveShelveEntry1.place(relx=0.089, rely=0.09, height=21
                , relwidth=0.123)
        self.SaveShelveEntry1.configure(background="white")
        self.SaveShelveEntry1.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.SaveShelveEntry1.configure(selectbackground="#c4c4c4")

        self.LoadShelveEntry1 = tk.Entry(self.TNotebook1_t0)
        self.LoadShelveEntry1.place(relx=0.089, rely=0.03, height=21
                , relwidth=0.123)
        self.LoadShelveEntry1.configure(background="white")
        self.LoadShelveEntry1.configure(font="-family {DejaVu Sans Mono} -size 12")
        self.LoadShelveEntry1.configure(selectbackground="#c4c4c4")

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.615, rely=0.209, height=18, width=156)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Strip Time''')

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.533, rely=0.007, height=18, width=156)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Current Time''')

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.652, rely=0.007, height=18, width=156)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''Timer''')

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.733, rely=0.209, height=18, width=96)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(text='''BIB NUM''')

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.852, rely=0.015, height=98, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.CapturePauseResume)
        self.Button1.configure(text='''PAUSE / RESUME (CAPTURE)''')
        self.Button1.configure(wraplength="70")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Pause or resume camera capture''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.656, rely=0.097, height=38, width=149)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.k5FramesGoForward)
        self.Button1.configure(text='''+5000 frames''')
        self.Button1.configure(width=149)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Go Forward 5000 frames''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.541, rely=0.097, height=38, width=149)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(command=UI_Page_support.k5FramesGoBack)
        self.Button1.configure(text='''- 5000 frames''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Go Back 5000 frames''', delay=0.5)

        self.Scale1 = tk.Scale(self.TNotebook1_t0, from_=0.0, to=100.0)
        self.Scale1.place(relx=0.533, rely=0.149, relwidth=0.236, relheight=0.0
                , height=40, bordermode='ignore')
        self.Scale1.configure(activebackground="#f9f9f9")
        self.Scale1.configure(font="-family {DejaVu Sans} -size 12")
        self.Scale1.configure(orient="horizontal")
        self.Scale1.configure(troughcolor="#d9d9d9")

        self.TSeparator2 = ttk.Separator(self.TNotebook1_t0)
        self.TSeparator2.place(relx=0.007, rely=0.209, relwidth=0.519)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.822, rely=0.164, height=38, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''<-''')
        self.Button1.configure(wraplength="70")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.904, rely=0.164, height=38, width=89)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''->''')
        self.Button1.configure(wraplength="70")

        self.TSeparator4 = ttk.Separator(self.TNotebook1_t0)
        self.TSeparator4.place(relx=0.526, rely=0.0, relheight=0.209)
        self.TSeparator4.configure(orient="vertical")

        self.ResultsLabelframe1 = tk.LabelFrame(self.TNotebook1_t0)
        self.ResultsLabelframe1.place(relx=0.815, rely=0.216, relheight=0.784
                , relwidth=0.178)
        self.ResultsLabelframe1.configure(relief='groove')
        self.ResultsLabelframe1.configure(text='''Results & YOLOv3 Objects''')
        self.ResultsLabelframe1.configure(width=240)

        self.FinishDirectionRtoLRadiobutton2 = tk.Radiobutton(self.TNotebook1_t0)
        self.FinishDirectionRtoLRadiobutton2.place(relx=0.222, rely=0.164
                , relheight=0.03, relwidth=0.078)
        self.FinishDirectionRtoLRadiobutton2.configure(activebackground="#f9f9f9")
        self.FinishDirectionRtoLRadiobutton2.configure(command=UI_Page_support.FinishDirectionRtoL)
        self.FinishDirectionRtoLRadiobutton2.configure(justify='left')
        self.FinishDirectionRtoLRadiobutton2.configure(text='''Right To Left''')
        self.FinishDirectionRtoLRadiobutton2.configure(variable=UI_Page_support.FinishDirection)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.FinishDirectionRtoLRadiobutton2, tooltip_font, '''Set finishing direction right to left''', delay=0.5)

        self.FinishDirectionLtoRRadiobutton2 = tk.Radiobutton(self.TNotebook1_t0)
        self.FinishDirectionLtoRRadiobutton2.place(relx=0.148, rely=0.164
                , relheight=0.03, relwidth=0.075)
        self.FinishDirectionLtoRRadiobutton2.configure(activebackground="#f9f9f9")
        self.FinishDirectionLtoRRadiobutton2.configure(command=UI_Page_support.FinishDirectionLtoR)
        self.FinishDirectionLtoRRadiobutton2.configure(justify='left')
        self.FinishDirectionLtoRRadiobutton2.configure(text='''Left To Right''')
        self.FinishDirectionLtoRRadiobutton2.configure(variable=UI_Page_support.FinishDirection)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.FinishDirectionLtoRRadiobutton2, tooltip_font, '''Set finishing direction left to right''', delay=0.5)

        self.YoloV3Button1 = tk.Button(self.TNotebook1_t0)
        self.YoloV3Button1.place(relx=0.437, rely=0.254, height=28, width=119)
        self.YoloV3Button1.configure(activebackground="#f9f9f9")
        self.YoloV3Button1.configure(command=UI_Page_support.StripDetectYoloV3)
        self.YoloV3Button1.configure(text='''Detect with YoloV3''')
        self.YoloV3Button1.configure(width=119)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.YoloV3Button1, tooltip_font, '''Detect Objects with Yolov3''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.319, rely=0.254, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.378, rely=0.254, height=28, width=69)
        self.Button1.configure(activebackground="#f9f9f9")

        self.ShelveExplorerCanvas3 = tk.Canvas(self.TNotebook1_t1)
        self.ShelveExplorerCanvas3.place(relx=0.007, rely=0.284, relheight=0.524
                , relwidth=0.779)
        self.ShelveExplorerCanvas3.configure(borderwidth="2")
        self.ShelveExplorerCanvas3.configure(relief='ridge')
        self.ShelveExplorerCanvas3.configure(selectbackground="#c4c4c4")
        self.ShelveExplorerCanvas3.configure(width=1051)

        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.326, rely=0.209, height=48, width=119)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(command=UI_Page_support.StripGoLeft)
        self.Button3.configure(text='''Go Left''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button3, tooltip_font, '''Go left on the strip (~1000 slices)''', delay=0.5)

        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.422, rely=0.209, height=48, width=129)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(command=UI_Page_support.StripGoRight)
        self.Button3.configure(text='''Go Right''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button3, tooltip_font, '''Go right on the strip (~1000 slices)''', delay=0.5)

        self.LineTimeText1 = tk.Text(self.TNotebook1_t1)
        self.LineTimeText1.place(relx=0.526, rely=0.209, relheight=0.069
                , relwidth=0.16)
        self.LineTimeText1.configure(background="white")
        self.LineTimeText1.configure(font=font21)
        self.LineTimeText1.configure(selectbackground="#c4c4c4")
        self.LineTimeText1.configure(width=216)
        self.LineTimeText1.configure(wrap='word')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.LineTimeText1, tooltip_font, '''Time of the line on the strip''', delay=0.5)

        self.BibNumText1 = tk.Text(self.TNotebook1_t1)
        self.BibNumText1.place(relx=0.689, rely=0.209, relheight=0.069
                , relwidth=0.093)
        self.BibNumText1.configure(background="white")
        self.BibNumText1.configure(font=font19)
        self.BibNumText1.configure(selectbackground="#c4c4c4")
        self.BibNumText1.configure(width=126)
        self.BibNumText1.configure(wrap='word')

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.533, rely=0.164, height=18, width=206)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''Time''')

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.689, rely=0.164, height=18, width=126)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(text='''BIB NUM''')

        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.23, rely=0.209, height=48, width=119)
        self.Button3.configure(activebackground="#f9f9f9")
        self.Button3.configure(text='''Delete Lines''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button3, tooltip_font, '''Delete the lines from Canvas''', delay=0.5)

        self.ExplorerResultsLabelframe1 = tk.LabelFrame(self.TNotebook1_t1)
        self.ExplorerResultsLabelframe1.place(relx=0.793, rely=0.194
                , relheight=0.784, relwidth=0.2)
        self.ExplorerResultsLabelframe1.configure(relief='groove')
        self.ExplorerResultsLabelframe1.configure(text='''Results & YOLOv3 Objects''')
        self.ExplorerResultsLabelframe1.configure(width=270)

        self.PixelClockScale1 = tk.Scale(self.TNotebook1_t2, from_=0.0, to=100.0)
        self.PixelClockScale1.place(relx=0.03, rely=0.164, relwidth=0.228
                , relheight=0.0, height=40, bordermode='ignore')
        self.PixelClockScale1.configure(activebackground="#f9f9f9")
        self.PixelClockScale1.configure(font="-family {DejaVu Sans} -size 12")
        self.PixelClockScale1.configure(orient="horizontal")
        self.PixelClockScale1.configure(troughcolor="#d9d9d9")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.PixelClockScale1, tooltip_font, '''Set the Camera Pixel Clock''', delay=0.5)

        self.IDSGainScale1 = tk.Scale(self.TNotebook1_t2, from_=0.0, to=100.0)
        self.IDSGainScale1.place(relx=0.03, rely=0.269, relwidth=0.228
                , relheight=0.0, height=40, bordermode='ignore')
        self.IDSGainScale1.configure(activebackground="#f9f9f9")
        self.IDSGainScale1.configure(font="-family {DejaVu Sans} -size 12")
        self.IDSGainScale1.configure(orient="horizontal")
        self.IDSGainScale1.configure(troughcolor="#d9d9d9")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSGainScale1, tooltip_font, '''Set the Camera Gain''', delay=0.5)

        self.IDSExposureScale1 = tk.Scale(self.TNotebook1_t2, from_=0.0, to=100.0)
        self.IDSExposureScale1.place(relx=0.03, rely=0.373, relwidth=0.228
                , relheight=0.0, height=40, bordermode='ignore')
        self.IDSExposureScale1.configure(activebackground="#f9f9f9")
        self.IDSExposureScale1.configure(font="-family {DejaVu Sans} -size 12")
        self.IDSExposureScale1.configure(orient="horizontal")
        self.IDSExposureScale1.configure(troughcolor="#d9d9d9")
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSExposureScale1, tooltip_font, '''Set the Camera Exposure time''', delay=0.5)

        self.IDSExposureCheckbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.IDSExposureCheckbutton1.place(relx=0.281, rely=0.373
                , relheight=0.075, relwidth=0.083)
        self.IDSExposureCheckbutton1.configure(activebackground="#f9f9f9")
        self.IDSExposureCheckbutton1.configure(justify='left')
        self.IDSExposureCheckbutton1.configure(text='''Auto exposure''')
        self.IDSExposureCheckbutton1.configure(variable=UI_Page_support.che88)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSExposureCheckbutton1, tooltip_font, '''Enable Auto Exposure on the Camera''', delay=0.5)

        self.Checkbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.Checkbutton1.place(relx=0.289, rely=0.522, relheight=0.075
                , relwidth=0.053)
        self.Checkbutton1.configure(activebackground="#f9f9f9")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=UI_Page_support.che88)

        self.IDSGainCheckbutton1 = tk.Checkbutton(self.TNotebook1_t2)
        self.IDSGainCheckbutton1.place(relx=0.274, rely=0.269, relheight=0.075
                , relwidth=0.076)
        self.IDSGainCheckbutton1.configure(activebackground="#f9f9f9")
        self.IDSGainCheckbutton1.configure(justify='left')
        self.IDSGainCheckbutton1.configure(text='''Auto gain''')
        self.IDSGainCheckbutton1.configure(variable=UI_Page_support.che88)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSGainCheckbutton1, tooltip_font, '''Enable Auto gain on the Camera''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t2)
        self.Button1.place(relx=0.111, rely=0.045, height=28, width=111)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Load Settings''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Load Camera settings''', delay=0.5)

        self.Button1 = tk.Button(self.TNotebook1_t2)
        self.Button1.place(relx=0.215, rely=0.045, height=28, width=119)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Default settings''')

        self.Button1 = tk.Button(self.TNotebook1_t2)
        self.Button1.place(relx=0.015, rely=0.045, height=28, width=109)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Save Settings''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Button1, tooltip_font, '''Save Camera Settings (opens filedialog)''', delay=0.5)

        self.IDSPreviewCanvas2 = tk.Canvas(self.TNotebook1_t2)
        self.IDSPreviewCanvas2.place(relx=0.607, rely=0.134, relheight=0.837
                , relwidth=0.364)
        self.IDSPreviewCanvas2.configure(borderwidth="2")
        self.IDSPreviewCanvas2.configure(relief='ridge')
        self.IDSPreviewCanvas2.configure(selectbackground="#c4c4c4")
        self.IDSPreviewCanvas2.configure(width=491)

        self.IDSStopPreviewButton2 = tk.Button(self.TNotebook1_t2)
        self.IDSStopPreviewButton2.place(relx=0.704, rely=0.03, height=58
                , width=106)
        self.IDSStopPreviewButton2.configure(activebackground="#f9f9f9")
        self.IDSStopPreviewButton2.configure(command=UI_Page_support.IDSStopPreview)
        self.IDSStopPreviewButton2.configure(text='''Stop Preview''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSStopPreviewButton2, tooltip_font, '''Stop the Camera Preview''', delay=0.5)

        self.IDSStartButton2 = tk.Button(self.TNotebook1_t2)
        self.IDSStartButton2.place(relx=0.615, rely=0.03, height=58, width=106)
        self.IDSStartButton2.configure(activebackground="#f9f9f9")
        self.IDSStartButton2.configure(command=UI_Page_support.IDSStartPreview)
        self.IDSStartButton2.configure(text='''Start Preview''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSStartButton2, tooltip_font, '''Start the Preview from the camera''', delay=0.5)

        self.Label1 = tk.Label(self.TNotebook1_t2)
        self.Label1.place(relx=0.03, rely=0.134, height=18, width=77)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Pixel Clock''')

        self.Label1 = tk.Label(self.TNotebook1_t2)
        self.Label1.place(relx=0.022, rely=0.239, height=18, width=137)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Gain + Gain boost''')

        self.Label1 = tk.Label(self.TNotebook1_t2)
        self.Label1.place(relx=0.007, rely=0.343, height=18, width=127)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Exposure time''')

        self.IDSFramerateScale1 = tk.Scale(self.TNotebook1_t2, from_=0.0, to=100.0)
        self.IDSFramerateScale1.place(relx=0.289, rely=0.164, relwidth=0.228
                , relheight=0.0, height=40, bordermode='ignore')
        self.IDSFramerateScale1.configure(activebackground="#f9f9f9")
        self.IDSFramerateScale1.configure(font="-family {DejaVu Sans} -size 12")
        self.IDSFramerateScale1.configure(orient="horizontal")
        self.IDSFramerateScale1.configure(troughcolor="#d9d9d9")
        self.IDSFramerateScale1.configure(variable=UI_Page_support.IDSFramerateScale)
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.IDSFramerateScale1, tooltip_font, '''Set the Camera Framerate''', delay=0.5)

        self.Label1 = tk.Label(self.TNotebook1_t2)
        self.Label1.place(relx=0.289, rely=0.134, height=18, width=77)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(text='''Framerate''')

        self.Label4 = tk.Label(self.TNotebook1_t2)
        self.Label4.place(relx=0.793, rely=0.09, height=18, width=26)
        self.Label4.configure(text='''FPS''')
        tooltip_font = "-family {DejaVu Sans} -size 12"
        ToolTip(self.Label4, tooltip_font, '''Framerate reported by the camera''', delay=0.5)

        self.Label5 = tk.Label(self.TNotebook1_t2)
        self.Label5.place(relx=0.822, rely=0.09, height=18, width=26)
        self.Label5.configure(text='''FPS''')

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive 
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================
# How to use this class...
#   Copy the file tooltip.py into your working directory
#   import this into the _support python file created by Page
#   from tooltip import ToolTip
#   in the _support python file, create a function to attach each tooltip
#   to the widgets desired. Example:
#   ToolTip(self.widgetname, font, msg='Exit program', follow=False, delay=0.5)
# ======================================================
from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





