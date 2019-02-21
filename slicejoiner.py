"""
Liittää olemassaolevat viivakuvat yhteen taulukon kautta
"""
import os
from pathlib import Path
import numpy as np
from PIL import Image



linesource = Path("faces")

prefix = "pattern_"
file_pattern = prefix + '%05d' + ".png"

list_im = []

# Käy kaikki tiedostot jota on kansiossa jossa pythonia ajetaan
# Tämä python tiedosto pitää laittaa kansioon (faces)
# jossa on ainoastaan ne "halkaistut" kuvat.

for file in os.listdir(linesource):
    if file.startswith(prefix):
        print("ignoring unrelated files")
    else:
        # tekee kuvista listan
        list_im.append(file)


# käy läpi listan ja lataa kuvat
imgs = [Image.open(i) for i in list_im]


# pick the image which is the smallest, and resize the others to match it
# (can be arbitrary image shape here)
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

# save that beautiful picture
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb = imgs_comb.transpose(Image.FLIP_LEFT_RIGHT)
imgs_comb.save('Trifecta.jpg')
