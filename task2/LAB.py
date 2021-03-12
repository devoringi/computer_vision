
import cv2


if __name__ == '__main__':
    src_img = cv2.imread('pic.jpg')
    lab_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2Lab)
    for i in range(1080):
        for j in range(1920):
            l, a, b, = lab_img[i, j]
            l *= 0.5
            lab_img[i, j] = l, a, b
    rgb_img = cv2.cvtColor(lab_img, cv2.COLOR_Lab2BGR)
    cv2.imshow('ColorRGB', rgb_img)
    cv2.waitKey(0)
