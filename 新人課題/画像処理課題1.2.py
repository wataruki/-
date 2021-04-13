import cv2
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r"/home/nakamura/ドキュメント/新人課題/neko.jpg",1)
img2 = Image.open(r"/home/nakamura/ドキュメント/新人課題/neko.jpg")
im_list = np.asarray(img2)
plt.imshow(im_list)
plt.show()
#cv2.imshow("neko",img)
#while True:
    #if cv2.waitKey(10) == 27:
        #break
#cv2.destroyAllWindows()
image_path = "/home/nakamura/ドキュメント/新人課題/"
width = img.shape[1]
height = img.shape[0]

minim = cv2.resize(img,(int(width*0.5), int(height*0.5)))
cv2.imwrite(image_path+"smallneko.jpg",minim)

maxim = cv2.resize(img,(int(width*2), int(height*2)))
cv2.imwrite(image_path+"bigneko.jpg",maxim)

width = img.shape[1]
height = img.shape[0]
center = (int(width/2), int(height/2))
angle = 90.0
scale = 1.0
trans = cv2.getRotationMatrix2D(center, angle, scale)
image2 = cv2.warpAffine(img, trans, (width,height))
cv2.imwrite(image_path+"yokoneko.jpg",image2)

gry = cv2.imread(r"/home/nakamura/ドキュメント/新人課題/neko.jpg",0)
cv2.imwrite(image_path+"grayneko.jpg",gry)