'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
import numpy as np
import matplotlib.pyplot as plt
from pypylon import pylon as py
import cv2
import os
import tempfile


#Camera emulation
# Set environment variable PYLON_CAMEMU = x , (x = number of emulated cameras)
# OR use the os function below
# enable emulation 
# os.environ["PYLON_CAMEMU"] = "1"


width = 1920
height = 1008

#jpg to numpy

test_pattern = np.fromfunction(lambda i, j, k: j % 256, (height, width,3 ), dtype=np.int16)

test_pattern[:,:,1]

print("testi array")
print(test_pattern[0,:])

img_dir = tempfile.mkdtemp()

# img_dir = "..\\test_images\\1-peloton-finishlynx.jpg"

for i in range(256):
    pattern = np.roll(test_pattern,i,axis=1)
    cv2.imwrite(os.path.join(img_dir,"pattern_%03d.png"%i), pattern)


cam = py.InstantCamera(py.TlFactory.GetInstance().CreateFirstDevice())
cam.Open()

cam.ImageFilename = img_dir


# enable image file test pattern
cam.ImageFileMode = "On"

# disable testpattern [ image file is "real-image"]
cam.TestImageSelector = "Off"

# choose one pixel format. camera emulation does conversion on the fly
cam.PixelFormat = "Mono8"


cam.StartGrabbingMax(100)

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

# converting to opencv bgr format
converter.OutputPixelFormat = py.PixelType_BGR8packed
converter.OutputBitAlignment = py.OutputBitAlignment_MsbAligned

while cam.IsGrabbing():
    grabResult = cam.RetrieveResult(5000, py.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        cv2.namedWindow('title', cv2.WINDOW_NORMAL)
        cv2.imshow('press esc', img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    grabResult.Release()
    
# Releasing the resource    
cam.StopGrabbing()

cv2.waitKey(0)

cv2.destroyAllWindows()