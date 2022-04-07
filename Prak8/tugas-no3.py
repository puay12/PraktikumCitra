import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg', 0)

kernel = np.ones((8, 8), np.float32) / 64
dst_blur = cv2.filter2D(img, -1, kernel)

kernel_v = np.array([[-1, -0.5 , 0], [-0.5, 1, 0.5], [0, 0.5, 1]])
kernel_h = np.transpose(kernel_v)
dst_h = cv2.filter2D(img, -1, kernel_h)
dst_v = cv2.filter2D(img, -1, kernel_v)
dst_edge = cv2.add(dst_v, dst_h)

img2 = cv2.add(img, dst_edge)
img_inverse = 255 - dst_edge

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_inverse = cv2.cvtColor(img_inverse, cv2.COLOR_BGR2RGB)
dst_blur = cv2.cvtColor(dst_blur, cv2.COLOR_BGR2RGB)
dst_edge = cv2.cvtColor(dst_edge, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

images = [img, dst_blur, dst_edge, img2, img_inverse]
titles = ["Original", "Image Blur", "Image Edge", "Sharp", "Sketsa"]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])
plt.show()