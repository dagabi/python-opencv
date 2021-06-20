# import the necessary packages
import imutils
import cv2

base = "countBlocks\\..\\"
picPath = base + "gabmic.jpg"

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(picPath)
cv2.imshow("Image", image)
cv2.waitKey(0)
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# applying edge detection we can find the outlines of objects in
# images
#edged = cv2.Canny(gray, 30, 150)
#cv2.imshow("Edged", edged)
#cv2.waitKey(0)


# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# we apply erosions to reduce the size of foreground objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=10)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)


# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
"""cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)"""