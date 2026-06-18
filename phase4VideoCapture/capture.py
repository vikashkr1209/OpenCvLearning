import cv2

cap = cv2.VideoCapture(0) # it capture our video with webcam(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Video not read")
        break
    cv2.imshow("webcam feed",frame)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quit")
        break

cap.release()
cv2.destroyAllWindows()