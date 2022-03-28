import cv2
import numpy as np

img = cv2.imread('sometin.jpg',0)
img = cv2.resize(img, (700, 500))

# gamma = 10
img1 = 1 * np.exp(img, 10)
img1 = np.uint8(img1)
# gamma = 8
img2 = 1 * np.exp(img, 8)
img2 = np.uint8(img1)
# gamma = 6
img3 = 1 * np.exp(img, 6)
img3 = np.uint8(img1)

cv2.imshow("Original Image", img)
cv2.imshow("Gamma = 10", img1)
cv2.imshow("Gamma = 8", img2)
cv2.imshow("Gamma = 6", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()