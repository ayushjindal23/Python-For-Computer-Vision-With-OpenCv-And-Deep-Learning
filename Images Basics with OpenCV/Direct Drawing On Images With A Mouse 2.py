import cv2 as cv
import numpy as np


################
### FUNCTION ###
################

def draw_circle(event,x,y,flags,param):
    
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),100,(0,255,0),-1)
        
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),100,(255,0,0),-1)

cv.namedWindow(winname='my_drawing')

cv.setMouseCallback('my_drawing',draw_circle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = np.zeros((512,512,3),np.int8)

while True:
    
    cv.imshow('my_drawing',img)
    
    if cv.waitKey(20) & 0xFF == 27:
        break