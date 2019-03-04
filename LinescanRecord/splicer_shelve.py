from pathlib import Path
import sys
import os
from datetime import datetime, timedelta
import time
import numpy as np
import cv2
# make importing modules possible from parent directory...
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import codereuse
import shelve

appver = "v0.02_shelve"

img_dir = Path("faces")
out_dir = Path("faces_out")
db_dir = out_dir / "db"

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

# esim pattern_v0.01ram_2019_03_03_23_15_46
save_with_prefix = str(out_dir) + os.sep + prefix + appver + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
save_shelve_name = str(db_dir) + os.sep + prefix + appver

# luo kansiot
codereuse.folderexist(img_dir, out_dir, db_dir)


img_path1 = Path("test_images") / "2-peloton-finishlynx.jpg"

print(img_path1)

# OpenCV takes only string paths..
im = cv2.imread(str(img_path1))

data = im

# Check image height
height = int(im.shape[0])
# Check image width
width = int(im.shape[1])

print(im.shape)

def splice_image_shelve():
    slices = list()
    file = Path(img_dir) / file_pattern
    if codereuse.pattern_exists(str(file)):
        return
    stamp_list = []
    db_shelve = shelve.open(save_shelve_name)
    for c in range(width):
        cut = [width-1-c, width-c]
        pattern = im
        pattern = pattern[0:0+height, cut[0]:cut[1]]
        # print("cutting " + str(cut[0]) + " by " + str(cut[1]) + " section")
        

        slices.append(pattern)


        date_combo = date + timedelta(milliseconds=c)
        time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        stamp_list.append(time_stamp)
        # Shelve pattern & slices & timestamps

        # takes way too long...
        # db_shelve[time_stamp] = pattern
        # db_shelve[time_stamp]

    with open(save_with_prefix + ".txt", "w") as file1:
        file1.write(str(stamp_list))
    print("Created a list of " + str(len(stamp_list)) + " timestamps")
    # print(slices)
    db_shelve["timestamps"] = stamp_list
    db_shelve["slices"] = slices
    db_shelve.close()

def join_splices_from_shelve(percent_start, percent_stop):
    # imgs_comb_start = time.time()

    db_shelve = shelve.open(save_shelve_name, flag='r')
    # slices = db_shelve[]

    slices = db_shelve["slices"]

    # print(type(composite))

    composite = np.hstack(slices)
    composite = cv2.flip(composite, +1)

    imgs_comb = np.hstack(slices)
    imgs_comb = cv2.flip(imgs_comb, +1)

    print(int(percent_start/100*len(slices)))
    print(int(percent_stop/100*len(slices)))

    slices_defined_area = slices[int(percent_start/100*len(slices)):int(percent_stop/100*len(slices))]

    imgs_comb_def_area = np.hstack(slices_defined_area)
    imgs_comb_def_area = cv2.flip(imgs_comb_def_area, +1)

    # itertools https://stackoverflow.com/a/8671323/5776626
    # import itertools
    # for line in itertools.islice(list , start, stop):
    #     foo(line)

    


    
    # imgs_comb = cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_with_prefix + ".jpg", imgs_comb)

    # composite = cv2.cvtColor(composite, cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_with_prefix + "_composite.jpg", composite)

    # save timestamps as text_file
    stamp_list = db_shelve["timestamps"]

    with open(save_with_prefix + ".txt", "w") as file1:
        file1.write(str(stamp_list))
    print("Created a list of " + str(len(stamp_list)) + " timestamps")

    return imgs_comb_def_area

app_start_time = time.time()

date = datetime.now()
# splice_image_shelve()
# join_splices_from_shelve()
print(type(slice))

print("--- Total Running time --- %s seconds ---" % (time.time() - app_start_time))