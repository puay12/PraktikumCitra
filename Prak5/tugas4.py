import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sundae.jpg', 0)

img1 = 40 * np.log(0.5 * img)
img1 = cv2.cvtColor(np.uint8(img1), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(255 - img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(255 - img1, cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

titles = ["Original Image", "Log a = 40 b = 0.5", "Invers", "Invers Log"]
images = [img, img1, img2, img3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()