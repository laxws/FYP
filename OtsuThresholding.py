import cv2
import numpy as np

imgA = cv2.imread("Database Pic/pcb3.jpg")
imgB = cv2.imread("Database Pic/pcb3_missingpinhole.jpg")

grayA = cv2.cvtColor(imgA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imgB,cv2.COLOR_BGR2GRAY)

th1 = cv2.adaptiveThreshold(grayA, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
th2 = cv2.adaptiveThreshold(grayB, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval2,th3 = cv2.threshold(grayA,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retval2,th4 = cv2.threshold(grayB,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Master AT',th1)
cv2.imshow('Refrential AT',th2)
cv2.imshow('Master Otsu',th3)
cv2.imshow('Refrential Otsu',th4)

cv2.waitKey(0)
cv2.destroyAllWindows()