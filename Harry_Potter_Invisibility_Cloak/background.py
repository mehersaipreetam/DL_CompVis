import cv2

cap = cv2.VideoCapture(0)
# 0 for webcam

while cap.isOpened():
    ret, back = cap.read()

    if ret:
        cv2.imshow("Image", back)
        if cv2.waitKey(1) == ord("q"):
            #save the Image
            cv2.imwrite('background.jpg',back)
            break
cap.release()
cv2.destroyAllWindows()
