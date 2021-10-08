import numpy as np
import argparse
import cv2

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))    
    return shifted

def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h //2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w,h))

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    
    else:
        r = width / float(w)
        dim = (width, int(h*r))

    return cv2.resize(image, dim, interpolation=inter)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

shifted = translate(image, 25, 50)
cv2.imshow("Shifted Down and Right", shifted)

cv2.waitKey()

sifted = translate(image, -50, -90)
cv2.imshow("Shifted up and left", shifted)

cv2.waitKey()