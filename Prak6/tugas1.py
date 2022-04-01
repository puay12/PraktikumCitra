import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("underwtr1.png")
img = cv2.resize(img, (800,500))

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

img1 = img.copy()
img1[:,:,0] = b
img1[:,:,1] = g
img1[:,:,2] = r
img1 = np.uint8(img1)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(121)
plt.axis('off')
plt.title("Original")
plt.imshow(img)

plt.subplot(122)
plt.axis('off')
plt.title("Enhanced")
plt.imshow(img1)
plt.show()

# cv2.imshow("Original", img)
# cv2.imshow("Enhanced", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()