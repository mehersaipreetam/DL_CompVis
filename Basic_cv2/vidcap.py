import cv2

capture = cv2.VideoCapture(0)
# 0 is for web-cam

while True:

    # ret is True or False, to see if live feed is on or not.
    ret, frame = capture.read()

    classifier = cv2.CascadeClassifier('HaarCascade_FrontalFace/haarcascade_frontalface_default.xml')
    faces = classifier.detectMultiScale(frame)

    for face in faces:
        x,y,w,h = face
        face_in_pic = frame[y : y + h, x : x + w]


        if ret:
            face_detect_in_feed = cv2.rectangle(frame,(x,y),(x+w,y+h), (100,0,0),2)
            cv2.imshow('My Window',face_detect_in_feed)

        key = cv2.waitKey(1)

        if key == ord("q"):
            capture.release()
            cv2.destroyAllWindows()
