import cv2

image = cv2.imread("flower.jpg")

scale = 0.25

width = int(image.shape[1] * scale)
height = int(image.shape[0] * scale)

resized = cv2.resize(image, (width, height))

edges = cv2.Canny(resized, 50, 150)

cv2.imshow("Original", resized)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()