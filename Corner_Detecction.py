import cv2
import numpy as np

img = cv2.imread('corner.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)


# displayed image gets destoyed :: Reason?
# imwrite to check the outup --> satisfactory
cv2.imshow('corner', img)
cv2.imwrite('save_img_corner.png', img)
