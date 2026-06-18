import cv2

image = cv2.imread("Modi.jpg")

if image is not None:
    size = image.shape
    print(size)
    cropped = image[0:500, 0:700] # image[y-axis, x-axis]
    cv2.imshow("cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()