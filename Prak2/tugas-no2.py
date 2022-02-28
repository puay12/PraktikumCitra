import cv2
import numpy as np
import matplotlib.pyplot as plt

# membaca file gambar
img = cv2.imread("girl.jpg")
# resize
img = cv2.resize(img, (500, 500))

# menampilkan ukuran dan struktur data image
print("Ukuran gambar : ", img.shape)

# get the height and width of the image
height, width = img.shape[0], img.shape[1]
print("Tipe data : ", img.dtype)

# mengakses warna pixel BGR
print(img[136,413])

# copy dan set pixel BGR
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img1 = img.copy()
new_img1[135:146, 413:423] = (0, 255, 0)

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

plt.figure()
plt.subplot(221)
plt.tight_layout(pad=3.0)
plt.imshow(new_img2)
plt.title("Copied Image")
new_img2 = cv2.cvtColor(new_img2, cv2.COLOR_BGR2RGB)

# flip horizontal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i, j][k] = img[height - 1 - i, j][k]

plt.subplot(222)
plt.imshow(new_img3)
plt.title("Horizontally Flipped Image")

# flip vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img4[i, j][k] = img[i, width - 1 - j][k]

plt.subplot(223)
plt.imshow(new_img4)
plt.title("Vertically Flipped Image")

# flip horizontal vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img5[i, j][k] = img[height - 1 - i, width - 1 - j][k]

plt.subplot(224)
plt.imshow(new_img5)
plt.title("Flipped Image")