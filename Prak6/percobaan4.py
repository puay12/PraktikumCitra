import cv2
import numpy as np

img = cv2.imread("foggy.jpg", 0)
img = cv2.resize(img, (700,500))

x_min = np.min(img)
x_max = np.max(img)

print (x_min)
print (x_max)

sk = 255. / (x_max-x_min)
img1 = sk * (img-x_min)
img1 = np.uint8(img1)

cv2.imshow("Original", img)
cv2.imshow("Enhanced", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()