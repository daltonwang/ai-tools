# -*- coding: utf-8 -*-
#!/usr/bin/env python3

'''
Divide face accordance CelebA Attr type.
https://zhuanlan.zhihu.com/p/35975956

该脚本可以自动根据属性Attr_type自行划分CelebA数据集，分别划分到trainA和trainB文件夹，
trainA表示有该属性的数据，
trainB表示无该属性的数据，
同时其也可以在完成划分时自动报告trainA、trainB以及无该图像的数量。
使用时，需要根据实际情况，调整output_path、image_path、CelebA_Attr_file及Attr_type，注意Attr_type即是你所要得到的属性划分数据集标记，其值范围为1到40，其含义如上文所述！


'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import os

output_path = "/home/andy/datasets/CelebA/"
image_path = "/home/andy/datasets/CelebA/img_align_celeba_160x160"
CelebA_Attr_file = "/home/andy/datasets/CelebA/list_attr_celeba.txt"
Attr_type = 16 # Eyeglasses

def main():
    '''Divide face accordance CelebA Attr eyeglasses label.'''
    trainA_dir = os.path.join(output_path, "trainA")
    trainB_dir = os.path.join(output_path, "trainB")
    if not os.path.isdir(trainA_dir):
        os.makedirs(trainA_dir)
    if not os.path.isdir(trainB_dir):
        os.makedirs(trainB_dir)

    not_found_txt = open(os.path.join(output_path, "not_found_img.txt"), "w")
    
    count_A = 0
    count_B = 0
    count_N = 0

    with open(CelebA_Attr_file, "r") as Attr_file:
        Attr_info = Attr_file.readlines()
        Attr_info = Attr_info[2:]
        index = 0
        for line in Attr_info:
            index += 1
            info = line.split()
            filename = info[0]
            filepath_old = os.path.join(image_path, filename)
            if os.path.isfile(filepath_old):
                if int(info[Attr_type]) == 1:
                    filepath_new = os.path.join(trainA_dir, filename)
                    shutil.copyfile(filepath_old, filepath_new)
                    count_A += 1
                else:
                    filepath_new = os.path.join(trainB_dir, filename)
                    shutil.copyfile(filepath_old, filepath_new)
                    count_B += 1
                print("%d: success for copy %s -> %s" % (index, info[Attr_type], filepath_new))
            else:
                print("%d: not found %s\n" % (index, filepath_old))
                not_found_txt.write(line)
                count_N += 1

    not_found_txt.close()
    
    print("TrainA have %d images!" % count_A)
    print("TrainB have %d images!" % count_B)
    print("Not found %d images!" % count_N)

if __name__ == "__main__":
    main()