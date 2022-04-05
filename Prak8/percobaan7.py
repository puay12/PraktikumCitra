import cv2
import numpy as np

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))

kernel = np.array([[1, 2,  1], [2, -12, 2], [1, 2, 1]])
dst = cv2.filter2D(img, -1, kernel)
sketsa = 255 - dst

cv2.imshow("Original", img)
cv2.imshow("Sketsa", sketsa)
cv2.waitKey(0)
cv2.destroyAllWindows()