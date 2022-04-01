import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sunset.jpg')

# gamma = 2.2
img1 = cv2.cvtColor(np.array(255*(img/255)**2.2, dtype='uint8'), cv2.COLOR_BGR2RGB)
# gamma = 0.4
img2 = cv2.cvtColor(np.array(255*(img/255)**0.4, dtype='uint8'), cv2.COLOR_BGR2RGB)
# gamma = 1.4
img3 = cv2.cvtColor(np.array(255*(img/255)**1.4, dtype='uint8'), cv2.COLOR_BGR2RGB)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

titles = ["Original Image", "Gamma = 2.2", "Gamma = 0.4", "Gamma = 1.4"]
images = [img, img1, img2, img3]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()