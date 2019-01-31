#===========================================================================#
#                                                                           #
#  Copyright (C) 2006 - 2018                                                #
#  IDS Imaging Development Systems GmbH                                     #
#  Dimbacher Str. 6-8                                                       #
#  D-74182 Obersulm, Germany                                                #
#                                                                           #
#  The information in this document is subject to change without notice     #
#  and should not be construed as a commitment by IDS Imaging Development   #
#  Systems GmbH. IDS Imaging Development Systems GmbH does not assume any   #
#  responsibility for any errors that may appear in this document.          #
#                                                                           #
#  This document, or source code, is provided solely as an example          #
#  of how to utilize IDS software libraries in a sample application.        #
#  IDS Imaging Development Systems GmbH does not assume any responsibility  #
#  for the use or reliability of any portion of this document or the        #
#  described software.                                                      #
#                                                                           #
#  General permission to copy or modify, but not for profit, is hereby      #
#  granted, provided that the above copyright notice is included and        #
#  reference made to the fact that reproduction privileges were granted     #
#  by IDS Imaging Development Systems GmbH.                                 #
#                                                                           #
#  IDS Imaging Development Systems GmbH cannot assume any responsibility    #
#  for the use or misuse of any portion of this software for other than     #
#  its intended diagnostic purpose in calibrating and testing IDS           #
#  manufactured cameras and software.                                       #
#                                                                           #
#===========================================================================#

# Developer Note: I tried to let it as simple as possible.
# Therefore there are no functions asking for the newest driver software or freeing memory beforehand, etc.
# The sole purpose of this program is to show one of the simplest ways to interact with an IDS camera via the uEye API.
# (XS cameras are not supported)
#---------------------------------------------------------------------------------------------------------------------------------------

#Libraries
from pyueye import ueye
import numpy as np
import cv2
import sys

#---------------------------------------------------------------------------------------------------------------------------------------

#Variables
hCam = ueye.HIDS(0)             #0: first available camera;  1-254: The camera with the specified camera ID
sInfo = ueye.SENSORINFO()
cInfo = ueye.CAMINFO()
pcImageMemory = ueye.c_mem_p()
MemID = ueye.int()
rectAOI = ueye.IS_RECT()
pitch = ueye.INT()
nBitsPerPixel = ueye.INT(24)    #24: bits per pixel for color mode; take 8 bits per pixel for monochrome
channels = 3                    #3: channels for color mode(RGB); take 1 channel for monochrome
m_nColorMode = ueye.INT()		# Y8/RGB16/RGB24/REG32
bytes_per_pixel = int(nBitsPerPixel / 8)
#---------------------------------------------------------------------------------------------------------------------------------------
print("START")
print()


# Starts the driver and establishes the connection to the camera
nRet = ueye.is_InitCamera(hCam, None)
if nRet != ueye.IS_SUCCESS:
    print("is_InitCamera ERROR")

# Reads out the data hard-coded in the non-volatile camera memory and writes it to the data structure that cInfo points to
nRet = ueye.is_GetCameraInfo(hCam, cInfo)
if nRet != ueye.IS_SUCCESS:
    print("is_GetCameraInfo ERROR")

# You can query additional information about the sensor type used in the camera
nRet = ueye.is_GetSensorInfo(hCam, sInfo)
if nRet != ueye.IS_SUCCESS:
    print("is_GetSensorInfo ERROR")

nRet = ueye.is_ResetToDefault( hCam)
if nRet != ueye.IS_SUCCESS:
    print("is_ResetToDefault ERROR")

# Set display mode to DIB
nRet = ueye.is_SetDisplayMode(hCam, ueye.IS_SET_DM_DIB)



# Can be used to set the size and position of an "area of interest"(AOI) within an image
nRet = ueye.is_AOI(hCam, ueye.IS_AOI_IMAGE_GET_AOI, rectAOI, ueye.sizeof(rectAOI))
if nRet != ueye.IS_SUCCESS:
    print("is_AOI ERROR")

width = rectAOI.s32Width
height = rectAOI.s32Height

# Prints out some information about the camera and the sensor
print("Camera model:\t\t", sInfo.strSensorName.decode('utf-8'))
print("Camera serial no.:\t", cInfo.SerNo.decode('utf-8'))
print("Maximum image width:\t", width)
print("Maximum image height:\t", height)
print()



#########
nRet = ueye.is_SetAutoParameter(hCam, ueye.IS_SET_ENABLE_AUTO_GAIN, ueye.double(1), ueye.double(0))
print("is_SetAutoParameter returns " + str(nRet))

#fps

targetFPS = ueye.double(160) # insert here which FPS you want
actualFPS = ueye.double(0)
nRet = ueye.is_SetFrameRate(hCam,targetFPS,actualFPS)
print("is_SetFrameRate returns " + str(nRet) + ", Actual FPS is: " + str(actualFPS) + "Target FPS is: " + str(targetFPS))

#get pixelclock

#var

nPixelClock = ueye.UINT()
nRet = ueye.is_PixelClock(hCam, ueye.IS_PIXELCLOCK_CMD_GET, nPixelClock, ueye.sizeof(nPixelClock))
print("Current PixelClock", nPixelClock)


#set pixelclock
#nPixelClock = ueye.UINT()

#set AutoExposure
nRet = ueye.is_SetAutoParameter(hCam, ueye.IS_SET_ENABLE_AUTO_SHUTTER, ueye.double(1), ueye.double(0))
print("is_SetAutoParameter returns " + str(nRet))


## set color

# nRet = ueye.is_SetColorMode(hCam, ueye.IS_CM_BGR8_PACKED)

# print("SetColorMode IS_CM_BGR8_PACKED returns " + str(nRet))
m_nColorMode = ueye.IS_CM_BGRA8_PACKED
nBitsPerPixel = ueye.INT(32)
bytes_per_pixel = int(nBitsPerPixel / 8)
print("IS_COLORMODE_CBYCRY: ", )
print("\tm_nColorMode: \t\t", m_nColorMode)
print("\tnBitsPerPixel: \t\t", nBitsPerPixel)
print("\tbytes_per_pixel: \t\t", bytes_per_pixel)
print()



## AOI Merge mode
# https://en.ids-imaging.com/manuals/uEye_SDK/EN/uEye_Manual_4.91.1/index.html

nVerticalAoiMergeMode = ueye.int(0)
nVerticalAoiMergePosition = ueye.int(0)

# /* Read current vertical AOI merge mode */


nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE, nVerticalAoiMergeMode, ueye.sizeof(nVerticalAoiMergeMode))
if nRet == ueye.IS_SUCCESS:
    print("AOI Merge MODE:", nVerticalAoiMergeMode)
    if nVerticalAoiMergeMode == ueye.IS_VERTICAL_AOI_MERGE_MODE_FREERUN:
    # /* Read current AOI merge position */
        nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION, nVerticalAoiMergePosition, ueye.sizeof(nVerticalAoiMergePosition))
        print("AOI Merge Position:", nVerticalAoiMergePosition)

# /* Set vertical AOI merge mode */
nVerticalAoiMergeMode = ueye.IS_VERTICAL_AOI_MERGE_MODE_FREERUN
nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_MODE, nVerticalAoiMergeMode, ueye.sizeof(nVerticalAoiMergeMode))

if nRet == ueye.IS_SUCCESS:
# /* Read and set new maximum AOI */
    pInfo = ueye.SENSORINFO()

    nRet = ueye.is_GetSensorInfo(hCam, pInfo)

    maxWidth = ueye.int(pInfo.nMaxWidth)
    maxHeight = ueye.int(pInfo.nMaxHeight)


# rectAOI = ueye.IS_RECT()

# C
# rectAOI.s32X = 0;
# rectAOI.s32Y = 0;
 
    rectAOI.s32X = ueye.INT(0)
    rectAOI.s32Y = ueye.INT(0)

# C
# rectAOI.s32Width = maxWidth;
# rectAOI.s32Height = maxHeight;

    maxWidth = rectAOI.s32Width
    maxHeight = rectAOI.s32Height

# C
# nRet = is_AOI(hCam, IS_AOI_IMAGE_SET_AOI, (void*)&rectAOI, sizeof(rectAOI));

    nRet = ueye.is_AOI(hCam, ueye.IS_AOI_IMAGE_SET_AOI, rectAOI, ueye.sizeof(rectAOI))

  
# /*Set vertical AOI merge position */

# C
# INT nVerticalAoiMergePosition = 100;
# nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_POSITION,
#                         (void*)&nVerticalAoiMergePosition, sizeof(nVerticalAoiMergePosition));
# }

    nVerticalAoiMergePosition = ueye.INT(height/2)

    nRet = is_DeviceFeature(hCam, ueye.IS_DEVICEFEATURE_CMD_SET_VERTICAL_AOI_MERGE_POSITION, nVerticalAoiMergePosition, ueye.sizeof(nVerticalAoiMergePosition))

# /* Read current vertical AOI merge mode */

nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE, nVerticalAoiMergeMode, ueye.sizeof(nVerticalAoiMergeMode))
if nRet == ueye.IS_SUCCESS:
    print("AOI Merge MODE")
    print(nVerticalAoiMergeMode)


#---------------------------------------------------------------------------------------------------------------------------------------

# Allocates an image memory for an image having its dimensions defined by width and height and its color depth defined by nBitsPerPixel
nRet = ueye.is_AllocImageMem(hCam, width, height, nBitsPerPixel, pcImageMemory, MemID)
if nRet != ueye.IS_SUCCESS:
    print("is_AllocImageMem ERROR")
else:
    # Makes the specified image memory the active memory
    nRet = ueye.is_SetImageMem(hCam, pcImageMemory, MemID)
    if nRet != ueye.IS_SUCCESS:
        print("is_SetImageMem ERROR")
    else:
        # Set the desired color mode
        nRet = ueye.is_SetColorMode(hCam, m_nColorMode)



# Activates the camera's live video mode (free run mode)
nRet = ueye.is_CaptureVideo(hCam, ueye.IS_DONT_WAIT)
if nRet != ueye.IS_SUCCESS:
    print("is_CaptureVideo ERROR")

# Enables the queue mode for existing image memory sequences
nRet = ueye.is_InquireImageMem(hCam, pcImageMemory, MemID, width, height, nBitsPerPixel, pitch)
if nRet != ueye.IS_SUCCESS:
    print("is_InquireImageMem ERROR")
else:
    print("Press q to leave the programm")

#---------------------------------------------------------------------------------------------------------------------------------------


# Continuous image display
while(nRet == ueye.IS_SUCCESS):

    # In order to display the image in an OpenCV window we need to...
    # ...extract the data of our image memory
    array = ueye.get_data(pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False)

    # bytes_per_pixel = int(nBitsPerPixel / 8)

    # ...reshape it in an numpy array...
    frame = np.reshape(array,(height.value, width.value, bytes_per_pixel))

    # ...resize the image by a half

    cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)

    cv2width = int(width)
    cv2height = int(height/2) 


    cv2.line(frame,(0,cv2height),(cv2width,cv2height),(255,255,255),5)

    frame = cv2.resize(frame,(0,0),fx=0.25, fy=0.25)
    
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
    
#---------------------------------------------------------------------------------------------------------------------------------------
    #Include image data processing here

#---------------------------------------------------------------------------------------------------------------------------------------

    #...and finally display it
    cv2.imshow("SimpleLive_Python_uEye_OpenCV", frame)

    # Press q if you want to end the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#---------------------------------------------------------------------------------------------------------------------------------------

# Releases an image memory that was allocated using is_AllocImageMem() and removes it from the driver management
ueye.is_FreeImageMem(hCam, pcImageMemory, MemID)

# Disables the hCam camera handle and releases the data structures and memory areas taken up by the uEye camera
ueye.is_ExitCamera(hCam)

# Destroys the OpenCv windows
cv2.destroyAllWindows()

print()
print("END")
