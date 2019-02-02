from PIL import Image
import numpy as np
import cv2
#from PIL.ExifTags import TAGS

#from datetime import datetime

from pathlib import Path



def splice_image ():
    path1 = Path("test_images") / str("1-peloton-finishlynx-shorter.png")
    ###avaa kuvan 
    im = Image.open(path1)
    im = cv2.cvtColor(cv2.UMat(imgUMat), cv2.COLOR_BGR2GRAY)
    ###tekee sen bittikartasta numpy arraylistan
    data = np.array(im)


    pathcounter = 1 
    ###Käy läpi kuvan pikselirivi kerrallaan
    for row in data:

           ###HUOM TALLENTAA TIETOKONEELLE NIIN MOINTA KUVAA KUIN PIKSELIRIVEJÄ ON KUVASSA!!!
           imgfrom = Image.fromarray(row.astype('uint8'))
           path = "faces/"+"faces %s" % pathcounter +".jpg"
           imgfrom.save(path)
           pathcounter = pathcounter + 1

###Tämä jatkuu myöhemmin
#def give_timestamps ():

    
    




splice_image()











