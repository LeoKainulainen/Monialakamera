from PIL import Image
import numpy as np
import cv2
#from PIL.ExifTags import TAGS

#from datetime import datetime

from pathlib import Path

import os

path1 = Path("test_images") / "1-peloton-finishlynx-shorter.png"

dir = "faces"

#luo kansion
if not os.path.exists(dir):
   os.makedirs(dir)

def splice_image ():
    ###avaa kuvan 
    im = Image.open(path1)
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ###tekee sen bittikartasta numpy arraylistan
    data = np.array(im)
    data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)


    pathcounter = 1 
    ###Käy läpi kuvan pikselirivi kerrallaan

    ##Transpose, eli sarakkeet riveiksi
    data = data.reshape((-1, 1)) 

    for row in data:

           ###HUOM TALLENTAA TIETOKONEELLE NIIN MOINTA KUVAA KUIN PIKSELIRIVEJÄ ON KUVASSA!!!
           imgfrom = Image.fromarray(row.astype('uint8'))
           path = "faces/"+"faces %s" % pathcounter +".jpg"
           imgfrom.save(path)
           pathcounter = pathcounter + 1

def give_timestamps ():
    #pass = ohita koko funktio
    pass



splice_image()
