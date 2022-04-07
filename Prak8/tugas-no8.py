import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg", 0)

kernel1 = np.ones([5, 5], np.float32) / 25
img_blur = cv2.filter2D(img, -1, kernel1)

kernel2a = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernel2b = np.transpose(kernel2a)
kernel2 = kernel2a + kernel2b
img_edge = 0.5 * cv2.filter2D(img, -1, kernel2)
img_edge = np.uint8(img_edge)
img_edges = np.add(img_edge, img_edge)

img_sharp = cv2.add(img_blur, img_edges)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_sharp = cv2.cvtColor(img_sharp, cv2.COLOR_BGR2RGB)
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_BGR2RGB)

images = [img, img_sharp]
titles = ["Original", "Sharp"]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])
plt.show()