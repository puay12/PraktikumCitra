import cv2
import numpy as np

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))

noise = np.random.randn(*img.shape) * 10
img_noise = np.abs(img + noise)
img_noise = np.uint8(img_noise)

dst_gauss = cv2.GaussianBlur(img_noise, [7, 7], 0)
dst_med = cv2.medianBlur(img_noise, 7)

cv2.imshow("Image Noise", img_noise)
cv2.imshow("Gaussian", dst_gauss)
cv2.imshow("Median", dst_med)
cv2.waitKey(0)
cv2.destroyAllWindows()