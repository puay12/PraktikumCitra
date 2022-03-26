import cv2
import matplotlib.pyplot as plt
import numpy as np
from urllib3.connectionpool import xrange

# membaca data image
img = cv2.imread("koala.jpg")
img = cv2.resize(img, (700, 500))
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# layer BGR
b = img.copy()
b[:,:,1] = 0
b[:,:,2] = 0
b = cv2.cvtColor(b, cv2.COLOR_RGB2BGR)
g = img.copy()
g[:,:,0] = 0
g[:,:,2] = 0
g = cv2.cvtColor(g, cv2.COLOR_RGB2BGR)
r = img.copy()
r[:,:,0] = 0
r[:,:,1] = 0
r = cv2.cvtColor(r, cv2.COLOR_RGB2BGR)

titles = ["Original Image", "B-RGB", "G-RGB", "R-RGB"]
images = [img, b, g, r]

for i in xrange(4) :
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.subplots_adjust(hspace=0.5)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# citra grayscale
B, G, R = cv2.split(img)
B = cv2.cvtColor(B, cv2.COLOR_RGB2BGR)
G = cv2.cvtColor(G, cv2.COLOR_RGB2BGR)
R = cv2.cvtColor(R, cv2.COLOR_RGB2BGR)

titles = ["Original Image", "Channel B", "Channel G", "Channel R"]
images = [img, B, G, R]

for i in xrange(4) :
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.subplots_adjust(hspace=0.5)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# citra grayscale dengan iluminasi
img_gray1 = 0.33 * R + 0.33 * G + 0.33 * B
img_gray1 = img_gray1.astype(np.uint8)
img_gray1 = cv2.cvtColor(img_gray1, cv2.COLOR_RGB2BGR)
rg = np.minimum(R, G)
img_gray2 = np.minimum(B, rg)
img_gray2 = cv2.cvtColor(img_gray2, cv2.COLOR_RGB2BGR)
rg = np.maximum(R, G)
img_gray3 = np.maximum(rg, B)
img_gray3 = cv2.cvtColor(img_gray3, cv2.COLOR_RGB2BGR)

titles = ["Original Image", "Iluminasi rata-rata", "Iluminasi minimum", "Iluminasi maksimum"]
images = [img, img_gray1, img_gray2, img_gray3]

for i in xrange(4) :
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.subplots_adjust(hspace=0.5)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# binar
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6) :
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.subplots_adjust(hspace=0.5)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()