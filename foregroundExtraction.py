import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img_file_name.extension')
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65), np.float64)

# Values as may be required according to image
rect = (50, 0, 300, 500)

cv2.grabCut(img, mask, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('unit8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colormaps()
plt.show()
