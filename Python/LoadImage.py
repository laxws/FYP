# load image from dataset
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgA = cv2.imread('Images/Results Watershed/pcb3master.jpg', cv2.IMREAD_COLOR)
imgB = cv2.imread('Images/Results Watershed/pcb3missingpinhole.jpg', cv2.IMREAD_COLOR)

# convert both images to grayscale
img1 = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)
dst = bit_xor
denoised = cv2.fastNlMeansDenoising(dst,None,10,7,21)

#cv2.imshow("img1", img1)
#cv2.imshow("img2", img2)
#cv2.imshow("bit_and", bit_and)
#cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
#cv2.imshow("bit_not", bit_not)
#cv2.imshow("bit_not2", bit_not2)
cv2.imshow("denoised", denoised)

cv2.imwrite("xor3_missingpinhole.jpg", denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()
