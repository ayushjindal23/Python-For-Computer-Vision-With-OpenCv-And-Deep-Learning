import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),thickness=10)

cv2.namedWindow(winname='dog')

cv2.setMouseCallback('dog',draw_circle)

img = cv2.imread("D:\Computer-Vision-with-Python\DATA\dog_backpack.jpg")

while True:

    cv2.imshow('dog',img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

