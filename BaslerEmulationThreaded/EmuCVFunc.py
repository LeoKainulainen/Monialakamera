import numpy as np
import cv2
import os

class EmuCVFunc:
    def __init__(self, test_pattern, file_pattern, series_length, series_width, width, height, path, img_dir):
        self.test_pattern = test_pattern
        self.file_pattern = file_pattern
        self.series_length = series_length
        self.series_width = series_width
        self.width = width
        self.height = height
        self.path = path
        self.img_dir = img_dir
    def create_pattern(self):
        def exists(path):
            "Check if path (image) exists"
            try:
                print(path%0)
                st = os.stat(path%0)
            except os.error:
                return False
            print("Image roll already exists in" + path%0)
            return True
        if exists(self.path):
            return
        else:
            print(self.file_pattern)
            print("creating " + str(self.series_length) +  " images with numpy roll")
            for i in range(self.series_length):
                pattern = np.roll(self.test_pattern,i,axis=1)
                pattern = pattern[0:0+self.height, -self.series_width:self.width]
                pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
                pattern = cv2.rotate(pattern, cv2.ROTATE_90_CLOCKWISE)
                print(os.path.join(self.img_dir,self.file_pattern%i))
                cv2.imwrite(os.path.join(self.img_dir,self.file_pattern%i), pattern)
                
                # write in to memory??
                # cv2.imwrite("pattern_%03d.png"%i, pattern)

    # testing video creation in opecv
    def create_video(self):
        writer = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*"MJPG"), 500,(width,height))
        for i in range(1000):
            self.pattern = np.roll(test_pattern,i,axis=1)
            self.pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
            writer.write(np.random.randint(0, 255, (width,height,3)).astype('uint8'))
            