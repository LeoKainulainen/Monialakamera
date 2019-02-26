from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from pathlib import Path
import os

root = Tk()
root.title('Face')
T = Text(root, height=1, width=30)

img_dir = "faces_testing"
list_im = os.listdir(img_dir)
imgs = [Image.open(os.path.join(img_dir, i)) for i in list_im]


#savedir = 'faces_testing'

def createSplits():
    pass
    width, height = im.size
    cropped_image_size = w, h = (1000, im.size[1])
    print(im.size[0])
    frame_num = 1
    for col_i in range(0, width, w):
        for row_i in range(0, height, h):
            crop = im.crop((col_i, row_i, col_i + w, row_i + h))
            save_to= os.path.join(savedir, "counter_{:03}.png")
            crop.save(save_to.format(frame_num))
            frame_num += 1
    


#im = im.resize((1000, 500), Image.ANTIALIAS) 


pic = ImageTk.PhotoImage(imgs[0])
stamp_list = []

def create_stamps(stamp_list):
    x, y = imgs[0].size
    date = datetime.now()

    for i in range (x):
        date_combo = date + timedelta(seconds=i)
        time_stamp = date_combo.strftime('%M:%S')
        stamp_list.append(time_stamp)
   
canvas = Canvas(root, width = pic.width(), height = pic.height() )
canvas.create_image(0, 0, anchor = NW, image=pic)
value = 0
print(len(imgs))
def leftClick(event):
    print("left")
    canvas.delete('text')
    canvas.create_line(event.x, 0, event.x, pic.height(), tag='line')
    
def deleteText():
    print("Deleted lines")
    canvas.delete('line')

def goLeft():
    global value
    if value == 0:
        print("Cant go right")

    else:
        value -= 1
        print("Going left")
        canvas.delete("all")
        pic = ImageTk.PhotoImage(imgs[value])
        canvas.create_image(0, 0, anchor = NW, image=pic)
        canvas.image = pic

def goRight():
    global value
    if value == (len(imgs)-1):
        print("Cant go right")

    else:
     value += 1
     print("Going right")
     canvas.delete("all")
     pic = ImageTk.PhotoImage(imgs[value])
     canvas.create_image(0, 0, anchor = NW, image=pic)
     canvas.image = pic
    

def motion(event):
    x = event.x
    T.delete('1.0', END)
    T.insert('1.0', "Time of the frame is " + str(stamp_list[event.x]))
    canvas.delete('constant')
    canvas.create_line(event.x, 0, event.x, pic.height(), tag='constant')

B = Button(text ="Delete lines", command = deleteText)
C = Button(text ="Go right", command = goRight)
D = Button(text ="Go left", command = goLeft)
canvas.bind("<Button-1>", leftClick)
#canvas.bind("<Button-3>", rightClick)
canvas.bind('<Motion>', motion)
T.pack()
B.pack()
C.pack()
D.pack()
canvas.pack()

create_stamps(stamp_list)
root.mainloop()
