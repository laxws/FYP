# load image from dataset
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('pcb1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('pcb2_pinhole.jpg', cv2.IMREAD_COLOR)

# convert both images to grayscale
grayA = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

bit_and = cv2.bitwise_and(grayB, grayA)
bit_or = cv2.bitwise_or(grayB, grayA)
bit_xor = cv2.bitwise_xor(grayA, grayB)
bit_not = cv2.bitwise_not(grayA)
bit_not2 = cv2.bitwise_not(grayB)

cv2.imshow("grayA", grayA)
cv2.imshow("grayB", grayB)
cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_not2", bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()
