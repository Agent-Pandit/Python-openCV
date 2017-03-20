import cv2

img = cv2.imread('cup.jpg',cv2.IMREAD_COLOR)

## making a pixel blank
##img[55,55] = [255,255,255]
img[300,300] = [0,0,0]

## copying a region of image
watch_face = img[37:211,107:294]
## redrawing over image img
img[0:174,0:187] = watch_face

## draw the new image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()