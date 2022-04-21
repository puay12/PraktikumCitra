import numpy as np
import scipy.signal as sc

img = np.array([[3,3,3,3,3,3,3], [3,4,4,4,4,4,3], [3,4,1,4,4,4,3], [3,4,0,0,0,1,3], [3,4,1,0,0,0,3], [3,3,3,0,0,3,3]])

kernel = np.array([[0.1,0.1,0.1], [0.1,0.2,0.1], [0.1,0.1,0.1]])
img1 = sc.convolve(img, kernel, mode='same', method='auto')

print(img1)