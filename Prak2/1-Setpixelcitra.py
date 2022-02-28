import cv2
# membaca image
img = cv2.imread("bg.jpg")
# menampilkan ukuran dan struktur data image
print("Ukuran ganbar : ", img.shape)
print("Tipe data gambar : ", img.dtype)

# mengakses warna pixel BGR
print(img[213,310])

# menampilkan image
cv2.imshow("img original : ", img)
cv2.waitKey(0)
cv2.destroyAllWindows()