import cv2 as cv 

img = cv.imread('C:/Users/Ayush/Desktop/CV with python/New folder/00-puppy.png')

while True:

    cv.imshow('Puppy',img)
    
    # If we've waited atleast 1 ms AND we've pressed th Esc
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()