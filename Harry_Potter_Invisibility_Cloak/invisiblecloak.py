import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('background.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        #Use cvtColor for rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        ### Demonstartes HSV Image for understanding
            #cv2.imshow('HSV image',hsv)

        ### Setting threshold range which is used to detect and mask close to blue oarts and mask. The range that worked for me:
            #lower: hue-20,70,70, higher: hue+20,255,255

        ### Run this snippet to test your threshold values. In a good scenario, you observe white on the desired cloak region
            #blue = np.uint8([[[255,0,0]]])
            #hsv_blue = #cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
            #print(hsv_blue)
            # [120,255,255] is the output for blue.


        l_blue = np.array([70,70,70])
        u_blue = np.array([140,255,255])

        mask = cv2.inRange(hsv,l_blue,u_blue)
        ### To check
            #cv2.imshow("Masked part",mask)

        ####
        #   What we have to do. The mask part outputs all black, except on the selected colour region, thats white
        #   So we are anding that region with the background image we took before, so all white part is replaced.
        #   And this leaves black part as it is.
        ####

        ###
        #   Opencv morphology
        #   Refer Docs
        ###
        kernel = np.ones((3,3),np.uint8)
        mask = cv2.dilate(mask,kernel,iterations = 1)
        kernel = np.ones((10,10),np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        part1 = cv2.bitwise_and(back,back,mask=mask)

        ### To check
            #cv2.imshow("part1",part1)

        ###
        #   Now, we make all black in mask white and all white in mask black. By simple not.
        #   Why? Because now we have to take the part other than the mask from the live feed only,
        #   So we not it and and with frame this time
        ###

        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame,frame,mask=mask)

        #cv2.imshow("Mask",part2)

        ###
        #   Now the final output is adding part1 and part2 as images are nothing but arrays at the end of the day
        #   Part1 mask region, Part2 others. So add
        ###

        final_frame = part1 + part2

        cv2.imshow("Cloak",final_frame)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
