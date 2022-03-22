import cv2

# membaca data image
img = cv2.imread("girl.png")
# resize
img = cv2.resize(img, (500,500))

r = img[:,:,2]

new_img1 = img.copy()
new_img1[:,:,2] = 2 * r
new_img1[:,:,1] = 1.8 * r
new_img1[:,:,0] = r

cv2.imshow("Original Image", img)
cv2.imshow("Sephia Image", new_img1)

cv2.waitKey(0)
cv2.destroyAllWindows()