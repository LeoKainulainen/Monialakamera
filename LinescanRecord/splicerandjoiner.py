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
import test_utils

# cwd to if needed ..\
# os.chdir(Path('.').resolve().parents[0])
# print(os.getcwd())


appver = "v0.02"

# np.set_printoptions(threshold=sys.maxsize)


img_dir = Path("faces")
out_dir = Path("faces_out")

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

save_with_prefix = str(out_dir) + os.sep + prefix + appver + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


# luo kansiot
test_utils.folderexist(img_dir, out_dir)


img_path1 = Path("test_images") / "2-peloton-finishlynx.jpg"

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
def splice_image_ram():
    file = Path(img_dir) / file_pattern
    if test_utils.pattern_exists(str(file)):
        return
    stamp_list = []
    date = datetime.now()
    for c in range(width):
        cut = [width-1-c, width-c]
        pattern = im
        pattern = pattern[0:0+height, cut[0]:cut[1]]
        # print("cutting " + str(cut[0]) + " by " + str(cut[1]) + " section")
        # pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        # print(os.path.join(img_dir,file_pattern%c))
        # cv2.imwrite(os.path.join(img_dir, file_pattern % c), pattern)
        slices.append(pattern)

        date_combo = date + timedelta(milliseconds=c)
        time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        stamp_list.append(time_stamp)

    with open(save_with_prefix + ".txt", "w") as file1:
        file1.write(str(stamp_list))
    print("Created a list of " + str(len(stamp_list)) + " timestamps")

def join_splices_ram():
    imgs_comb_start = time.time()

    imgs_comb = np.hstack(slices)

    global imgs_comb_run_time
    imgs_comb_run_time = (time.time() - imgs_comb_start)

    imgs_comb = cv2.flip(imgs_comb, +1)
    imgs_comb = cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(save_with_prefix + ".jpg", cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR))
enumerate_run_time = None
# ##Käy läpi kuvan pikseli*sarake* kerrallaan
# Toimisko np.hsplit nopeammin? (hstack vastakohta)
def splice_image():
    file = Path(img_dir) / file_pattern
    if test_utils.pattern_exists(file):
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
        cv2.imwrite(os.path.join(img_dir, file_pattern % c), pattern)

        date_combo = date + timedelta(milliseconds=c)
        time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        stamp_list.append(time_stamp)

    with open(os.path.join(out_dir, 'time_stamps.txt'), "w") as file1:
        file1.write(str(stamp_list))
    print("Created a list of " + str(len(stamp_list)) + " timestamps")

# Videotallennuksen testaustaa jaaaaaaaa.... ei toimi. MJPG vähimmäisleveys ~~ 4px

def splice_image_to_video():
    # stamp_list = []
    writer = cv2.VideoWriter(save_with_prefix + ".avi", cv2.VideoWriter_fourcc(*"MJPG"), 5, (100, height), True)
    for i in range(1, 40):
        # print(i)
        cut = [4000-100*i, 4100-100*i]
        print(cut[0], cut[1])
        pattern = im
        pattern = pattern[0:0+height, cut[0]:cut[1]]
        pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        # print(pattern%i)
        writer.write(pattern%i)
    writer.release()

        # date_combo = date + timedelta(milliseconds=i)
        # time_stamp = date_combo.strftime('%H:%M:%S.%f')[:-2]
        # stamp_list.append(time_stamp)

    # with open(os.path.join(out_dir, 'time_stamps.txt'), "w") as file1:
    #     file1.write(str(stamp_list))
    # print("Created a list of " + str(len(stamp_list)) + " timestamps")


def join_splices():
    list_im = []
    start_time_join = time.time()
    # faster without enumerate?
    for file, f in zip(os.listdir(img_dir), range(width)):
        if file.startswith(file_pattern%f):
            list_im.append(file)

    # for f, file in enumerate(os.listdir(img_dir)):
    #     if file.startswith(file_pattern%f):
    #         # print(f,file)
    #         # print(file)
    #         list_im.append(file)
    global enumerate_run_time
    enumerate_run_time = time.time() - start_time_join
    # print(list_im)
    # time.sleep(5)
    # raise SystemExit(0)
    # for file in os.listdir(img_dir):
    #     if file.startswith(prefix):
    #         print(file)
    #         list_im.append(file)
    # print(list_im)
    # imgs = [Image.open(os.path.join(img_dir, i)) for i in list_im]
    imgs = []
    for i in list_im:
        img = cv2.imread(os.path.join(img_dir, i))
        imgs.append(img)
    # imgs = [cv2.imread(os.path.join(img_dir, i)) for i in list_im]
    print("Type of variable", imgs[0], " is ", type(imgs[0]))

    # pick the image which is the smallest, and resize the others to match it
    # (can be arbitrary image shape here)
    # min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    # print(min_shape)
    imgs_comb_start = time.time()

    # avoiding this here: https://github.com/numpy/numpy/blob/master/numpy/core/shape_base.py#L209
    # imgs_comb = np.hstack(tuple(map(tuple, (np.asarray(i.resize(min_shape)) for i in imgs))))
    # imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
    # imgs_comb = np.hstack((i.resize(min_shape)) for i in imgs)
    imgs_comb = np.hstack(imgs)
    # imgs_comb = np.hstack(tuple(map(tuple, (i for i in imgs))))
    global imgs_comb_run_time
    imgs_comb_run_time = (time.time() - imgs_comb_start)

    #tuple to array..
    # print(type(imgs_comb), imgs_comb[0])
    # imgs_comb = np.asarray(imgs_comb)
    # imgs_Comb = cv2.UMat(imgs_comb)
    imgs_comb = cv2.flip(imgs_comb, +1)
    cv2.imwrite(save_with_prefix + ".jpg", cv2.cvtColor(imgs_comb, cv2.COLOR_RGB2BGR))
    # imgs_comb = Image.fromarray(imgs_comb)
    # imgs_comb = imgs_comb.transpose(Image.FLIP_LEFT_RIGHT)

    # imgs_comb.save(save_with_prefix + ".jpg")
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
