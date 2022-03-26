import cv2
import matplotlib.pyplot as plt

# membaca data image
img = cv2.imread("dark.jpg")
# resize
img = cv2.resize(img, (500,500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thres0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thres1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
thres2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)

titles = ["Original Image", "Global Thresholding (v = 127)", "Adaptive Mean Thresholding", "Adaptive Gaussian Thresholding"]
images = [img, thres0, thres1, thres2]

for i in range(4) :
    plt.subplot(2, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()