import cv2

image = cv2.imread("03296402722.jpg")
if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imshow("Gray Scale",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not find the image")