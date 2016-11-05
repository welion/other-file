# -*- coding: utf-8 -*-
"""
Created on Sat Nov 05 10:28:32 2016

@author: welion
"""

####################################################
#python enumerate的用法
####################################################
import pandas as pd

list_to_test_enumerate = ['First','Second','Third','Fourth','Fifth']
for index, item in enumerate(list_to_test_enumerate):
    print index, item
    

####################################################
# os.walk 的用法
#os.walk()可以得到一个三元tupple(dirpath, dirnames, filenames)，其中第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
#其中dirpath是一个string，代表目录的路径，dirnames是一个list，包含了dirpath下所有子目录的名字。filenames是一个list，包含了非目录文件的名字。这些名字不包含路径信息，如果需要得到全路径，需要使用os.path.join(dirpath, name).
####################################################    
import os

PATH='E:\Share Floder'

for dirpath, dirname, filenames in os.walk(PATH):
    print "The root dir path is %s." % dirpath
    print "The dir name is %s." % dirname
    print "All the file is...."
    for index, files in enumerate(filenames):
        print index, files
        