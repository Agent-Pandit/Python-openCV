import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    edges = cv2.Canny(frame, 100, 100)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
