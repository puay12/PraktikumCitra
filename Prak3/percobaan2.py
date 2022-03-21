import cv2

# membaca data image
img = cv2.imread("girl.jpg")
# resize
img = cv2.resize(img, (500,500))

B, G, R = cv2.split(img)
cv2.imshow("Original", img)
cv2.imshow("Channel R", R)
cv2.imshow("Channel G", G)
cv2.imshow("Channel B", B)

cv2.waitKey(0)
cv2.destroyAllWindows()