import cv2

image = cv2.imread("Modi.jpg")

# blured = cv2.GaussianBlur(image,(5,5),0)
blured = cv2.medianBlur(image,7)
cv2.imshow("Original Image",image)
cv2.imshow("Blurred Image",blured)
img = cv2.imwrite("Blurred_Image.jpg",blured)

cv2.waitKey(0)
cv2.destroyAllWindows()