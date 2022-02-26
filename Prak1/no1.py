import cv2

#membaca image
img = cv2.imread("bg.jpg")

#menampilkan ukuran dan struktur data image
print("Ukuran gambar : ", img.shape)
print("Type data : ", img.dtype)

#menampilkan image
cv2.imshow("Image : ", img)

cv2.waitKey(0)
cv2.destroyAllWindows()