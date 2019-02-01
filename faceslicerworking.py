from PIL import Image
import numpy as np
from PIL.ExifTags import TAGS

from datetime import datetime


def splice_image ():
    ###avaa kuvan 
    im = Image.open("face.png")
    ###tekee sen bittikartasta numpy arraylistan
    data = np.array(im)


    pathcounter = 1 
    ###Käy läpi kuvan pikselirivi kerrallaan
    for row in data:

           ###Tallentaa jokaisen rivin erikseen
           imgfrom = Image.fromarray(row.astype('uint8'))
           path = "faces/"+"faces %s" % pathcounter +".jpg"
           imgfrom.save(path)
           pathcounter = pathcounter + 1

###Tämä jatkuu myöhemmin
#def give_timestamps ():

    
    




splice_image()











