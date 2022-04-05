import cv2

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))
img_blur1 = cv2.blur(img, [5, 5])
img_blur2 = cv2.blur(img, [11, 11])

cv2.imshow("Original", img)
cv2.imshow("Blur 5x5", img_blur1)
cv2.imshow("Blur 11x11", img_blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()