import os
from pathlib import Path
from datetime import datetime, timedelta
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Face')
T = Text(root, height=1, width=40)

img_path1 = Path("test_images") / "1-light.jpg"
img_dir = Path("faces_out")
im = Image.open(img_path1)
im = im.resize((1000, 483), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(im)
stamp_list = []
with open(os.path.join(Path(img_dir), "time_stamps.txt"), "r") as fileR:
    print(fileR)
    stamp_list = eval(fileR.readline())

def create_stamps(stamp_list_in):
    x, y = im.size
    print(x)
    date = datetime.now()

    for i in range(x):
        date_combo = date + timedelta(milliseconds=i)
        time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        stamp_list_in.append(time_stamp)

canvas = Canvas(root, width=pic.width(), height=pic.height())
canvas.create_image(0, 0, anchor=NW, image=pic)

def leftClick(event):
    print("left")
    canvas.delete('text')
    canvas.create_line(event.x, 0, event.x, pic.height(), tag='line')

def deleteText():
    print("Deleted lines")
    canvas.delete('line')

def motion(event):
    x = event.x
    T.delete('1.0', END)
    T.insert('1.0', "Time of the frame is " + str(stamp_list[event.x]))

B = Button(text="Delete lines", command=deleteText)
canvas.bind("<Button-1>", leftClick)
#canvas.bind("<Button-3>", rightClick)
canvas.bind('<Motion>', motion)
T.pack()
B.pack()
canvas.pack()

# create_stamps(stamp_list)
root.mainloop()
