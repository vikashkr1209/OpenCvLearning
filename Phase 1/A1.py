import cv2

path = input("Enter the path of the image: ")
image = cv2.imread(path)

print("Which action do you want to perform:")
print("1 Show, 2 Grey_Scale,3 Save_image")
Choice = input("Enter your choice: ")
if Choice == "1":
    if image is not None:
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Please enter a valid path")
elif Choice == "2":
    if image is not None:
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        cv2.imshow("Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Please enter a valid path")
elif Choice == "3":
    if image is not None:
        success = cv2.imwrite("outout_image.jpg", image)
        if success:
            print("Image successfully saved", image)
        else:
            print("Image could not be saved")
    else:
        print("Please enter a valid path")






