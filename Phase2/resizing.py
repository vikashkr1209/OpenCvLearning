# resizing and scaling Images -cv2.resize()
import cv2

img = cv2.imread("Modi.jpg")
if img is None:
    print("Could not find the image")
else:
    print("The image loaded")

    resized = cv2.resize(img,(300,300)) # width, height 

    cv2.imshow("Original",img)
    cv2.imshow("Resized",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()