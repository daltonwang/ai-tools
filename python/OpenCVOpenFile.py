# 目标：
# 1. 如何打开视频文件，获取视频文件相关参数
# 2. 如何抽帧，并对该帧调用相关的opencv算法


import os
import sys

import cv2 as cv
import numpy as np


if __name__ == '__main__':

    file_path = "../data/mp4/"
    file_name = "001.MOV"

    # Open a video file or an image file or a camera stream
    cap = cv.VideoCapture(file_path+file_name)
    padding = 20

    # You can get video informations with GET Method
    width       = int(round(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
    height      = int(round(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    fps         = int(round(cap.get(cv.CAP_PROP_FPS)))
    videoformat = int(round(cap.get(cv.CAP_PROP_FORMAT)))

    print("-------video information------")
    print("video name:"+file_path+file_name)
    print("video width:" + str(width))
    print("video height:" + str(height))
    print("video fps：" + str(fps))
    print("video format：" + str(videoformat))
    print("------------------------------")
    k = np.ones((5, 5), np.uint8)

    while(True):
        # 读取一帧，read()方法是其他两个类方法的结合，具体文档
        # ret为bool类型，指示是否成功读取这一帧
        ret, frame = cap.read()
        # 就是个处理一帧的例子，这里转为灰度图
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #
        # img = cv.erode(frame, k, iterations=2)
        # img = cv.dilate(frame, k, iterations=2)

        # 图像边缘检测
        img = cv.Canny(frame, 100, 200)
        # img = cv.pyrDown(frame)

        # 不断显示一帧，就成视频了
        # 这里没有提前创建窗口，所以默认创建的窗口不可调整大小
        # 可提前使用cv.WINDOW_NORMAL标签创建个窗口
        cv.imshow('frame',img)
        # 若没有按下q键，则每1毫秒显示一帧
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()