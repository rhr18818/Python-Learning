import cv2
import numpy as np

img = cv2.imread('demo.jpg')
cv2.imshow("Original Image",img)
cv2.waitKey(0)


H,W = img.shape[:2]
new_H , new_W = H//4,W//4
new_img = np.zeros((new_H,new_W,3),dtype=np.uint8)

for i in range(0,H,4):
    for j in range(0,W,4):
        block = img[i:i+4,j:j+4]
        avg = block.mean(axis=(0,1))
        new_img[i//4][j//4]= avg


cv2.imshow("4 Time Smaller Image",new_img)
cv2.waitKey(0)