# KUANTISASI CITRA
import cv2
from cv2 import COLOR_BGR2RGB
from cv2 import COLOR_BGR2GRAY
import numpy as np
import matplotlib.pyplot as plt

# membaca gambar
img = cv2.imread('girl.jpg')
# resize
img = cv2.resize(img, (500, 500))
# coloring
img = cv2.cvtColor(img, COLOR_BGR2GRAY)

img_gray = 128 * np.floor(img/128)
gray1 = img_gray
img_gray = 64 * np.floor(img/64)
gray2 = np.uint8(img_gray)
img_gray = 32 * np.floor(img/32)
gray3 = np.uint8(img_gray)
img_gray = 16 * np.floor(img/16)
gray4 = np.uint8(img_gray)

# show image
titles = [u'(a) Kuantisasi Gray L1', u'(b) Kuantisasi Gray L2', u'(c) Kuantisasi Gray L3', u'(d) Kuantisasi Gray L4']
images = [img, gray1, gray2, gray3, gray4]

for i in range(4):
    plt.subplot(2, 2, i+1),
    plt.imshow(images[i], cmap='gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()