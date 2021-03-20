
import cv2
import numpy as np
from PIL import Image, ImageCms


if __name__ == '__main__':
    #hustogram
    img = cv2.imread('pic.jpg', 0)
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))  # stacking images side-by-side
    cv2.imwrite('histogram.png', res)
    #gauss blur
    img2 = cv2.imread('pic.jpg')
    dst = cv2.GaussianBlur(img2, (101, 101), cv2.BORDER_DEFAULT)
    res = np.hstack((img2, dst))  # stacking images side-by-side
    cv2.imwrite('gaussian_blur.png', res)
    #sobel filtr
    img3 = cv2.imread('pic.jpg')
    sob = cv2.Sobel(img3,cv2.CV_64F,0,1,ksize=5)
    res = np.hstack((img2, sob))  # stacking images side-by-side
    cv2.imwrite('sobel.png', res)
    #laplas filtr
    img4 = cv2.imread('pic.jpg')
    s = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(s, cv2.CV_16S, ksize=3)
    res = np.hstack((s, lap))  # stacking images side-by-side
    cv2.imwrite('laplas.png', res)
    cv2.waitKey(0)
