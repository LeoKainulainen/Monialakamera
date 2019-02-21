"""
Testing CVlib
"""
import os
import cvlib as cv
from cvlib.object_detection import draw_bbox

list_im = []
for file in os.listdir("."):
    if file.startswith("slice"):
        print("ignoring unrelated files")
    else:
        # tekee kuvista listan
        list_im.append(file)


# käy läpi listan ja lataa kuvat
imgs = [Image.open(i) for i in list_im]

bbox, label, conf = cv.detect_common_objects(img)

output_image = draw_bbox(img, bbox, label, conf)
