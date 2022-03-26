import cv2
from cv2 import COLOR_BGR2RGB
from cv2 import COLOR_BGR2GRAY
import numpy as np
import matplotlib.pyplot as plt

# membaca img
img = cv2.imread('apple.jpg')

height, width = img.shape[0], img.shape[1]

# color
img = cv2.cvtColor(img, COLOR_BGR2RGB)
gray_induk = cv2.cvtColor(img, COLOR_BGR2GRAY)
color1 = img.copy()
color2 = img.copy()
color3 = img.copy()

# bangun img, content is zero filled
color1 = np.zeros((height, width, 3), np.uint8)
color2 = np.zeros((height, width, 3), np.uint8)
color3 = np.zeros((height, width, 3), np.uint8)

# color
# the quantification level is 5
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 51:
                gray = 0
            elif img[i, j][k] < 102:
                gray = 51
            elif img[i, j][k] < 153:
                gray = 102
            elif img[i, j][k] < 204:
                gray = 153
            else:
                gray = 204
            color1[i, j][k] = np.uint8(gray)

# the quantification level is 6
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 43:
                gray = 0
            elif img[i, j][k] < 86:
                gray = 43
            elif img[i, j][k] < 129:
                gray = 86
            elif img[i, j][k] < 172:
                gray = 129
            elif img[i, j][k] < 215:
                gray = 172
            else:
                gray = 215
            color2[i, j][k] = np.uint8(gray)

# the quantification level is 7
for i in range(height):
    for j in range(width):
        for k in range(3):
            if img[i, j][k] < 36:
                gray = 0
            elif img[i, j][k] < 72:
                gray = 36
            elif img[i, j][k] < 108:
                gray = 72
            elif img[i, j][k] < 144:
                gray = 108
            elif img[i, j][k] < 180:
                gray = 144
            elif img[i, j][k] < 216:
                gray = 180
            else:
                gray = 216
            color3[i, j][k] = np.uint8(gray)

# gray 
gray = 128 * np.floor(gray_induk/128) #level 1
img_gray1 = gray
gray = 64 * np.floor(gray_induk/64) #level 2
img_gray2 = np.uint8(gray)
gray = 32 * np.floor(gray_induk/32) #level 3
img_gray3 = np.uint8(gray)
gray = 16 * np.floor(gray_induk/16) #level 4
img_gray4 = np.uint8(gray)
gray = 8 * np.floor(gray_induk/8) #level 5
img_gray5 = np.uint8(gray)
gray = 4 * np.floor(gray_induk/4) #level 6
img_gray6 = np.uint8(gray)
gray = 2 * np.floor(gray_induk/2) #level 7
img_gray7 = np.uint8(gray)
gray = 1 * np.floor(gray_induk/1) #level 8
img_gray8 = np.uint8(gray)

# show image
titles = ['Original Image', 'Kuantisasi Color L5', 'Kuantisasi Color L6', 'Kuantisasi Color L7', 'Kuantisasi Gray L1', 'Kuantisasi Gray L2', 'Kuantisasi Gray L3', 'Kuantisasi Gray L4', 'Kuantisasi Gray L5', 'Kuantisasi Gray L6', 'Kuantisasi Gray L7', 'Kuantisasi Gray L8']
images = [img, color1, color2, color3, img_gray1, img_gray2, img_gray3, img_gray4, img_gray5, img_gray6, img_gray7, img_gray8]

for i in range(12):
    plt.subplot(3, 4, i+1),
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()