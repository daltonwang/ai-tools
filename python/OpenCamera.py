# 目标：
# 1. 如何打开视频文件，获取视频文件相关参数
# 2. 如何抽帧，并对该帧调用相关的opencv算法


import os
import sys

import cv2 as cv
import numpy as np


if __name__ == '__main__':

    # Open a video from camera
    cap = cv.VideoCapture(0)

    # You can get video informations with GET Method
    width       = int(round(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
    height      = int(round(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    fps         = int(round(cap.get(cv.CAP_PROP_FPS)))
    videoformat = int(round(cap.get(cv.CAP_PROP_FORMAT)))

    print("-------video information------")
    print("video name: Default Camera")
    print("video width:" + str(width))
    print("video height:" + str(height))
    print("video fps：" + str(fps))
    print("video format：" + str(videoformat))
    print("------------------------------")

    while(True):
        # 读取一帧，read()方法是其他两个类方法的结合，具体文档
        # ret为bool类型，指示是否成功读取这一帧
        ret, frame = cap.read()
        cv.imshow('frame',frame)
        # 若没有按下q键，则每1毫秒显示一帧
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()