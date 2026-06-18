import cv2
from fontTools.cffLib.transforms import StopHintCountEvent

image = cv2.imread("Modi.jpg")

if image is None:
    print("Could not open image")
else:
    print("Image Loaded")
    center = (300,300)
    radius = 100
    color = (255,0,0)
    thickness = 2
    cv2.circle(image,center,radius,color,thickness)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()