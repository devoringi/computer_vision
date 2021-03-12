
import cv2
import numpy as np
from PIL import Image, ImageCms

def alphaPic(im):
    #im.convert('RGB')
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            r, g, b, = pixels[i, j]
            if (r ==255 and g ==255 and b == 255):
                r = 0
                g = 0
                b = 0
            else:
                r = 255
                g = 255
                b = 255
            pixels[i, j] = r, g, b
    im.save("alpha.png")

if __name__ == '__main__':
    foreground = cv2.imread("cat2.png")
    background = cv2.imread("background.jpg")
    background2 = Image.open('cat2.png').convert('RGB')
    #alpha = alphaPic(background2)
    alphaPic(background2)
    alpha = cv2.imread("alpha.png")

    # Convert uint8 to float
    foreground = foreground.astype(float)
    background = background.astype(float)

    # Normalize the alpha mask to keep intensity between 0 and 1
    alpha = alpha.astype(float) / 255

    # Multiply the foreground with the alpha matte
    foreground = cv2.multiply(alpha, foreground)

    # Multiply the background with ( 1 - alpha )
    background = cv2.multiply(1.0 - alpha, background)

    # Add the masked foreground and background.
    outImage = cv2.add(foreground, background)

    # Display image
    cv2.imshow("outImg", outImage/255)
    cv2.waitKey(0)