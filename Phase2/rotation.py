import cv2

image = cv2.imread("Modi.jpg")

if image is None:
    print("Image Not Found")
else:
    (h, w) = image.shape[:2] # getting only height and width slicing
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 180,1.0)
    rotated = cv2.warpAffine(image,M,(h,w))

    cv2.imshow("Original",image)
    cv2.imshow("Rotated",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()