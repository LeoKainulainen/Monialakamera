"""
Testing CVlib
"""
from pathlib import Path
import os
import sys
from datetime import datetime, timedelta
import time
import numpy as np

import cvlib as cv
import cv2
from PIL import Image
from cvlib.object_detection import draw_bbox
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from LinescanRecord import splicer_shelve

import test_utils

app_start_time = time.time()

# shelve open db takes percentage of input image as arguments ("start of image", "end of image")

# splice image function from splicer_shelve.py
# splicer_shelve.splice_image_shelve()

appver = "v0.02_cvlib"

img_dir = Path("splicer")
out_dir = Path("splicer_out")
db_dir = out_dir / "db"

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

# esim pattern_v0.01ram_2019_03_03_23_15_46
save_with_prefix = str(out_dir) + os.sep + prefix + appver + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
# save_shelve_name = str(db_dir) + os.sep + prefix + appver

def mv_identify_participants(scan_area_start, scan_area_stop):
    """takes arguments scan_area_start, scan_area_stop, which are parts of picture as 0-100 (%)
    currently because of splicer_shelve.splice_image(), arguments need to be inverted 
    e.g. 0-20 equals 80-100
    
    """

    img = splicer_shelve.join_splices_from_shelve(scan_area_start, scan_area_stop)
    height, width, channels = img.shape 
    # join_splices_from_shelve()

    bbox, label, conf = cv.detect_common_objects(img)

    output_image = draw_bbox(img, bbox, label, conf)

    cv2.imwrite(splicer_shelve.save_with_prefix + "cvlib" + ".jpg", output_image)
    #path = 'faces_out'
    #cv2.imwrite(os.path.join(path ,  "cvlib" + ".jpg"), output_image)

    # output, bbox = boxes.append([x, y, w, h]) // cvlib
    # furthest x coordinate finish line finishing left to right = x + w
    # (marks first point of contact with finish line or camera)
    # furthest x coordinate finish line finishing right to left = x
    # (marks first point of contact with finish line or camera)
    # ^^ above is how darknet should work, but cvlib is actually x,y
    # (upper left coordinate) + x,y (lower right coordinate)...
    # e.g. finishing from left to right, first over camera = bbox[*][3]
    # finishing right to left, first over camera = bbox[*][0]

    # make list with objects ordered from either left to right or right to left

    finish_direction = "toright"
    #print("boxes" + str(bbox[0]))
    #print((list(np.array(bbox)[:, 0])))
    
    if finish_direction == "toright":
        
        first_points = list(np.array(bbox)[:, 2])
        second_points = list(np.array(bbox)[:, 0])
        combined_list = list(zip(label, first_points))
        combined_list = sorted(combined_list, key=lambda x: int(x[1]), reverse=True)
        print("detected objects arranged left to right", combined_list, "\n")
    elif finish_direction == "toleft":
        
        first_points = list(np.array(bbox)[:, 2])
        combined_list = list(zip(label, first_points))
        combined_list = sorted(combined_list, key=lambda x: int(x[1]))
        print("detected objects arranged right to left", combined_list, "\n")

    # write detected boxes to list
    
   #print(type(bbox), bbox, "\n")
   # print(type(label), label, "\n")
    #print(type(conf), conf)

    # luo kansiot
    test_utils.folderexist(img_dir, out_dir, db_dir)
    filesave = Path(img_dir) / file_pattern

    imgs = []

    
    first_points = sorted(first_points)
    second_points = sorted(second_points)
    print("coordinates1 " + str(first_points[0]))
    print("coordinates2 " + str(second_points[0]))
    
    list_im = []
    for i in range(len(first_points)):
        spliced_img = img[0:height, second_points[i]:first_points[i]]
        cv2.imwrite(str(filesave)%i, spliced_img)
        list_im.append(str(filesave)%i)
        imgs.append(spliced_img)
        
    imgs_comb = np.hstack(imgs)
    # imgs_comb = Image.fromarray(imgs[0])
    # imgs    = [ Image.open(i) for i in list_im ]
    # min_shape = sorted( [(np.sum(b.size), b.size ) for b in imgs])[0][1]
    # imgs_comb = np.hstack( (np.asarray( b.resize(min_shape) ) for b in imgs ) )
   
    imgs_comb = Image.fromarray(imgs_comb)

    imgs_comb.save(save_with_prefix + ".jpg")  
    
    return combined_list

mv_identify_participants(80, 100)

print("--- Total Running time --- %s seconds ---" % (time.time() - app_start_time))
