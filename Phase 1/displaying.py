import cv2

image = cv2.imread("03296402722.jpg")

if image is not None:
    cv2.imshow("Image Opened", image) # open the window
    cv2.waitKey(0)# wait for a key
    cv2.destroyAllWindows() # close the window
else:
    print("Could not open or find the image")

