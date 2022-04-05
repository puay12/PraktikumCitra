import cv2
import numpy as np

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))

kernel1 = np.ones([5, 5], np.float32)/25
img_blur = cv2.filter2D(img, -1, kernel1)
kernel2a = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel2b = np.transpose(kernel2a)
kernel2 = kernel2a + kernel2b
img_edge = 0.5 * cv2.filter2D(img, -1, kernel2)
img_edge = np.uint8(img_edge)
img_sharp = cv2.add(img_blur, img_edge)

cv2.imshow("Original", img)
cv2.imshow("Sharpeness", img_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()