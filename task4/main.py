import cv2
import numpy as np

img1 = cv2.imread("ball1.png")
img1 = cv2.resize(img1, (1000, 1000))
img2 = cv2.imread("ball2.jpg")
img2 = cv2.resize(img2, (1000, 1000))



layer = img1.copy()
gaussian_pyramid = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)


layer = gaussian_pyramid[5]
laplacian_pyramid = [layer]
for i in range(5, 0, -1):
    size = (gaussian_pyramid[i-1].shape[1], gaussian_pyramid[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)


layer = img2.copy()
gaussian_pyramid2 = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid2.append(layer)


layer = gaussian_pyramid2[5]
laplacian_pyramid2 = [layer]
for i in range(5, 0, -1):
    size = (gaussian_pyramid2[i-1].shape[1], gaussian_pyramid2[i-1].shape[0])
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid2[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid2[i-1], gaussian_expanded)
    laplacian_pyramid2.append(laplacian)


res_pyramid = []
n = 0
for img1_lap, img2_lap in zip(laplacian_pyramid, laplacian_pyramid2):
    n += 1
    cols, rows, ch = img1_lap.shape
    laplacian = np.hstack((img1_lap[:, 0:int(cols/2)], img2_lap[:, int(cols/2):]))
    res_pyramid.append(laplacian)


res_reconstructed = res_pyramid[0]
for i in range(1, 5):
    size = (res_pyramid[i].shape[1], res_pyramid[i].shape[0])
    res_reconstructed = cv2.pyrUp(res_reconstructed, dstsize=size)
    res_reconstructed = cv2.add(res_pyramid[i], res_reconstructed)

cv2.imshow("", res_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()