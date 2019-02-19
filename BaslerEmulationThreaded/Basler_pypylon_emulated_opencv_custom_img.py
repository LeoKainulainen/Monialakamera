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

from EmuCVFunc import EmuCVFuncParallel

#Camera emulation
# Set environment variable PYLON_CAMEMU = x , (x = number of emulated cameras)
# OR use the os function below
# enable emulation 
os.environ["PYLON_CAMEMU"] = "1"


#jpg to numpy testing
# test_pattern = "..\\test_images\\1-peloton-finishlynx.jpg"
# test_pattern = cv2.imread("..\\test_images\\1-peloton-finishlynx.jpg")
# test_pattern = np.array(Image.open("..\\test_images\\1-peloton-finishlynx.jpg"))
# test_pattern = np.fromfunction(cv2.imread("..\\test_images\\1-peloton-finishlynx.jpg"))
# test_pattern = np.fromfunction(lambda i, j, k: j % 256, (height, width,3 ), dtype=np.int16)

#Pathlib used:
path = Path("test_images") / "1-peloton-finishlynx-shorter.png"

#create dir
img_dir = "test_roll"
if not os.path.exists(img_dir):
        os.makedirs(img_dir)

#Create file pattern for saving to folder
file_pattern = "pattern_" + '%05d' + ".png"

print(img_dir, file_pattern)

test_pattern = np.array(Image.open(path))

# Check image height
height = int(test_pattern.shape[0])
# Check image width
width = int(test_pattern.shape[1])
print(height, width)

#set framerate
framerate = 1000


#"AOI" width, set to 2 or 4 for accurate capture when using a camera at AOI of **** x 2px
#
# Set to 50px for "demoing" effect
#
emu_AOI_h = height
# 2px for IDS Camera & automatic detection
# 1px for getting same picture from test input picture (finishlynx-short,-shorter...) 
emu_AOI_w = 50

series_width = emu_AOI_w
#number of frames: to have whole image, set this to the width of image
series_length = width


# test_pattern[:,:,1]

# Load to memory here...?
#
# img_dir = tempfile.mkdtemp()
# img_dir = tempfile.SpooledTemporaryFile()
#
#
#




#Path of first generated image for checking pre-existing images with exists()
path = os.path.join(img_dir,file_pattern)
print(path%0)

import time
start_time = time.time()
EmuCVFuncParallel(test_pattern, file_pattern, series_length, series_width, width, height, path, img_dir).create_pattern()
print("--- %s seconds ---" % (time.time() - start_time))
# Video testing here
#reate_video()

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
# cam.PixelFormat = "Mono8"
cam.PixelFormat = "RGB8Packed"

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

        
        if frame.shape[0] == 1:
            print(frame.shape[1], "resized to", frame.shape[1]/2)
            frame = cv2.resize(frame,(int(frame.shape[1]/2),1))
        else:
            frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
        
        

        cv2.imshow('press esc', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
    
# Releasing the resource    
cam.StopGrabbing()

cv2.waitKey(0)

cv2.destroyAllWindows()