import cv2

img = cv2.imread('cup.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('save_img.png', img)
