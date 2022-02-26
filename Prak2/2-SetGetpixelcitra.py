import cv2
import numpy as np

# membaca image
img = cv2.imread("bg.jpg")
# menampilkan ukuran dan struktur data image
print("Ukuran gambar : ", img.shape)

# get the height and width of the image
height, width = img.shape[0], img.shape[1]
print("Tipe data : ", img.dtype)

# menampilkan image
cv2.imshow("Image original", img)

# mengakses warna pixel BGR
print(img[136,413])

# copy dan set pixel BGR
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img1 = img.copy()
new_img1[135:146, 413:423] = (0, 255, 0)

# menampilkan updated image
cv2.imshow("img set pixel : ", new_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()