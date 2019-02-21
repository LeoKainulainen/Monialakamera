"""
cv2 functions
"""
import os
import time
import multiprocessing
import numpy as np
import cv2


# Parallelization & Multithreading
from joblib import Parallel, delayed

def exists(path):
    print(type(path),path)

    print(type(path),path)
    "Check if path (image) exists"
    try:
        print(path % 0)
        st = os.stat(path % 0)
    except os.error:
        return False
    print("Image roll already exists in" + path % 0)
    return True

class EmuCVFuncParallel:
    def __init__(self, test_pattern, file_pattern, series_length, series_width, width, height, path, img_dir):
        print(type(img_dir),img_dir)
        self.test_pattern = test_pattern
        self.file_pattern = file_pattern
        self.series_length = series_length
        self.series_width = series_width
        self.width = width
        self.height = height
        self.path = path
        self.img_dir = img_dir
    def create_pattern(self):
        if exists(self.path):
            return
        else:
            print(self.file_pattern)
            print("creating " + str(self.series_length) + " images with numpy roll")

            def processInput(i):
                # start_time = time.time()
                pattern = np.roll(self.test_pattern, i, axis=1)
                # print("--- roll for --- %s seconds ---" % (time.time() - start_time))

                # start_time = time.time()
                pattern = pattern[0:0+self.height, -self.series_width:self.width]
                # print("--- slicing for --- %s seconds ---" % (time.time() - start_time))

                # start_time = time.time()
                # cut = [self.width-1-i,self.width-i]
                # pattern = self.test_pattern[0:0+self.height, cut[0]:cut[1]]
                # print("--- slicing for --- %s seconds ---" % (time.time() - start_time))

                # start_time = time.time()
                # pattern = cv2.UMat(pattern)
                # print("--- imgUMat --- %s seconds ---" % (time.time() - start_time))

                # start_time = time.time()
                pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
                # print("--- color for --- %s seconds ---" % (time.time() - start_time))

                pattern = cv2.rotate(pattern, cv2.ROTATE_90_CLOCKWISE)

                start_time = time.time()
                # print(os.path.join(self.img_dir,self.file_pattern%i))
                cv2.imwrite(os.path.join(self.img_dir, self.file_pattern % i), pattern)
                # print("--- imwrite for --- %s seconds ---" % (time.time() - start_time))

        # parallellization
        inputs = range(self.series_length)
        num_cores = multiprocessing.cpu_count()
        print("Multiprocessing with: ",num_cores)
        Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)

# write in to memory??
# cv2.imwrite("pattern_%03d.png"%i, pattern)

# testing video creation in opecv
def create_video(self):
    writer = cv2.VideoWriter("o", cv2.VideoWriter_fourcc(*"MJPG"), 500, (self.width, self.height))
    for i in range(1000):
        pattern = np.roll(self.test_pattern, i, axis=1)
        pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
        writer.write(np.random.randint(0, 255, (self.width, self.height, 3)).astype('uint8'))