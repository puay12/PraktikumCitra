import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sunset.jpg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
img_spectrum = 20 * np.log(np.abs(fshift))
img_spectrum = np.array(img_spectrum, np.uint8)
img_spectrum = cv2.cvtColor(img_spectrum, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

titles = ["Original Image", "Fourier Spectrum"]
images = [img, img_spectrum]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()