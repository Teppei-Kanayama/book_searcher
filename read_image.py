#coding: utf-8

import numpy as np
import cv2

img = cv2.imread('./images/0.jpg', 1)

print(img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
