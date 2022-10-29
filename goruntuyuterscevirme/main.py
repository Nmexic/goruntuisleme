import cv2
import numpy as np

minyon_gri=cv2.imread("minion.png",0)
cv2.imshow("minion.png",minyon_gri)

im = np.array(minyon_gri)

mask = np.full(im.shape,255)

mod_img = mask - im
mod_img = mod_img.astype(np.uint8)

cv2.imshow("inverted",mod_img)

cv2.waitKey()