import cv2
import numpy as np

# membaca data image
img = cv2.imread("cat.jpg")
# resize
img = cv2.resize(img, (500,500))
# split ke abu" masing" channel
B, G, R = cv2.split(img)

img_gray1 = 0.33 * R + 0.33 * G + 0.33 * B
img_gray1 = img_gray1.astype(np.uint8)
img_RG1 = np.minimum(R, G)

img_gray2 = np.minimum(img_RG1, B)
img_RG2 = np.maximum(R, G)

img_gray3 = np.maximum(img_RG2, B)

cv2.imshow("Original", img)
cv2.imshow("Iluminasi Rata-rata", img_gray1)
cv2.imshow("Ilumniasi minimum", img_gray2)
cv2.imshow("Iluminasi maksimum", img_gray3)

cv2.waitKey(0)
cv2.destroyAllWindows()