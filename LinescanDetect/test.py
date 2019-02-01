import cv2
import numpy as np
import math
import ctypes






#kuvan skaalaus näytön kokoon

#näytön resoluutio
user32 = ctypes.windll.user32
#windows only screen res
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)
screenwidth = screensize[0]
print (screenwidth)

def resize_keep_aspect(resize_image):
    print("resizing")
    TARGET_PIXEL_AREA = 100000.0

    ratio = float(resize_image.shape[0]) / float(resize_image.shape[1])
    new_w = screenwidth - 20
    new_h = int((new_w * ratio) + 0.5)
    resize_image = cv2.resize(resize_image, (new_w,new_h))
    # cv2.imshow('image', resize_image)
    return resize_image

##Opencv lukee kuvan ja muuntaa sen grayscaleksi
# img = cv2.imread('..\\test_images\\2-dark.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('..\\test_images\\2-light.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('..\\test_images\\1-dark.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('..\\test_images\\1-light.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('test_images\\1-peloton-finishlynx.jpg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('..\\test_images\\2-peloton-finishlynx.jpg',cv2.IMREAD_GRAYSCALE)

origimg = img

origimg = resize_keep_aspect(origimg)

# kuvan käsittelyä (morphology:opening)
kernel = np.ones((25,25),np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

##Muuntaa kontrastia, että kuviot olisivat vain yhtä väriä (mustaa)
# _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

# img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)


#
# img = cv2.convertScaleAbs(img, alpha=12, beta=12)

# img = cv2.blur(img,(15,15))



th2 = img

_, threshold = cv2.threshold(th2, 240, 255, cv2.THRESH_BINARY)


##Etsii kuvioiden ääriviivat 
contours,hierachy=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_COMPLEX
triangle = 0
rectangle = 0
pentagon = 0
ellipse = 0
circle = 0

##Käy läpi ääriviivat
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength (cnt, True), True)
    cv2.drawContours(img, [approx], 0,(0), 4)
    

    ##Ottaa kaksi pisteen kuvioista (ensimmäiset x ja y -koordinaatit)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    ##käy läpi ääriviivat, kirjoittaa kuvioiden nimet ja asettaa tekstin
    # if len(approx) == 3:
    #     cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    #     triangle = triangle + 1
        #print(approx.ravel())
    # elif len(approx) == 4:
    #     cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    #     rectangle = rectangle + 1
        
    # elif len(approx) == 5:
    #     cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
    #     pentagon = pentagon + 1

    if 6 < len(approx) < 15:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
        ellipse = ellipse + 1
        
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))
        circle = circle + 1

    
##Näyttää greyscale kuvan johon on piirretty ääriviivat ja kirjoitettu kuvioiden nimet  


th2 = resize_keep_aspect(th2)
cv2.imshow('origimg', origimg)
cv2.imshow("th2", th2)
# cv2.imwrite("th2.jpg", th2)
# cv2.waitKey(0)

img = resize_keep_aspect(img)
cv2.imshow('image', img)
# print("The number of shapes is " + str(triangle + rectangle + pentagon + ellipse + circle))

#cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()