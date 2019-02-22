"""
splice and join an already made finish line photo
"""
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta
import time
import numpy as np
import cv2
from PIL import Image

# cwd to if needed ..\
# os.chdir(Path('.').resolve().parents[0])
# print(os.getcwd())


appver = "v0.01"

# np.set_printoptions(threshold=sys.maxsize)


img_dir = Path("faces")
out_dir = Path("faces_out")

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

save_with_prefix = str(out_dir) + os.sep + prefix + appver + "_" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S")


# luo kansiot
def folderexist(*args, **kwargs):
    for fname in args:
        if not os.path.exists(fname):
            os.makedirs(fname)

folderexist(img_dir, out_dir)


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

print("Image width: ",width)
def exists(path):
    print(type(path), path)
    path = str(path)
    print(type(path), path)
    "Check if path (image) exists"
    try:
        print(path % 0)
        st = os.stat(path % 0)
    except os.error:
        return False
    print("Image roll already exists in" + path % 0)
    return True

# ##Käy läpi kuvan pikseli*sarake* kerrallaan
def splice_image():
    file = Path(img_dir) / file_pattern
    if exists(file):
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
    stamp_list = []
    date = datetime.now()
    writer = cv2.VideoWriter(save_with_prefix + ".avi", cv2.VideoWriter_fourcc(*"MJPG"), 5, (100, height),True)
    for i in range(1,40):
        # print(i)
        cut = [4000-100*i,4100-100*i]
        print(cut[0],cut[1])
        pattern = im
        pattern = pattern[0:0+height, cut[0]:cut[1]]
        pattern = cv2.cvtColor(pattern%i, cv2.COLOR_RGB2BGR)
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
    start_time = time.time()
    # faster without enumerate?
    for file, f in zip(os.listdir(img_dir), range(width)):
        if file.startswith(file_pattern%f):
            list_im.append(file)
    
    # for f, file in enumerate(os.listdir(img_dir)):
    #     if file.startswith(file_pattern%f):
    #         # print(f,file)
    #         # print(file)
    #         list_im.append(file)
    print("--- enumerating for --- %s seconds ---" % (time.time() - start_time))
    # print(list_im)
    # time.sleep(5)
    # raise SystemExit(0)
    # for file in os.listdir(img_dir):
    #     if file.startswith(prefix):
    #         print(file)
    #         list_im.append(file)

    imgs = [Image.open(os.path.join(img_dir, i)) for i in list_im]


    # pick the image which is the smallest, and resize the others to match it
    # (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb_start = time.time()
    imgs_comb = np.hstack(tuple(map(tuple, (np.asarray(i.resize(min_shape)) for i in imgs))))
    print("--- hstack() Running time --- %s seconds ---" % (time.time() - imgs_comb_start))

    #tuple to array..
    print(type(imgs_comb))
    imgs_comb = np.asarray(imgs_comb)
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb = imgs_comb.transpose(Image.FLIP_LEFT_RIGHT)
    imgs_comb.save(save_with_prefix + ".jpg")
app_start_time = time.time()

start_time = time.time()
splice_image()
# splice_image_to_video()
print("--- splice_image() Running time --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
join_splices()


print("--- join_splices Running time --- %s seconds ---" % (time.time() - start_time))

print("--- Total Running time --- %s seconds ---" % (time.time() - app_start_time))
