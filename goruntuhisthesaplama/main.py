import cv2
import numpy as np

minyon=cv2.imread("minion.png")
cv2.imshow("minion.png",minyon)

minyon_gri=cv2.imread("minion.png",0)
cv2.imshow("minion.png",minyon_gri)

histBoyut=256
histAralık=(0,256)

Hist = np.zeros(256)
[w,h]=minyon_gri.shape

for u in range (0,w):
    for v in range (0,h):
        piksel=minyon_gri[u,v]
        Hist[piksel]+=1

cv2.waitKey()
