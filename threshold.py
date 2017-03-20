import cv2

# Reading source image
img = cv2.imread('paper.jpeg')

# Drawing images
retval, threshold = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 35, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 8)

# Displaying images
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus',gaus)

# Saving images
cv2.imwrite('save_img_threshold.png', threshold)
cv2.imwrite('save_img_threshold2.png', threshold2)
cv2.imwrite('save_img_gaus.png',gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
