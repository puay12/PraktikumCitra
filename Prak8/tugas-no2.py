import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg', 0)

kernel = np.ones((4, 4), np.float32) / 16
dst_blur = cv2.filter2D(img, -1, kernel)

kernel_v = np.array([[0, -0.5 , 0], [-0.5, 0, 0.5], [0, 0.5, 0]])
kernel_h = np.transpose(kernel_v)
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst_edge = cv2.add(dst_v, dst_h)

img2 = cv2.add(img, dst_edge)
img_inverse = 255 - dst_edge

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_inverse = cv2.cvtColor(img_inverse, cv2.COLOR_BGR2RGB)

images = [img, img_inverse]
titles = ["Original", "Sharp"]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])
plt.show()

# kernel kedua
kernel_v = np.array([[0, -0.5 , 0], [-0.5, 1, 0.5], [0, 0.5, 0]])
kernel_h = np.transpose(kernel_v)
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst_edge = cv2.add(dst_v, dst_h)

img2 = cv2.add(img, dst_edge)
img_inverse = 255 - dst_edge

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_inverse = cv2.cvtColor(img_inverse, cv2.COLOR_BGR2RGB)

images = [img, img_inverse]
titles = ["Original", "Sharp"]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])
plt.show()