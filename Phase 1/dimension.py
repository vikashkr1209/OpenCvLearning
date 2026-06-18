import cv2

image = cv2.imread("03296402722.jpg")
# .shape will give the dimension image(height,width,color channels
if image is not None:
    h,w,c = image.shape
    print(f"Image shape: \nHeight:{h}\nWidth:{w}\nColor:{c}")
else:
    print("Could not find the image")