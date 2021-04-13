import cv2
from matplotlib import pyplot as plt
import numpy as np

img1 = cv2.imread(r"/home/nakamura/ドキュメント/新人課題/machigai1.1.jpg",1)
img2 = cv2.imread(r"/home/nakamura/ドキュメント/新人課題/machigai2.1.jpg",1)
temp = img2.copy()

gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img_dif = cv2.absdiff(gray_img1, gray_img2)

#ret, img_bin = cv2.threshold(img_dif, 50, 255, 0)

#cv2.imshow("img_dif", img_dif)
#while True:
    #if cv2.waitKey(10) == 27:
        #break
#cv2.destroyAllWindows()

im_list = np.asarray(img_dif)
plt.imshow(im_list)
plt.show()
