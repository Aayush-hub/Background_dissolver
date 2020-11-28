import cv2
import numpy as np
cap = cv2.VideoCapture(0)
back = cv2.imread('./back.jpg')
while True:
    ret , frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #lower red = (hue -10,100,100) , Upper red = (h+10,255,255)
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])
        mask = cv2.inRange(hsv, l_red, u_red)
        part1 = cv2.bitwise_and(back , back , mask = mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame,frame, mask= mask)
        cv2.imshow("mask", part1+part2)
        if cv2.waitKey(1) == ord('q'):
            break
#for edge quality go for morphology
cap.release()
cv2.destroyAllWindows()
