import cv2
import numpy as np

# membaca image
img = cv2.imread("girl.jpg")
# resize
img = cv2.resize(img, (500, 500))
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

# build an image with zero filled
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)
new_img5 = np.zeros((height, width, 3), np.uint8)

new_img1 = cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# copy image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i, j][k] = img[i, j][k]

cv2.imshow("Image copy", new_img2)
new_img2 = cv2.cvtColor(new_img2, cv2.COLOR_BGR2RGB)

# flip horizontal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i, j][k] = img[height - 1 - i, j][k]

cv2.imshow("Image flip horizontal", new_img3)

# flip vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img4[i, j][k] = img[i, width - 1 - j][k]

cv2.imshow("Image flip vertikal", new_img4)

# flip horizontal vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img5[i, j][k] = img[height - 1 - i, width - 1 - j][k]

cv2.imshow("Image flip horizontal vertikal", new_img5)

cv2.waitKey(0)
cv2.destroyAllWindows()