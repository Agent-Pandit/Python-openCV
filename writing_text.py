import cv2
import numpy as np

img = cv2.imread('cup.jpg', cv2.IMREAD_COLOR)

font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, "TEXT RIGHT HERE :)", (0, 130), font, 1, (0, 2, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
