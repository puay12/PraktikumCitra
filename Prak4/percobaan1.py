import cv2

# membaca gambar
img = cv2.imread('girl.jpg')
# resize
img = cv2.resize(img, (500, 500))
