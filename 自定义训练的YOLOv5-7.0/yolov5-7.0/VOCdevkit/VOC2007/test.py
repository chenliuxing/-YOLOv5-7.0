import os
import random

# 训练集和验证集的比例分配
trainval_percent = 0.1
train_percent = 0.9

# 标注文件的路径
xmlfilepath = '/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/Annotations'

# 生成的txt文件存放路径
txtsavepath = '/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('/home/cxx/project/yolov5-7.0/VOCdevkit2007/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
