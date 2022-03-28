import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sundae.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 = img_gray * 0.5
img2 = img_gray * 0.75
img3 = img_gray * 1.25
img4 = img_gray * 1.5

plt.subplot(231)
plt.imshow(img_gray, cmap='gray', vmin=0, vmax =255)
plt.title("Original Image")
plt.subplot(232)
plt.imshow(img1, cmap='gray', vmin=0, vmax= 255)
plt.title("c = 0.5")
plt.subplot(233)
plt.imshow(img2, cmap='gray', vmin=0, vmax=255)
plt.title("c = 0.75")
plt.subplot(234)
plt.imshow(img3, cmap='gray', vmin=0, vmax= 255)
plt.title("c = 1.25")
plt.subplot(235)
plt.imshow(img4, cmap='gray', vmin=0, vmax=255)
plt.title("c = 1.5")
plt.show()