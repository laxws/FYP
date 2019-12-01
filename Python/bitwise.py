import timeit
bitwise = """
import cv2
import numpy as np

imgA = cv2.imread('Images/Real PCB/pcb.jpg', cv2.IMREAD_COLOR)
imgB = cv2.imread('Images/Real PCB/defect-2.jpg', cv2.IMREAD_COLOR)

grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

retval2,th1 = cv2.threshold(grayA,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
retval2,th2 = cv2.threshold(grayB,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img1 = cv2.fastNlMeansDenoising(th1,None,10,7,21)
img2 = cv2.fastNlMeansDenoising(th2,None,10,7,21)

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)
dst = bit_xor = cv2.bitwise_xor(img1, img2)
denoised = cv2.fastNlMeansDenoising(dst,None,10,7,21)

#cv2.imshow("img1", img1)
#cv2.imshow("img2", img2)
#cv2.imshow("bit_and", bit_and)
#cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
#cv2.imshow("bit_not", bit_not)
#cv2.imshow("bit_not2", bit_not2)
cv2.imshow("denoised", denoised)

#cv2.imwrite("xor_defect-3.jpg", denoised)

#cv2.waitKey(0)
cv2.destroyAllWindows()
"""
elapsed_time = timeit.timeit(bitwise, number=5)/5
print(elapsed_time)
