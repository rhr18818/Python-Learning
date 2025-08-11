import cv2
import numpy as np

img = cv2.imread('demo.jpg')
cv2.imshow("image",img)
cv2.waitKey(0)
print(img.shape[:2])

H ,W = img.shape[:2]
new_H,new_W = H//4,W//4;
new_img = np.zeros((new_H,new_W,3),dtype=np.uint8)
print(new_img.shape)

# img = img/255

print(type(img))

for i in range(0,H,4):
    for j in range(0,W,4):
        block = img[i:i+4,j:j+4]
        avg = block.mean(axis=(0,1))
        new_img[i//4,j//4] = avg


cv2.imshow("New Image",new_img)
cv2.waitKey(0)


# count =0
# # for i in img:
# #     count= count +1
# #     if count == 2:
# #         break
# #     for elm in i:
# #         print(elm)
# # cv2.imshow("image",img)
# # cv2.waitKey(0)
# print(count)