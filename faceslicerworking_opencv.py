from PIL import Image
import numpy as np
import cv2
#from PIL.ExifTags import TAGS

#from datetime import datetime
import os
from pathlib import Path



img_dir = "faces"
file_pattern = "pattern_" + '%05d' + ".png"
#luo kansion
if not os.path.exists(img_dir):
   os.makedirs(img_dir)

img_path1 = Path("test_images") / "1-peloton-finishlynx-shorter.png"

print(img_path1)

im = np.array(Image.open(img_path1))
# im = np.array(Image.open(path1).convert('LA'))
data = im


data2 = im[:,:,1]

# Check image height
height = int(im.shape[0])
print(height)
# Check image width
width = int(im.shape[1])

print(im.shape)

print(width)


def splice_image ():
    ###Käy läpi kuvan pikseli*sarake* kerrallaan
    for c in range(width):
            cut = [width-1-c,width-c]
            pattern = im
            pattern = pattern[0:0+height, cut[0]:cut[1]]
            print("cutting " + str(cut[0]) + " by " + str(cut[1]) + " section")
            pattern = cv2.cvtColor(pattern, cv2.COLOR_RGB2BGR)
            print(os.path.join(img_dir,file_pattern%c))
            cv2.imwrite(os.path.join(img_dir,file_pattern%c), pattern)


def give_timestamps ():
    #pass = ohita koko funktio
    pass


splice_image()











