import cv2

image = cv2.imread("03296402722.jpg")

if image is None:
    print("Image Not Found")
else:
    print("Image Loaded Successfully")

cv2.waitKey(0)
cv2.destroyAllWindows()