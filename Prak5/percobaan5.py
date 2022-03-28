import cv2
import numpy as np

img = cv2.imread('sundae.jpg',0)
img = cv2.resize(img, (700,500))

img1 = 40 * np.log(0.5 * img)
img1 = np.uint8(img1)
img2 = 40. * np.log(2. * img)
img2 = np.uint8(img2)

cv2.imshow("Original Image", img)
cv2.imshow("a=40 b= 0.5", img1)
cv2.imshow("a=40 b= 2.0", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()