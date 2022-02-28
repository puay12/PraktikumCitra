import cv2
import numpy as np

# membaca file gambar
img = cv2.imread("girl.jpg")
# resize
img = cv2.resize(img, (500, 500))

# menampilkan ukuran dan struktur data image
print("Ukuran gambar : ", img.shape)

# get the height and width of the image
height, width = img.shape[0], img.shape[1]
print("Tipe data : ", img.dtype)

# menampilkan image
cv2.imshow("Original Image", img)
# mengakses warna pixel BGR
print(img[136,413])

# copy dan set pixel BGR
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img1 = img.copy()
new_img1[135:146, 413:423] = (0, 255, 0)

# menampilkan updated image
# plt.figure()
# plt.subplot(222)
# plt.imshow(new_img1)
# plt.title("Updated Image")

# build an image with zero filled
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)
new_img4 = np.zeros((height, width, 3), np.uint8)
new_img5 = np.zeros((height, width, 3), np.uint8)
new_img6 = np.zeros((height, width, 3), np.uint8)
new_img7 = np.zeros((height, width, 3), np.uint8)
new_img8 = np.zeros((height, width, 3), np.uint8)

new_img1 = cv2.cvtColor(new_img1, cv2.COLOR_BGR2RGB)

# copy image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img2[i, j][k] = img[i, j][k]

cv2.imshow("Copied Image", new_img2)
new_img2 = cv2.cvtColor(new_img2, cv2.COLOR_BGR2RGB)

# flip horizontal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img3[i, j][k] = img[height - 1 - i, j][k]

cv2.imshow("Horizontally Flipped Image", new_img3)

# flip vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img4[i, j][k] = img[i, width - 1 - j][k]

cv2.imshow("Vertically Flipped Image", new_img4)

# flip horizontal vertikal image
for i in range(height):
    for j in range(width):
        for k in range(3):
            new_img5[i, j][k] = img[height - 1 - i, width - 1 - j][k]

cv2.imshow("Both Side Flipped Image", new_img5)

# rotate image
new_img6 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 90 derajat searah jarum jam
cv2.imshow("Clockwised Rotated Image", new_img6)

new_img7 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 90 derajat berlawanan jarum jam
cv2.imshow("Counterclockwised Rotated Image", new_img7)

rotate_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1.0)
new_img8 = cv2.warpAffine(img, rotate_matrix, (width, height))
cv2.imshow("Rotated image using matrix", new_img8)

cv2.waitKey(0)
cv2.destroyAllWindows()