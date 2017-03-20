import cv2
import numpy as np

img = cv2.imread('cup.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (200, 200), (125, 0, 90), 12)
cv2.rectangle(img, (20, 35), (320, 60), (0, 200, 50), 8)
cv2.circle(img, (100, 63), 23, (220, 20, 59), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10], [80, 60], [11, 12]])
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 146, 73, 33), 4)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
