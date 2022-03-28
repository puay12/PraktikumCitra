import cv2

img = cv2.imread('sometin.jpg', 0)
img = cv2.resize(img, (700,500))

img1 = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Invers", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()