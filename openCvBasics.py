import numpy as np
import imutils
import cv2

image = cv2.imread("gabmic.jpg")
(h, w, d) = image.shape
print(f"image dimentions: h: {h}, w: {w}, d: {d}")

cv2.imshow("GabMic", image)

#resize the image
resized = imutils.resize(image, width=350)
(newH, newW, newD) = resized.shape
cv2.imshow("resized", resized)

#rotate the image
rotated = imutils.rotate_bound(resized, -45)
cv2.imshow("Rotate", rotated)

#blur image
blurred = cv2.GaussianBlur(resized, (25,25), 0)
cv2.imshow("Blurred", blurred)


cv2.waitKey(0)