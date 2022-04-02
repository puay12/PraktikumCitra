import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("fish2.jpeg")
img1 = cv2.imread("fish.jpeg")

# GAMBAR 1
# layer B
x_min = np.min(img[:,:,0])
x_max = np.max(img[:,:,0])
sk = 255 / (x_max - x_min)
b = sk * (img[:,:,0] - x_min)

# layer G
x_min = np.min(img[:,:,1])
x_max = np.max(img[:,:,1])
sk = 255 / (x_max - x_min)
g = sk * (img[:,:,1] - x_min)

# layer R
x_min = np.min(img[:,:,2])
x_max = np.max(img[:,:,2])
sk = 255 / (x_max - x_min)
r = sk * (img[:,:,2] - x_min)

img2 = img.copy()
img2[:,:,0] = b
img2[:,:,1] = g
img2[:,:,2] = r
img2 = np.uint8(img2)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# GAMBAR 2
# layer B
x_min = np.min(img1[:,:,0])
x_max = np.max(img1[:,:,0])
sk = 255 / (x_max - x_min)
b = sk * (img1[:,:,0] - x_min)

# layer G
x_min = np.min(img1[:,:,1])
x_max = np.max(img1[:,:,1])
sk = 255 / (x_max - x_min)
g = sk * (img1[:,:,1] - x_min)

# layer R
x_min = np.min(img1[:,:,2])
x_max = np.max(img1[:,:,2])
sk = 255 / (x_max - x_min)
r = sk * (img1[:,:,2] - x_min)

img3 = img1.copy()
img3[:,:,0] = b
img3[:,:,1] = g
img3[:,:,2] = r
img3 = np.uint8(img3)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

plt.subplot(221)
plt.axis('off')
plt.title("Gambar 1 Original")
plt.imshow(img)

plt.subplot(222)
plt.axis('off')
plt.title("Gambar 1 Enhanced")
plt.imshow(img2)

plt.subplot(223)
plt.axis('off')
plt.title("Gambar 2 Original")
plt.imshow(img1)

plt.subplot(224)
plt.axis('off')
plt.title("Gambar 2 Enhanced")
plt.imshow(img3)

plt.show()