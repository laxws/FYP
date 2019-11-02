import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

th1 = cv.imread('Images/PCB/pcb3.jpg')
th2 = cv.imread('Images/PCB/pcb3_missingpinhole.jpg')
grayA = cv.cvtColor(th1,cv.COLOR_BGR2GRAY)
grayB = cv.cvtColor(th2,cv.COLOR_BGR2GRAY)
ret, threshA = cv.threshold(grayA,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
ret, threshB = cv.threshold(grayB,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

# noise removal A
kernelA = np.ones((3,3),np.uint8)
openingA = cv.morphologyEx(threshA,cv.MORPH_OPEN,kernelA, iterations = 2)

# noise removal B
kernelB = np.ones((3,3),np.uint8)
openingB = cv.morphologyEx(threshB,cv.MORPH_OPEN,kernelB, iterations = 2)

# sure background area A
sure_bgA = cv.dilate(openingA,kernelA,iterations=3)

# sure background area B
sure_bgB = cv.dilate(openingB,kernelB,iterations=3)

# Finding sure foreground area A
dist_transform = cv.distanceTransform(openingA,cv.DIST_L2,5)
ret, sure_fgA = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding sure foreground area B
dist_transform = cv.distanceTransform(openingB,cv.DIST_L2,5)
ret, sure_fgB = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region A
sure_fgA = np.uint8(sure_fgA)
unknownA = cv.subtract(sure_bgA,sure_fgA)

# Finding unknown region B
sure_fgB = np.uint8(sure_fgB)
unknownB = cv.subtract(sure_bgB,sure_fgB)

# Marker labelling A
ret, markersA = cv.connectedComponents(sure_fgA)

# Marker labelling B
ret, markersB = cv.connectedComponents(sure_fgB)

# Add one to all labels so that sure background is not 0, but 1 A
markersA = markersA+1

# Add one to all labels so that sure background is not 0, but 1 B
markersB = markersB+1

# Now, mark the region of unknown with zero A
markersA[unknownA==255] = 0

# Now, mark the region of unknown with zero B
markersB[unknownB==255] = 0

markersA = cv.watershed(th1,markersA)
th1[markersA == -1] = [255,0,0]

markersA = cv.watershed(th2,markersB)
th2[markersB == -1] = [255,0,0]

cv.imshow('Master', th1)
cv.imshow('Referential', th2)
'''
grayA = cv.cvtColor(th1, cv.COLOR_BGR2GRAY)
grayB = cv.cvtColor(th2, cv.COLOR_BGR2GRAY)

retval2,th1 = cv.threshold(grayA,125,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
retval2,th2 = cv.threshold(grayB,125,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#th1 = cv.fastNlMeansDenoising(th1,None,10,7,21)
#th2 = cv.fastNlMeansDenoising(th2,None,10,7,21)

bit_and = cv.bitwise_and(th2, th1)
bit_or = cv.bitwise_or(th2, th1)
bit_xor = cv.bitwise_xor(th1, th2)
bit_not = cv.bitwise_not(th1)
bit_not2 = cv.bitwise_not(th2)
dst = bit_xor = cv.bitwise_xor(th1, th2)
denoised = cv.fastNlMeansDenoising(dst,None,10,7,21)

#cv.imshow("th1", th1)
#cv.imshow("th2", th2)
#cv.imshow("bit_and", bit_and)
#cv.imshow("bit_or", bit_or)
cv.imshow("bit_xor", bit_xor)
#cv.imshow("bit_not", bit_not)
#cv.imshow("bit_not2", bit_not2)
cv.imshow("denoised", denoised)
'''
cv.waitKey(0)
cv.destroyAllWindows()

