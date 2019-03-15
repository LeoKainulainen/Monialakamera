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
import ctypes
import numpy as np
import cv2
import sys
import time

from PIL import Image, ImageTk

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


def startCamera():
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

    # def uEyeException(Exception):
    #     def __init__(error_code):
    #         error_code = error_code
    #     def __str__():
    #         return "Err: " + str(error_code)

    # def check(nRet):
    #     if nRet != ueye.IS_SUCCESS:
    #         raise uEyeException(nRet)


    # Starts the driver and establishes the connection to the camera
    global nRet
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

    rectAOI.s32Height = 8000

    width = rectAOI.s32Width
    height = rectAOI.s32Height

    global cameraHeight
    cameraHeight = height

    print("rectAOI.s32Height 1st: ", rectAOI.s32Height)

    # Prints out some information about the camera and the sensor
    print("Camera model:\t\t", sInfo.strSensorName.decode('utf-8'))
    print("Camera serial no.:\t", cInfo.SerNo.decode('utf-8'))
    print("Maximum image width:\t", width)
    print("Maximum image height:\t", height)
    print()



    #########Auto Gain
    nRet = ueye.is_SetAutoParameter(hCam, ueye.IS_SET_ENABLE_AUTO_GAIN, ueye.DOUBLE(1), ueye.DOUBLE(0))
    print("is_SetAutoParameter (Autogain) returns " + str(nRet))

    # Gain Boost
    nRet = ueye.is_SetGainBoost(hCam, ueye.INT(1))

    #fps

    # targetFPS = ueye.double(160) # insert here which FPS you want
    # actualFPS = ueye.double(0)
    # nRet = ueye.is_SetFrameRate(hCam,targetFPS,actualFPS)
    # print("is_SetFrameRate returns " + str(nRet) + ", Actual FPS is: " + str(actualFPS) + "Target FPS is: " + str(targetFPS))


    #get pixelclock
    #var
    nPixelClock = ueye.UINT()
    nRet = ueye.is_PixelClock(hCam, ueye.IS_PIXELCLOCK_CMD_GET, nPixelClock, ueye.sizeof(nPixelClock))
    nPixelClock = ueye.UINT(118)
    nRet = ueye.is_PixelClock(hCam, ueye.IS_PIXELCLOCK_CMD_SET, nPixelClock, ueye.sizeof(nPixelClock))
    print("Current PixelClock", nPixelClock)


    #set pixelclock

    #nPixelClock = ueye.UINT()
    # nRet = ueye.is_PixelClock(hCam, ueye.IS_PIXELCLOCK_CMD_SET, nPixelClock, ueye.sizeof(nPixelClock))
    # print("Current PixelClock", nPixelClock)


    #set AutoExposure
    nRet = ueye.is_SetAutoParameter(hCam, ueye.IS_SET_ENABLE_AUTO_SHUTTER, ueye.double(0), ueye.double(1))
    print("is_SetAutoParameter returns " + str(nRet))

    ms = ueye.DOUBLE(0.228)

    nRet = ueye.is_Exposure(hCam, ueye.IS_EXPOSURE_CMD_SET_EXPOSURE, ms, ueye.sizeof(ms))

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

    nVerticalAoiMergeMode = ueye.INT(0)
    nVerticalAoiMergePosition = ueye.INT(0)

    # /* Read current vertical AOI merge mode */


    nRet = ueye.INT(ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE,
        nVerticalAoiMergeMode, ueye.sizeof(nVerticalAoiMergeMode)))
    if nRet == ueye.IS_SUCCESS:
        print("AOI Merge MODE:", nVerticalAoiMergeMode)
        if nVerticalAoiMergeMode == ueye.IS_VERTICAL_AOI_MERGE_MODE_FREERUN:
        # /* Read current AOI merge position */
            nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_POSITION,
                nVerticalAoiMergePosition, ueye.sizeof(nVerticalAoiMergePosition))
            print("AOI Merge Position:", nVerticalAoiMergePosition)

    # nVerticalAoiMergeMode = ueye.INT(1)

    # /* Set vertical AOI merge mode */
    # temp = ueye.int()
    # smode = ueye.INT(nVerticalAoiMergeMode)
    # nVerticalAoiMergeMode = ueye.IS_VERTICAL_AOI_MERGE_MODE_FREERUN
    nVerticalAoiMergeMode = ueye.IS_VERTICAL_AOI_MERGE_MODE_TRIGGERED_SOFTWARE

    nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_MODE,
        ueye.INT(nVerticalAoiMergeMode), ueye.sizeof(nVerticalAoiMergeMode))

    #------ Supported features

    # capVerticalAoiMergeMode = ueye.IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE
    # nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE,
    #     ueye.INT(capVerticalAoiMergeMode), ueye.sizeof(capVerticalAoiMergeMode))

    # INT nSupportedFeatures;
    # INT nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_FEATURES,
    #                           (void*)&nSupportedFeatures, sizeof(nSupportedFeatures));
    # if (nRet == IS_SUCCESS)
    # {
    # if (nSupportedFeatures & IS_DEVICE_FEATURE_CAP_LINESCAN_MODE_FAST)
    # {
    #   // Enable line scan mode
    #   INT nMode = IS_DEVICE_FEATURE_CAP_LINESCAN_MODE_FAST;
    #   nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_SET_LINESCAN_MODE, (void*)&nMode,
    #                           sizeof(nMode));
    #   // Disable line scan mode
    #   nMode = 0;
    #   nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_SET_LINESCAN_MODE, (void*)&nMode,
    #                           sizeof(nMode));
    #   // Return line scan mode
    #   nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_LINESCAN_MODE, (void*)&nMode,
    #                           sizeof(nMode));
    # }

    nSupportedFeatures = ueye.INT()

    nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_SUPPORTED_FEATURES,
        nSupportedFeatures, ueye.sizeof(nSupportedFeatures))

    # if nRet == ueye.IS_SUCCESS:
    #     if nSupportedFeatures & ueye.IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE:
    #         ## Check IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE exists?
    #         print("IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE is a feature",)
    #         nMode = ueye.IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE
    #         nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CAP_VERTICAL_AOI_MERGE,
    #             ueye.INT(nMode), ueye.sizeof(nMode))

    #------

    if nRet == ueye.IS_SUCCESS:
    # /* Read and set new maximum AOI */
        pInfo = ueye.SENSORINFO()

        nRet = ueye.is_GetSensorInfo(hCam, pInfo)

        maxWidth = ueye.int(pInfo.nMaxWidth)
        maxHeight = ueye.int(pInfo.nMaxHeight)

        print("ueye.int(pInfo.nMaxHeight)", ueye.int(pInfo.nMaxHeight))


    # rectAOI = ueye.IS_RECT()

    # C
    # rectAOI.s32X = 0;
    # rectAOI.s32Y = 0;q
    
        rectAOI.s32X = ueye.INT(0)
        rectAOI.s32Y = ueye.INT(0)
        # rectAOI.s32Y = ueye.INT(int(maxHeight/2))

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

        # nVerticalAoiMergePosition = ueye.INT(int(height/2))

        # nVerticalAoiMergePosition = ueye.INT(int(1216/2))

        nVerticalAoiMergePosition = ueye.INT(608)

        print("rectAOI.s32Height", height)
        print("cameraHeight", cameraHeight)
        print("nVerticalAoiMergePosition: ", nVerticalAoiMergePosition)

        nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_POSITION, 
            nVerticalAoiMergePosition, ueye.sizeof(nVerticalAoiMergePosition))

    # # /* Read current vertical AOI merge mode */

    # nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_MODE,
    #     ueye.INT(nVerticalAoiMergeMode), ueye.sizeof(nVerticalAoiMergeMode))
    # if nRet == ueye.IS_SUCCESS:
    #     print("AOI Merge MODE")
    #     print(nVerticalAoiMergeMode)


    # /* Get the default value for the vertical AOI merge mode height */
    # INT nHeight = 0;
    # INT nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_DEFAULT, 
    #                           (void*)&nHeight, sizeof(nHeight));
    
    # /* Get current value of the vertical AOI merge mode height */
    # nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT,

    #                        (void*)&nHeight, sizeof(nHeight));

    nHeight = ueye.INT(0)
    nRet = ueye.is_DeviceFeature(hCam,ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_DEFAULT,
        nHeight, ueye.sizeof(nHeight))

    print("IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_DEFAULT: ", nHeight)

    nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT,
        nHeight, ueye.sizeof(nHeight))

    print("IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT: ", nHeight)
    
    # /* Get the number of elements in the vertical AOI merge mode height list */
    # INT nVerticalAoiMergeModeHeightNumber;
    # nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_NUMBER,

    #                       (void*)&nVerticalAoiMergeModeHeightNumber,
    #                        sizeof(nVerticalAoiMergeModeHeightNumber));

    nVerticalAoiMergeModeHeightNumber = ueye.UINT()
    nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_NUMBER,
        nVerticalAoiMergeModeHeightNumber, ueye.sizeof(nVerticalAoiMergeModeHeightNumber))

    print("nVerticalAoiMergeModeHeightNumber :", nVerticalAoiMergeModeHeightNumber)

    # if (nRet == IS_SUCCESS)
    # {
    # UINT* pVerticalAoiMergeModeHeightList = new UINT[nVerticalAoiMergeModeHeightNumber];

    if nRet == ueye.IS_SUCCESS:
        list_AOI_merge_height_list = (ueye.UINT * int(nVerticalAoiMergeModeHeightNumber))()

        # print("pVerticalAoiMergeModeHeightList", pVerticalAoiMergeModeHeightList)

    # /* Get the vertical AOI merge mode height list */pVerticalAoiMergeModeHeightList
    # nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_LIST,

    #                         (void*)pVerticalAoiMergeModeHeightList,
    #                         nVerticalAoiMergeModeHeightNumber * sizeof(UINT));

    # -------
        # nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_LIST,
        #     pVerticalAoiMergeModeHeightList, nVerticalAoiMergeModeHeightNumber * ueye.sizeof(nVerticalAoiMergeModeHeightNumber))
        
        nRet = ueye.is_PixelClock(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT_LIST, 
            list_AOI_merge_height_list, nVerticalAoiMergeModeHeightNumber*ueye.sizeof(nVerticalAoiMergeModeHeightNumber))
        print(list_AOI_merge_height_list)
        pVerticalAoiMergeModeHeightList = np.frombuffer(list_AOI_merge_height_list, int)
        print('PxCLK list:', nRet, pVerticalAoiMergeModeHeightList[0:nVerticalAoiMergeModeHeightNumber.value])

        print("pVerticalAoiMergeModeHeightList :", pVerticalAoiMergeModeHeightList)
    # ------

    # if (nRet == IS_SUCCESS)
    # {
    #   /* Set the maximum possible vertical AOI merge mode height depending on the current image height */
    #   UINT nMaxHeight = pVerticalAoiMergeModeHeightList[nVerticalAoiMergeModeHeightNumber - 1];
    #   nRet = is_DeviceFeature(hCam, IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_HEIGHT,

    #                            (void*)&nMaxHeight, sizeof(nMaxHeight));
    # }
    # }
    # if nRet = ueye.IS_SUCCESS

        # if nRet == ueye.IS_SUCCESS:
        #     print("---------------------------------------------", nMaxHeight)
        #     # nMaxHeight = ueye.UINT()
        #     print("pVerticalAoiMergeModeHeightList[]", pVerticalAoiMergeModeHeightList[0])
        #     # nMaxHeight = (pVerticalAoiMergeModeHeightList)[-1]
            
        #     nMaxHeight = ueye.UINT(1000)
        #     # nMaxHeight = ueye.UINT(2)
        #     print("nMaxHeight", nMaxHeight)
        #     nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_SET_VERTICAL_AOI_MERGE_HEIGHT,
        #         nMaxHeight, ueye.sizeof(nMaxHeight))

        #     nRet = ueye.is_DeviceFeature(hCam, ueye.IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT,
        #     nHeight, ueye.sizeof(nHeight))

        #     print("IS_DEVICE_FEATURE_CMD_GET_VERTICAL_AOI_MERGE_HEIGHT: ", nHeight)

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
def IDSSettings():
        # pass
        print("IDS Settings")

    # class:
    #     def __init__(self):
    #         def IDSPreview(self):
class IDS:
    def __init__(self, w):
        self.w = w
    def IDSPreview2(self):
        global nRet
        print(nRet)
        # self.w = w
        while(nRet == ueye.IS_SUCCESS):
            self.frame_timer = time.time()
            # In order to display the image in an OpenCV window we need to...
            # ...extract the data of our image memory
            array = ueye.get_data(pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False)

            # bytes_per_pixel = int(nBitsPerPixel / 8)

            # ...reshape it in an numpy array...
            self.frameIn = np.reshape(array,(height.value, width.value, bytes_per_pixel))
                # Check if image is not the same as previous
            # global frame
            self.frame = None
            if not np.array_equal(self.frameIn, self.frame):

                # ...resize the image by a half

                # cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)

                # cv2width = int(width)
                # cv2height = int(height/2)




                # cv2.line(frame,(0,height),(width,height),(255,255,255),5)

                self.frame = cv2.resize(self.frameIn,(0,0),fx=0.25, fy=0.25)
                
                self.frame = cv2.rotate(self.frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                
                
            #---------------------------------------------------------------------------------------------------------------------------------------
                #Include image data processing here

            #---------------------------------------------------------------------------------------------------------------------------------------
                # Print FPS
                # 
                # 
                CurrentFPS = ueye.DOUBLE()
                ueye.is_GetFramesPerSecond(hCam, CurrentFPS)
                CurrentFPS = CurrentFPS * height/2
                print("CurrentFPS: ", CurrentFPS)

                targetFPS = ueye.double(1007) # insert here which FPS you want
                actualFPS = ueye.double()
                nRet = ueye.is_SetFrameRate(hCam,targetFPS,actualFPS)
                print("is_SetFrameRate returns " + str(nRet) + ", Actual FPS is: " + str(actualFPS) + "Target FPS is: " + str(targetFPS))
                print("CurrentFPS: ", actualFPS)
                if CurrentFPS != 0:
                    global sleepTime
                    self.sleepTime = (height/2 / CurrentFPS) * 1/4
                    time.sleep(self.sleepTime)
                    print("Sleeptime", self.sleepTime)
                else:
                    self.sleepTimeNoFPS = 0.25
                    time.sleep(self.sleepTimeNoFPS)
                #time.sleep(1)
                

                # Print frame time on screen
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                # bottomLeftCornerOfText = (500,350)
                topRightCornerOfText = (0,480)
                fontScale              = 0.75
                fontColor              = (255,255,255)
                lineType               = 2
                
                cv2.putText(self.frame,"--- Total Running time --- %s seconds ---" % (time.time() - self.frame_timer), 
                # bottomLeftCornerOfText, 
                topRightCornerOfText,
                font, 
                fontScale,
                fontColor,
                lineType)

                # print("--- Total Running time --- %s seconds ---" % (time.time() - frame_timer))


                #...and finally display it

                # cv2.imshow("SimpleLive_Python_uEye_OpenCV", self.frame)
                
                # time.sleep()
                # Press q if you want to end the loop
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break
                self.image=Image.frombytes('L', (self.frame.shape[1],self.frame.shape[0]), self.frame.astype('b').tostring())
                self.imageCanvas = ImageTk.PhotoImage(self.image)
                self.w.IDSPreviewCanvas2.create_image(0,0,image=self.imageCanvas,anchor=tk.NW)
                cv2.imshow("SimpleLive_Python_uEye_OpenCV", self.frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    def IDSPreview_stop(self):
        # Releases an image memory that was allocated using is_AllocImageMem() and removes it from the driver management
        ueye.is_FreeImageMem(hCam, pcImageMemory, MemID)

        # Disables the hCam camera handle and releases the data structures and memory areas taken up by the uEye camera
        ueye.is_ExitCamera(hCam)

        # Destroys the OpenCv windows
        cv2.destroyAllWindows()

def IDSPreview():
    print("Starting IDS Camera Preview")
    # Continuous image display
    slices = list()
    
    cv2width = int(width)
    cv2height = int(height/2)

    print("created list")
    while(nRet == ueye.IS_SUCCESS):

        # In order to display the image in an OpenCV window we need to...
        # ...extract the data of our image memory
        array = ueye.get_data(pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False)

        # bytes_per_pixel = int(nBitsPerPixel / 8)

        # ...reshape it in an numpy array...
        frame = np.reshape(array,(height.value, width.value, bytes_per_pixel))

        # ...resize the image by a half


        
        
    #---------------------------------------------------------------------------------------------------------------------------------------
        #Include image data processing here
        # cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)



        # cv2.line(frame,(0,cv2height),(cv2width,cv2height),(255,255,255),5)

        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        # if frame.shape[0] == 1:
        #     print(frame.shape[1], "resized to", frame.shape[1]/2)
        #     frame = cv2.resize(frame, (int(frame.shape[1]/2), 1))
        # else:
        #     frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        

    #---------------------------------------------------------------------------------------------------------------------------------------

        
        
        
        # Create Slice of few thousand slices
        if 1000 > len(slices):
            slices.append(frame)
            # print("slice list")
            # return slices
            if 1 == len(slices):
                frame_timer = time.time()
        else:
            print(len(slices))
            print("hstack")
            print("--- Total Running time --- %s seconds ---" % (time.time() - frame_timer))
            slices_comb = np.vstack(slices)
            slices_comb = cv2.resize(slices_comb, (0, 0), fx=0.5, fy=0.5)
            slices_comb = cv2.rotate(slices_comb, cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("SimpleLive_Python_uEye_OpenCV", slices_comb)
            slices.clear()
        
        

        #...and finally display it
        # cv2.imshow("SimpleLive_Python_uEye_OpenCV", frame)

            #empty list
        # list()
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

    if nRet != ueye.IS_SUCCESS:
        print("is_CaptureVideo ERROR")

    if nRet != ueye.IS_SUCCESS:
        print("is_InquireImageMem ERROR")
    else:
        print("Press q to leave the programm")
    # Prints out some information about the camera and the sensor
    print("Camera model:\t\t", sInfo.strSensorName.decode('utf-8'))
    print("Camera serial no.:\t", cInfo.SerNo.decode('utf-8'))
    print("Maximum image width:\t", width)
    print("Maximum image height:\t", height)
    print("Current PixelClock", nPixelClock)
    print("is_SetFrameRate returns " + str(nRet) + ", Actual FPS is: " + str(actualFPS) + "Target FPS is: " + str(targetFPS))

    print()



def IDSPreview_standalone():
    # Continuous image display
    while(nRet == ueye.IS_SUCCESS):

        # In order to display the image in an OpenCV window we need to...
        # ...extract the data of our image memory
        array = ueye.get_data(pcImageMemory, width, height, nBitsPerPixel, pitch, copy=False)

        # bytes_per_pixel = int(nBitsPerPixel / 8)

        # ...reshape it in an numpy array...
        frame = np.reshape(array,(height.value, width.value, bytes_per_pixel))

        # ...resize the image by a half
    
        
    #---------------------------------------------------------------------------------------------------------------------------------------
        #Include image data processing here
        # cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)

        cv2width = int(width)
        cv2height = int(height/2)


        # cv2.line(frame,(0,cv2height),(cv2width,cv2height),(255,255,255),5)

        frame = cv2.resize(frame,(0,0),fx=0.25, fy=0.25)
        
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

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

    if nRet != ueye.IS_SUCCESS:
        print("is_CaptureVideo ERROR")

    if nRet != ueye.IS_SUCCESS:
        print("is_InquireImageMem ERROR")
    else:
        print("Press q to leave the programm")
    # Prints out some information about the camera and the sensor
    print("Camera model:\t\t", sInfo.strSensorName.decode('utf-8'))
    print("Camera serial no.:\t", cInfo.SerNo.decode('utf-8'))
    print("Maximum image width:\t", width)
    print("Maximum image height:\t", height)
    print("Current PixelClock", nPixelClock)
    print("is_SetFrameRate returns " + str(nRet) + ", Actual FPS is: " + str(actualFPS) + "Target FPS is: " + str(targetFPS))

    print()


# IDSPreview_standalone()

# IDSPreview()

print()
print("END")
