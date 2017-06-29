#-*- coding:utf-8 -*-
import cv2 as cv

img = cv.imread("./test.jpg")    # 读取图片
cv.imshow("picture title",img)  # 显示图片

cv. waitKey(3000)       # 图片显示时长
cv.destroyAllWindows()  # 关闭显示窗口,图片显示不用也可以
