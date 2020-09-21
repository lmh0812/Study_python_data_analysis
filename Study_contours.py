# import cv2
# import numpy as np

# image = cv2.imread("C:/Users/User/Desktop/private/Practice_code/test2.jpg", cv2.IMREAD_GRAYSCALE)

# ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("image", thresh)
# cv2.waitKey(0)

# contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# image = cv2.drawContours(image, contours, -1, (0,0,255), 3)
# cv2.imshow("contours", image)
# cv2.waitKey(0)

import cv2

img = cv2.imread('C:/Users/User/Desktop/private/Practice_code/images/test2.jpg') # 이미지를 그냥 불러오고 cv2.cvtColor()함수 이용해서 변환


imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지를 그레이 칼로 변환 이렇게 해야 Contours할 때 색상이 입혀짐
ret, thr = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY) # 임계값 지정 127이상을 255로 만듦


countors, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 윤곽을 찾아줌
cv2.drawContours(img, countors, -1, (0, 255, 0), 1) # 윤곽을 그림 (img = contours를 나타낼 대상 이미지)

cv2.imshow('thr', thr)
cv2.imshow('contours', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

