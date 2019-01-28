import cv2
import numpy as np
import math

img = cv2.imread('test_images\\2-dark.jpg',cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img,(0,0),fx=0.25, fy=0.25)

img = cv2.convertScaleAbs(img, alpha=10, beta=10)
cv2.imshow("img",img)

img = cv2.bitwise_not(img)



th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,-2)
cv2.imshow("th2", th2)
# cv2.imwrite("th2.jpg", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

horizontal = th2
vertical = th2
rows,cols = horizontal.shape

#inverse the image, so that lines are black for masking
horizontal_inv = cv2.bitwise_not(horizontal)
#perform bitwise_and to mask the lines with provided mask
masked_img = cv2.bitwise_and(img, img, mask=horizontal_inv)
#reverse the image back to normal
masked_img_inv = cv2.bitwise_not(masked_img)
cv2.imshow("masked img", masked_img_inv)
# cv2.imwrite("result2.jpg", masked_img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

horizontalsize = int(cols / 30)
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,1))
horizontal = cv2.erode(horizontal, horizontalStructure, (-1, -1))
horizontal = cv2.dilate(horizontal, horizontalStructure, (-1, -1))


cv2.imshow("horizontal", horizontal)
# cv2.imwrite("horizontal.jpg", horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()