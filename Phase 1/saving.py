import cv2

image = cv2.imread("03296402722.jpg")

if image is not None:
    success = cv2.imwrite("outout_image.jpg", image)
    if success:
        print("Image Saved successfully as 'output_python.jpg'")

    else:
        print("Could not save image")
else:
    print("Error: Could not find the image")


