# coding:utf-8
import cv2
import numpy as np
import train_set


def get_sift_feature(gray):
    # sift = cv2.SIFT()
    sift = cv2.SURF()
    kp = sift.detect(gray, None)
    return kp


if __name__ == '__main__':
    photo_list = train_set.get_train_set()
    for item in photo_list:
        img = cv2.imread(item)
        gray_photo = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        photo_kp = get_sift_feature(gray_photo)
        img_with_kp = cv2.drawKeypoints(gray_photo, photo_kp)
