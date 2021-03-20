
import cv2


if __name__ == '__main__':
    src_img = cv2.imread('pic3.jpg')
    lab_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2Lab)
    for i in range(1080):
        for j in range(1920):
            l, a, b, = lab_img[i, j]
            l *= 0.5
            lab_img[i, j] = l, a, b
    rgb_img = cv2.cvtColor(lab_img, cv2.COLOR_Lab2BGR)
    hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2HSV)
    #cv2.imshow('ColorRGB', rgb_img)
    for i in range(1080):
        for j in range(1920):
            h, s, v, = hsv_img[i, j]
            s *= 0.5
            hsv_img[i, j] = h, s, v
    rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imshow('ColorRGB', rgb_img)
    cv2.waitKey(0)
