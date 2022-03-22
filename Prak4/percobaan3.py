import cv2
from cv2 import COLOR_BGR2RGB
import numpy as np
import matplotlib.pyplot as plt

# membaca img
img = cv2.imread('girl.jpg')
# resize
img = cv2.resize(img, (500, 500))

height, width = img.shape[0], img.shape[1]

# color
img = cv2.cvtColor(img, COLOR_BGR2RGB)
new_img1 = cv2.cvtColor(img, COLOR_BGR2RGB)
new_img2 = cv2.cvtColor(img, COLOR_BGR2RGB)
new_img3 = cv2.cvtColor(img, COLOR_BGR2RGB)

# bangun img, content is zero filled
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)

# the quantification level is 2
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 129
            new_img1[i, j][k] = np.uint8(gray)

# the quantification level is 4
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img2[i, j][k] = np.uint8(gray)

# the quantification level is 8
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 32:
                gray = 0
            elif img[i, j][k] < 64:
                gray = 32
            elif img[i, j][k] < 96:
                gray = 64
            elif img[i, j][k] < 128:
                gray = 96
            elif img[i, j][k] < 160:
                gray = 128
            elif img[i, j][k] < 192:
                gray = 160
            elif img[i, j][k] < 224:
                gray = 192
            else:
                gray = 224
            new_img3[i, j][k] = np.uint8(gray)

# show image
titles = [u'(a) Original Image', u'(b) Kuantisasi Gray L2', u'(c) Kuantisasi Gray L4', u'(d) Kuantisasi Gray L8']
images = [img, new_img1, new_img2, new_img3]

for i in range(4):
    plt.subplot(2, 2, i+1),
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()