
import cv2
import numpy as np
from PIL import Image, ImageCms


if __name__ == '__main__':
    #histogram
    img = cv2.imread('pic.jpg', 0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('histogram.png', res)

    #use CLAHE
    bgr = cv2.imread('pic.jpg')
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    lab_planes = cv2.split(lab)
    clahe = cv2.createCLAHE()
    lab_planes[0] = clahe.apply(lab_planes[0])
    lab = cv2.merge(lab_planes)
    cv2.waitKey(0)
    bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    cv2.imshow('hist', bgr)
    cv2.waitKey(0)

    #gauss blur

    dst = cv2.GaussianBlur(bgr, (101, 101), cv2.BORDER_DEFAULT)
    res = np.hstack((bgr, dst))  # stacking images side-by-side
    cv2.imwrite('gaussian_blur.png', res)
    #sobel filtr
    sob = cv2.Sobel(bgr,cv2.CV_64F,0,1,ksize=5)
    res = np.hstack((bgr, sob))  # stacking images side-by-side
    cv2.imwrite('sobel.png', res)
    #laplas filtr
    s = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(s, cv2.CV_16S, ksize=3)
    res = np.hstack((s, lap))  # stacking images side-by-side
    cv2.imwrite('laplas.png', res)