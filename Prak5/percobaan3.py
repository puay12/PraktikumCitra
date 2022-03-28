import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sundae.jpg', 0)

img1 = 255 - img

plt.subplot(121)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("Invers")
plt.show()