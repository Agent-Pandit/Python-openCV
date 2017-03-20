import cv2

img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')

# types of image addition

# method I
# size of image need to be same
add = img1 + img2
cv2.imshow('img1 + img2', add)

# method II
add = cv2.add(img1, img2)
cv2.imshow('(add(img1, img2)', add)

# method III
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()
