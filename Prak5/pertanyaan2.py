import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('sundae.jpg', 0)
img1 = img + 255.
img1 = np.uint8(img1)

plt.subplot(121)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image")
plt.subplot(122)
plt.imshow(img1, cmap='gray', vmin=0, vmax=255)
plt.title("Brigtness +255")
plt.show()