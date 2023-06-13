#image transformation
import cv2 as cv
import numpy as np

img=cv.imread('Videos/tree.jpg')

cv.imshow('Image',img)

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(img,100,100)
cv.imshow('Translate', translated)
    
#rotation
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    
    if rotpoint is None:
        rotpoint=(width//2,height//2)
        
    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('Rotated', rotated) 

rotated_1=rotate(rotated,20)
cv.imshow('rotated_1', rotated_1)

#resize

resized=cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR_EXACT)
cv.imshow('Resized', resized)
    
#flipping

flip=cv.flip(img,1)
cv.imshow('Flip',flip)

#cropping

cropped=img[200:400,300:400]
cv.imshow('Cropped', cropped)

rotated=rotate(img,45)
cv.imshow('Rotated', rotated) 


cv.waitKey(0)

cv.destroyAllWindows()