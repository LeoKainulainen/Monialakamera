from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from pathlib import Path
import os

root = Tk()
root.title('Face')
T = Text(root, height=1, width=30)

img_path1 = Path("test_images") / "1-peloton-finishlynx.png"
im = Image.open(img_path1)
im = im.resize((1000, 483), Image.ANTIALIAS) 
pic = ImageTk.PhotoImage(im)

stamp_list = []
def create_stamps(stamp_list):
    x, y = im.size
    date = datetime.now()

    for i in range (x):
        date_combo = date + timedelta(seconds=i)
        time_stamp = date_combo.strftime('%M:%S')
        stamp_list.append(time_stamp)
    
        
canvas = Canvas(root, width = pic.width(), height = pic.height() )
canvas.create_image(0, 0, anchor = NW, image=pic)





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


    
    
    

B = Button(text ="Delete lines", command = deleteText)
canvas.bind("<Button-1>", leftClick)
#canvas.bind("<Button-3>", rightClick)
canvas.bind('<Motion>', motion)
T.pack()
B.pack()
canvas.pack()

create_stamps(stamp_list)
root.mainloop()

