# -*- coding:utf-8 -*-
import cv2

cap = cv2.VideoCapture(0) 	# 初始化摄像头
img = cap.read()			# 获取摄像头内容
cv2.imwrite("photo.png", img[0])	 # 将内容写到文件