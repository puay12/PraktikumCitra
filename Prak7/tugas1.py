import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower1.jpg", 0)
img1 = cv2.equalizeHist(img)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 1 Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 1 Original')

plt.subplot(2, 2, 3)
plt.imshow(img1, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 1 Enhanced')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(img1.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 1 Enhanced')
plt.show()

img = cv2.imread("flower2.jpg", 0)
img1 = cv2.equalizeHist(img)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 2 Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 2 Original')

plt.subplot(2, 2, 3)
plt.imshow(img1, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 2 Enhanced')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(img1.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 2 Enhanced')
plt.show()

img = cv2.imread("flower3.jpg", 0)
img1 = cv2.equalizeHist(img)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 3 Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 3 Original')

plt.subplot(2, 2, 3)
plt.imshow(img1, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Gambar 3 Enhanced')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(img1.flatten(), 256, [0, 256], color='r')
plt.title('Histogram Gambar 3 Enhanced')
plt.show()