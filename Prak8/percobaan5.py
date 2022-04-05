import cv2

img = cv2.imread("flower.jpg", 0)
img = cv2.resize(img, (400, 600))

sobel_x = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobel_y = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobel = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
sobel = cv2.convertScaleAbs(sobel)

canny = cv2.Canny(img, 100, 200)

im_lap = cv2.Laplacian(img, ksize=5, ddepth=cv2.CV_64F)
im_lap = cv2.convertScaleAbs(im_lap)

cv2.imshow("Grayscale", img)
cv2.imshow("Sobel", sobel)
cv2.imshow("Canny", canny)
cv2.imshow("Laplacian", im_lap)
cv2.waitKey(0)
cv2.destroyAllWindows()