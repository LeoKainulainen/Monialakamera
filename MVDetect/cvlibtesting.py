"""
Testing CVlib
"""
import os
import sys
import cvlib as cv
import cv2
from cvlib.object_detection import draw_bbox

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from LinescanRecord import splicer_shelve

list_im = []
for file in os.listdir("."):
    if file.startswith("slice"):
        print("ignoring unrelated files")
    else:
        # tekee kuvista listan
        list_im.append(file)

# shelve open db
img = splicer_shelve.join_splices_from_shelve(30, 50)
# join_splices_from_shelve()

bbox, label, conf = cv.detect_common_objects(img)

output_image = draw_bbox(img, bbox, label, conf)

cv2.imwrite(splicer_shelve.save_with_prefix + "cvlib" + ".jpg", output_image)
