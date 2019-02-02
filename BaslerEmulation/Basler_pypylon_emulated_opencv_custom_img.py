'''
Test program for creating & emulating Linescan of specified framewdith (AOI) with Basler python wrapper API
'''
import numpy as np
import matplotlib.pyplot as plt
from pypylon import pylon as py
from PIL import Image
import cv2
import os
import tempfile
#Make paths work on Linux/Windows
from pathlib import Path

#Camera emulation
# Set environment variable PYLON_CAMEMU = x , (x = number of emulated cameras)
# OR use the os function below
# enable emulation 
os.environ["PYLON_CAMEMU"] = "1"




#jpg to numpy testing
#
# here..
# test_pattern = "..\\test_images\\1-peloton-finishlynx.jpg"
# test_pattern = cv2.imread("..\\test_images\\1-peloton-finishlynx.jpg")
# test_pattern = np.array(Image.open("..\\test_images\\1-peloton-finishlynx.jpg"))
# test_pattern = np.fromfunction(cv2.imread("..\\test_images\\1-peloton-finishlynx.jpg"))
# test_pattern = np.fromfunction(lambda i, j, k: j % 256, (height, width,3 ), dtype=np.int16)

#Pathlib used:
path = Path("test_images") / str("1-peloton-finishlynx-shorter.png")


file_pattern = "pattern_" + '%05d' + ".png"

print(file_pattern)

test_pattern = np.array(Image.open(path))

# Check image height
height = int(test_pattern.shape[0])
print(height)
# Check image width
width = int(test_pattern.shape[1])
print(width)
# width = 1920

#set framerate
framerate = 1000


#"AOI" width, set to 2 or 4 for accurate capture when using a camera at AOI of **** x 2px
#

emu_AOI_h = height
emu_AOI_w = 2

series_width = emu_AOI_w

#height from, because 1-peloton-finishlynx.jpg
# height = 1008

#number of frames: to have whole image, set this to the width of image
series_length = width


test_pattern[:,:,1]

# print("testi array")
# print(test_pattern[0,:])

# Load to memory here...?
#
# img_dir = tempfile.mkdtemp()
# img_dir = tempfile.SpooledTemporaryFile()

img_dir = "test_roll"


#Path of first generated image for checking pre-existing images with exists()
path = os.path.join(img_dir,file_pattern)
print(path%0)

def exists(path):
    "Check if path (image) exists"
    try:
        print(path%0)
        st = os.stat(path%0)
    except os.error:
        return False
    print("Image roll already exists in" + path%0)
    return True


def create_pattern():
    
    if exists(path):
        return
    else:
        print(file_pattern)
        print("creating " + str(series_length) +  " images with numpy roll")
        for i in range(series_length):
            pattern = np.roll(test_pattern,i,axis=1)
            pattern = pattern[0:0+height, -series_width:width]
            pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
            print(os.path.join(img_dir,file_pattern%i))
            cv2.imwrite(os.path.join(img_dir,file_pattern%i), pattern)
            
            # write in to memory??
            # cv2.imwrite("pattern_%03d.png"%i, pattern)

# testing video creation in opecv
def create_video():
    writer = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 500,(width,height))
    for i in range(1000):
        pattern = np.roll(test_pattern,i,axis=1)
        pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        writer.write(np.random.randint(0, 255, (width,height,3)).astype('uint8'))
        

create_pattern()
# create_video()

cam = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
cam.Open()

cam.ImageFilename = img_dir

#Camera framerate to 1000fps (probably cannot run at it without loading images to RAM)
cam.AcquisitionFrameRateEnable.SetValue(True)

cam.AcquisitionFrameRateAbs.SetValue(framerate)

# enable image file test pattern
cam.ImageFileMode = "On"

# disable testpattern [ image file is "real-image"]
cam.TestImageSelector = "Off"

# choose one pixel format. camera emulation does conversion on the fly
cam.PixelFormat = "Mono8"
# cam.PixelFormat = "RGB"


cam.StartGrabbing()

# while cam.IsGrabbing():
#     res = cam.RetrieveResult(1000)
#     print( res.Array[0,:])
#     res.Release()
    
# cam.StopGrabbing()


# cam.Close()

# # conecting to the first available camera
# camera = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())

# Grabing Continusely (video) with minimal delay
# cam.StartGrabbing(py.GrabStrategy_LatestImageOnly) 
converter = py.ImageFormatConverter()

# # converting to opencv bgr format
# converter.OutputPixelFormat = py.PixelType_BGR8packed
# converter.OutputBitAlignment = py.OutputBitAlignment_MsbAligned

# converting to opencv RGB format
converter.OutputPixelFormat = py.PixelType_RGB8packed
converter.OutputBitAlignment = py.OutputBitAlignment_MsbAligned

while cam.IsGrabbing():
    grabResult = cam.RetrieveResult(5000, py.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        frame = image.GetArray()

        cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)

        cv2width = int(width)
        cv2height = int(height/2)


        cv2.line(frame,(0,cv2height),(cv2width,cv2height),(255,0,0),5)

        frame = cv2.resize(frame,(0,0),fx=0.5, fy=0.5)
        
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        cv2.imshow('press esc', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
    
# Releasing the resource    
cam.StopGrabbing()

cv2.waitKey(0)

cv2.destroyAllWindows()