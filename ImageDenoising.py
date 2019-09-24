import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('noise.jpg')
dst = cv2.fastNlMeansDenoising(img,None,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst)
plt.title("Denoised")
plt.xticks([]), plt.yticks([])
plt.show()

'''
cv2.imshow("Denoised", dstA)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


