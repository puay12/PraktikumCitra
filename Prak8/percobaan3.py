import cv2
import numpy as np

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))
noise = np.random.randn(*img.shape) * 10
img_noise = np.abs(img + noise)
img_noise = np.uint8(img_noise)

cv2.imshow("Original", img)
cv2.imshow("Image Noise", img_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()