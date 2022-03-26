import cv2
import numpy as np
import matplotlib.pyplot as plt

# membaca image
img = cv2.imread('apple.jpg')

B, G, R = cv2.split(img)
gray = 0.33 * R + 0.33 * G + 0.33 * B

ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

titles = ["Original", "Global", "Value 100", "Value 200"]
images = [gray, thresh1, thresh2, thresh3]

for i in range(4) :
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.subplots_adjust(hspace=0.5)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()