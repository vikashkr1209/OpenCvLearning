import cv2

image = cv2.imread("image3.jpg")

scale = 0.25

width = int(image.shape[1] * scale)
height = int(image.shape[0] * scale)

resized = cv2.resize(image, (width, height))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 120,255,cv2.THRESH_BINARY)

cv2.imshow("Original", gray)
cv2.imshow("Edges", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()