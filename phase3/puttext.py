import cv2

image = cv2.imread("Modi.jpg")

if image is None:
    print("Image Not Found")
else:
    print("Image Found")
    cv2.putText(image,
                "Hi modu",(300,400),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.3,
                (0,255,0),2)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()