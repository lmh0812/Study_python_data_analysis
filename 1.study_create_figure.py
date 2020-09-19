import cv2
import numpy as np

image = np.full((512, 512, 3), 255, np.uint8) # numpy를 이용해서 (x,y,색상3개)이렇게 만듦

image = cv2.line(image, (255,255),(300,300), (0,0,255), 3)

image = cv2.rectangle(image, (0,0), (255, 255), (255,0,0), 3) # rectangle(image_src, 사각형 좌측상단 좌표, 사각형 우측하단 좌표, 색깔, 두께) 두께가 -1이면 꽉채워짐

image = cv2.circle(image, (300, 300), 30, (0,255,0), -1) # 원그리기

point = np.array([[5, 5], [128, 258], [483,444], [400, 150]])
image = cv2.polylines(image, [point], True, (100,100,100), 1) # 다각형 그리기

image = cv2.putText(image, "Hello world", (100,300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0,39,49)) # text 그리기 putText(img_src, 글자, 위치, 글자폰트, 글자스케일(크기), 색깔)

cv2.imshow("image", image)
cv2.waitKey(0)