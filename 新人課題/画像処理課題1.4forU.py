import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"/home/nakamura/ドキュメント/新人課題/inu.jpg",0)
surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img, None)

img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()

#hst = cv2.calcHist(r"/home/nakamura/ドキュメント/新人課題/neko.jpg", 0, None, 256, (0, 256))
plt.hist(img.ravel(), 256, [0, 256]); plt.show()

blur = cv2.GaussianBlur(img, (5,5), 0)
can = cv2.Canny(blur, 50, 110)
plt.imshow(can),plt.show()