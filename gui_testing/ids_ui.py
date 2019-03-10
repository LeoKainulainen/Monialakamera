import sys
import os

import time
import cv2
import numpy as np

# For Tkinter Image Display

from PIL import Image
from PIL import ImageTk

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
# from LinescanRecord import UI_IDS_functions as UI_IDS_f

from LinescanRecord.UI_IDS_functions import IDSSettings, IDSPreview, IDSPreview_standalone
from LinescanRecord.UI_IDS_functions import IDSPreview_stop

from pyueye import ueye
from IDSCapture.pyueye_camera import Camera
from IDSCapture.pyueye_utils import FrameThread, ImageBuffer, ImageData
from multiprocessing import Pipe
def IDSCapturePreview():
    max_frames = 500
    global PreviewStatus
    if PreviewStatus != True:
        # Begin IDS Video Capture and display via hstack

        # parent_conn, child_conn = Pipe()
        # cpt = 0
        # max_frames = int(input("How many pictures would you like?: "))
        # max_frames = 500

        # camera class to simplify uEye API access
        cam = Camera()
        cam.init()
        cam.set_colormode(ueye.IS_CM_BGR8_PACKED)
        cam.set_aoi(0, 0, 0, 2, "centered")

        cam.set_full_auto()

        cam.set_auto_pixelclock_framerate(420,500)

        

        cam.alloc()
        cam.capture_video()


        # a thread that waits for new images and processes all connected views
        thread = FrameThread(cam, child_conn)

        thread.start()
        # global PreviewStatus
        PreviewStatus = True
        print("Start camera",PreviewStatus)

        # keep repeating this
    elif PreviewStatus == True:
        parent_conn, child_conn = Pipe()
        cpt = 0
        slices = []
        slices.clear()
        while cpt < max_frames:
            img = parent_conn.recv()



            slices.append(img)
            
            # cv.imwrite('train_file/image%04i.jpg' %cpt, img)
            
            #print(input_q.qsize())

            time.sleep(5)
            cpt += 1
        
        
        img = np.vstack(slices)
        
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("Image", img)

        cv2.waitKey(200)
        print("image captured")
        print("Capture",PreviewStatus)

        # Set Tkinter Preview canvas

        # w.IDSPreviewCanvas2.create_image(image=img)

        # IDSCapturePreview()
        thread.stop()
        thread.join()

        cam.stop_video()
        cam.exit()

global PreviewStatus
PreviewStatus = True
IDSCapturePreview()