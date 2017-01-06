# coding:utf-8
import os
import cv2
import numpy as np


def get_train_set():
    photo_count = 0

    train_path = 'train/'
    train_size = 'train_size/'
    train_photo_list = list()
    fish_type_list = os.listdir(train_path)
    for item in fish_type_list:
        photo_file_list = os.listdir(train_path + item)
        for photo_item in photo_file_list:
            photo_item_path = train_path + item + '/' + photo_item
            train_photo_list.append(photo_item_path)

            # save photo by size
            img = cv2.imread(photo_item_path)
            height, weight = img.shape[:2]
            size_path = str(height) + str(weight)
            if not os.path.exists(train_size + size_path):
                os.mkdir(train_size + size_path)
            if not os.path.exists(train_size + size_path + '/' + item):
                os.mkdir(train_size + size_path + '/' + item)
            cv2.imwrite(train_size + size_path + '/' + item + '/' + photo_item, img)
            photo_count += 1
            print photo_count

    return train_photo_list


def cluster_by_sift():
    return


if __name__ == '__main__':
    if not os.path.exists('train_size'):
        os.mkdir('train_size')
    train_set = get_train_set()
