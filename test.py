import os
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np


def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = "adb shell input swipe 300 1600 300 1600 " + str(press_time)
    print(cmd)
    m2 = os.popen(cmd)


scale=0.35
x1=x2=y1=y2=0
cnt = 0
def caculate(event,x,y,flags,param):
    global cnt, x1, x2, y1, y2
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cnt = cnt + 1
        if cnt==1:
            x1=x
            y1=y
        elif cnt==2:
            x2=x
            y2=y
            distance = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
            distance = np.sqrt(distance)/scale
            print(distance)
            jump(distance)
            cnt = 0


cv2.namedWindow("screenshot")
cv2.setMouseCallback('screenshot', caculate)

while(1):
    # use adb to create a screenshot
    m1=os.popen("adb shell screencap /sdcard/screen.png")

    # wait finish
    time.sleep(2)

    #read message
    m2=os.popen("adb pull /sdcard/screen.png C:\\Users\\jeffery\\Desktop\\jump\\shot")

    time.sleep(1)
    #caculate time from distance
    im = cv2.imread("shot\\screen.png")
    im2 = cv2.resize(im, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("screenshot",im2)
    cv2.waitKey(0)


