import cv2
import numpy as np

minyon_gri=cv2.imread("minion.png",0)
cv2.imshow("normal",minyon_gri)

im = np.max(minyon_gri)

w,h = minyon_gri.shape

for i in range(0,w):
    for j in range(0,h):
        piksel=im-minyon_gri[i,j]
        minyon_gri[i,j]=piksel

cv2.imshow("inverted",minyon_gri)
cv2.waitKey()