from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
from pathlib import Path
import os
from PIL import Image
import glob

path1 = Path("test_images") / "1-light-cyclist.png"
path2  = Path("test_images") / "empty.png"
path3 = Path("test_images") / "1-light-altered.png"
#img = cv2.imread(str(path1), cv2.COLOR_BGR2GRAY)
test_img = cv2.imread(str(path2), cv2.COLOR_BGR2GRAY)
#altered_img = cv2.imread(str(path3), cv2.COLOR_BGR2GRAY)
long_img = Image.open(path3)
empty_img = Image.open(path2)
savedir = 'diff_testing'

width, height = long_img.size



#cv2.imshow('image', img)
#cv2.imshow('test', test_img)




#print(img)
#print(test_image)

def loop_image():
    width, height = long_img.size
    cropped_image_size = w, h = (1000, long_img.size[1])
    frame_num = 1
    for col_i in range(0, width, w):
        for row_i in range(0, height, h):
            crop = long_img.crop((col_i, row_i, col_i + w, row_i + h))
            save_to= os.path.join(savedir, "cropped_{:03}.png")
            crop.save(save_to.format(frame_num))
            frame_num += 1
            

def calculate_diff(images):
        
        i = 0
        for files in images:
           (score, diff) = compare_ssim(images[i], test_img, full=True, multichannel=True)
           diff = (diff * 255).astype("uint8")
           print(i)
           print("SSIM: {}".format(score))
           print("-----")
           i = i+1

def prequisities():
    
    if len(os.listdir(savedir) ) == 0:
        loop_image()
    else:
        images = [cv2.imread(file) for file in glob.glob("diff_testing/*.png")]
        
        calculate_diff(images)
        


prequisities()
