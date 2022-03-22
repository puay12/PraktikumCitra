# KUANTISASI CITRA
import cv2
import numpy as np

# membaca gambar
img = cv2.imread('girl.jpg')
# resize
img = cv2.resize(img, (500, 500))
height, width = img.shape[0], img.shape[1]

new_img = np.zeros((height, width, 3), np.uint8)

# the quantification level is 2
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 129
            new_img[i, j][k] = np.uint8(gray)

# show image
cv2.imshow("Original Image", img)
cv2.imshow("Quantificated Image", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()