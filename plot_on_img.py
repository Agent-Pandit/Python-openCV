import matplotlib.pyplot as plt
import cv2

img = cv2.imread('cup.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [200, 180], 'c', linewidth=5)
plt.plot([200, 100], [80, 100], 'd', linewidth=5)
plt.show()
