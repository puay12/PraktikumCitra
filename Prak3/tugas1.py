import cv2
import numpy as np

# membaca data image
img = cv2.imread("koala.jpg")
# resize
img = cv2.resize(img, (700, 500))
# copy
sepia_img = img.copy()

sepia_img = np.array(img, dtype=np.float64) # converting to float to prevent loss
sepia_img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                        [0.349, 0.686, 0.168],
                                        [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix]))

sepia_img[np.where(sepia_img > 255)] = 255 #normalizing values greater than 255 to 255
sepia_img = np.array(sepia_img, np.uint8) # converting back to int

# r = img[:,:,2]
# new_img1 = img.copy()
# new_img1[:,:,2] = 2 * r
# new_img1[:,:,1] = 1.8 * r
# new_img1[:,:,0] = r

cv2.imshow("Original Image", img)
cv2.imshow("Sephia Image", sepia_img)

cv2.waitKey(0)
cv2.destroyAllWindows()