"""
splice and join an already made finish line photo
"""
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
# from PIL import Image
import codereuse


appver = "v0.01ram"


img_dir = Path("faces")
out_dir = Path("faces_out")

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

save_with_prefix = str(out_dir) + os.sep + prefix + appver + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


# luo kansiot
codereuse.folderexist(img_dir, out_dir)


img_path1 = Path("test_images") / "1-light.jpg"

print(img_path1)

# OpenCV takes only string paths..
im = cv2.imread(str(img_path1))
# im = np.array(Image.open(path1).convert('LA'))
data = im


data2 = im[:, :, 1]

# Check image height
height = int(im.shape[0])
print(height)
# Check image width
width = int(im.shape[1])

print(im.shape)

print("Image width: ", width)
def exists(path):
    print(type(path), path)
    path = str(path)
    print(type(path), path)
    # "Check if path (image) exists"
    try:
        print(path % 0)
        os.stat(path % 0)
    except os.error:
        return False
    print("Image roll already exists in" + path % 0)
    return True

# ##Käy läpi kuvan pikseli*sarake* kerrallaan
# Toimisko np.hsplit nopeammin? (hstack vastakohta)
def splice_image_ram():
    file = Path(img_dir) / file_pattern
    if codereuse.pattern_exists(str(file)):
        return
    stamp_list = []
    date = datetime.now()
    for c in range(width):
        cut = [width-1-c, width-c]
        pattern = im
        pattern = pattern[0:0+height, cut[0]:cut[1]]
        # print("cutting " + str(cut[0]) + " by " + str(cut[1]) + " section")
        pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        # print(os.path.join(img_dir,file_pattern%c))
        # cv2.imwrite(os.path.join(img_dir, file_pattern % c), pattern)
        slices.append(pattern)

        date_combo = date + timedelta(milliseconds=c)
        time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        stamp_list.append(time_stamp)

    with open(os.path.join(out_dir, 'time_stamps.txt'), "w") as file1:
        file1.write(str(stamp_list))
    print("Created a list of " + str(len(stamp_list)) + " timestamps")

def join_splices_ram():
    imgs_comb_start = time.time()

    imgs_comb = np.hstack(slices)

    global imgs_comb_run_time
    imgs_comb_run_time = (time.time() - imgs_comb_start)

    imgs_comb = cv2.flip(imgs_comb, +1)
    cv2.imwrite(save_with_prefix + ".jpg", cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR))
enumerate_run_time = None
def join_splices():
    list_im = []
    start_time_join = time.time()
    # faster without enumerate?
    for file, f in zip(os.listdir(img_dir), range(width)):
        if file.startswith(file_pattern%f):
            list_im.append(file)

    enumerate_run_time = time.time() - start_time_join

    imgs = []
    for i in list_im:
        img = cv2.imread(os.path.join(img_dir, i))
        imgs.append(img)
    # imgs = [cv2.imread(os.path.join(img_dir, i)) for i in list_im]
    print("Type of variable", imgs[0], " is ", type(imgs[0]))

    imgs_comb_start = time.time()

    # avoiding this here: https://github.com/numpy/numpy/blob/master/numpy/core/shape_base.py#L209
    # imgs_comb = np.hstack(tuple(map(tuple, (np.asarray(i.resize(min_shape)) for i in imgs))))
    imgs_comb = np.hstack(imgs)
    # imgs_comb = np.hstack(tuple(map(tuple, (i for i in imgs))))
    global imgs_comb_run_time
    imgs_comb_run_time = (time.time() - imgs_comb_start)

    imgs_comb = cv2.flip(imgs_comb, +1)
    cv2.imwrite(save_with_prefix + ".jpg", cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR))

app_start_time = time.time()

start_time = time.time()
slices = list()
splice_image_ram()
# splice_image_to_video()
splice_image_run_time = (time.time() - start_time)

start_time = time.time()
join_splices_ram()

print("--- splice_image() Running time --- %s seconds ---" % splice_image_run_time)

print("--- enumerating for --- %s seconds ---" % enumerate_run_time)

print("--- hstack() Running time --- %s seconds ---" % imgs_comb_run_time)

print("--- join_splices Running time --- %s seconds ---" % (time.time() - start_time))

print("--- Total Running time --- %s seconds ---" % (time.time() - app_start_time))
