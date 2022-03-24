import cv2

# membaca data image
img = cv2.imread("cat.jpg")
# resize
img = cv2.resize(img, (500,500))

b = img.copy()
b[:,:,1] = 0
b[:,:,2] = 0

g = img.copy()
g[:,:,0] = 0
g[:,:,2] = 0

r = img.copy()
r[:,:,0] = 0
r[:,:,1] = 0

cv2.imshow("Orginal", img)
cv2.imshow("B-RGB", b)
cv2.imshow("G-RGB", g)
cv2.imshow("R-RGB", r)

cv2.waitKey(0)
cv2.destroyAllWindows()