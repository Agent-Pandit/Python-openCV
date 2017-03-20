import cv2
import numpy as np

img_bgr = cv2.imread('patterns.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template.png')
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 25, 255), 2)

cv2.imshow('deteceed', img_bgr)

# Traceback (most recent call last):
#   File "F:/OpenCV python/templateMatching.py", line 8, in <module>
#     w, h = template.shape[::-1]
# ValueError: too many values to unpack (expected 2)
