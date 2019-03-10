from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from pathlib import Path
import os


root = Tk()
root.title('Face')
T = Text(root, height=1, width=30)

path = Path("test_images") / "1-peloton-finishlynx.jpg"
im = Image.open(path)
w, h = im.size

print(w/1000)

pic = ImageTk.PhotoImage(im.crop((0, 0, 1000, h)))


canvas = Canvas(root, width = pic.width(), height = pic.height() )
canvas.create_image(0, 0, anchor = NW, image=pic)
value = 1
working_list = []
print("hello")


def leftClick(event):
    print("left")
    canvas.delete('text')
    canvas.create_line(event.x, 0, event.x, pic.height(), tag='line')
    
def deleteText():
    print("Deleted lines")
    canvas.delete('line')

def goLeft():
    global value
    if value == 1:
        print("Cant go right")

    else:
        value -= 1
        print("Going left")
        canvas.delete("all")
        pic = ImageTk.PhotoImage(im.crop(((value*1000-1000), 0, (value*1000), h)))
        canvas.create_image(0, 0, anchor = NW, image=pic)
        canvas.image = pic
        
        print(value)

def goRight():
     global value
     if value > w/1000:
         print("Cant go right")
     else:
         print("Going right")
         print(value)
         canvas.delete("all")
         pic = ImageTk.PhotoImage(im.crop(((value*1000), 0, ((1+value)*1000), h)))
         canvas.create_image(0, 0, anchor = NW, image=pic)
         canvas.image = pic
         value += 1
    

#def motion(event):
   # pass
  #  try:
       # working_list = stamp_list[value*1000:value*1000+1000]
      #  x = event.x
     #  T.delete('1.0', END)
      #  T.insert('1.0', "Time of the frame is " + str(working_list[event.x]))
      #  canvas.delete('constant')
     #   canvas.create_line(event.x, 0, event.x, pic.height(), tag='constant')

  #  except IndexError:
        #    pass

B = Button(text ="Delete lines", command = deleteText)
C = Button(text ="Go right", command = goRight)
D = Button(text ="Go left", command = goLeft)
canvas.bind("<Button-1>", leftClick)
#canvas.bind("<Button-3>", rightClick)
#canvas.bind('<Motion>', motion)
T.pack()
B.pack()
C.pack()
D.pack()
canvas.pack()
#createSplits()
#create_stamps(stamp_list)
root.mainloop()
