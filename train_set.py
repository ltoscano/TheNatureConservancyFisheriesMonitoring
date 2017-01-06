# coding:utf-8
import os
import cv2
import numpy as np


def get_train_set():
    train_path = 'train/'
    train_photo_list = list()
    fish_type_list = os.listdir(train_path)
    for item in fish_type_list:
        photo_file_list = os.listdir(train_path + item)
        for photo_item in photo_file_list:
            photo_item_path = train_path + item + '/' + photo_item
            train_photo_list.append(photo_item_path)
    return train_photo_list


if __name__ == '__main__':
    train_set = get_train_set()
    # get size set of photo
    size_list = list()
    print len(train_set)
    for train_item in train_set:
        img = cv2.imread(train_item)
        height, weight = img.shape[:2]
        if [height, weight] not in size_list:
            size_list.append([height, weight])
    print size_list
