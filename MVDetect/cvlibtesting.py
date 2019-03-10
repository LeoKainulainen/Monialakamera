"""
Testing CVlib
"""
import os
import sys
import time
import numpy as np
import cvlib as cv
import cv2
import PIL
from cvlib.object_detection import draw_bbox
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from LinescanRecord import splicer_shelve

app_start_time = time.time()

# shelve open db takes percentage of input image as arguments ("start of image", "end of image")

# splice image function from splicer_shelve.py
# splicer_shelve.splice_image_shelve()

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

    
    if finish_direction == "toright":
        
        first_points = list(np.array(bbox)[:, 2])
        combined_list = list(zip(label, first_points))
        combined_list = sorted(combined_list, key=lambda x: int(x[1]), reverse=True)
        print("detected objects arranged left to right", combined_list, "\n")
    elif finish_direction == "toleft":
        
        first_points = list(np.array(bbox)[:, 2])
        combined_list = list(zip(label, first_points))
        combined_list = sorted(combined_list, key=lambda x: int(x[1]))
        print("detected objects arranged right to left", combined_list, "\n")

    # write detected boxes to list
    
    print(type(bbox), bbox, "\n")
    print(type(label), label, "\n")
    print(type(conf), conf)

    imgs = []

    
    first_points = sorted(first_points)
    
    print("coordinates" + str(first_points))
    
    print("coord29")
    for i in range(len(first_points)):
        spliced_img = img[0:height, first_points[i]-500:first_points[i]+150]
        cv2.imwrite("test" + str(i) +".jpg", spliced_img)
        imgs.append(spliced_img)
        

        
    
    return combined_list

mv_identify_participants(0, 100)

print("--- Total Running time --- %s seconds ---" % (time.time() - app_start_time))
