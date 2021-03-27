import cv2 as cv

img = cv.imread('DATA/00-puppy.jpg')

while True:
    cv.imshow('img',img)

    if cv.waitKey(1) & 0xFF == 27:
        break
        
cv.destroyAllWindows()