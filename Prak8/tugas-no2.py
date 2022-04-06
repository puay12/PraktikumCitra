import numpy as np
import cv2

img = cv2.imread('flower.jpg', 0)
img = cv2.resize(img, (400, 600))
kernel = np.ones((7, 7), np.float32) / 49
dst_blur = cv2.filter2D(img, -1, kernel)

kernel_v = np.array([[0, -0.5 , 0], [-0.5, 0, 0.5], [0, 0.5, 0]])
kernel_h = np.array([[0, -0.5 , 0], [-0.5, 1, 0.5], [0, 0.5, 0]])
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst_edge = cv2.add(dst_v, dst_h)

img2 = cv2.add(img, dst_edge)
img_inverse = 255 - dst_edge

cv2.imshow("Original", img)
cv2.imshow("Filtered Blur", dst_blur)
cv2.imshow("Filtered Edge", dst_edge)
cv2.imshow("Filtered Sharpeness", img2)
cv2.imshow("Filtered Sketsa", img_inverse)
cv2.waitKey(0)
cv2.destroyAllWindows()