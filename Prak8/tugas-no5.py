import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.jpg", 0)

sobel_x = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobel_y = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobel = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
sobel = cv2.convertScaleAbs(sobel)

canny = cv2.Canny(img, 100, 200)

im_lap = cv2.Laplacian(img, ksize=5, ddepth=cv2.CV_64F)
im_lap = cv2.convertScaleAbs(im_lap)

sobel = 255 - sobel
canny = 255 - canny
im_lap = 255 - im_lap

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
sobel = cv2.cvtColor(sobel, cv2.COLOR_BGR2RGB)
canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)
im_lap = cv2.cvtColor(im_lap, cv2.COLOR_BGR2RGB)

images = [img, sobel, canny, im_lap]
titles = ["Original", "Sobel", "Canny", "Laplacian"]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])
plt.show()