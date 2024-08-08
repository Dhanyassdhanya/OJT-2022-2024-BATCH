import cv2
import numpy as np

# read the image with the particular library which we have imported
image = cv2.imread('test.jpg')

if image is None:
    print ("Could not read the image")
    exit()

# cv2.imshow("original image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # convert to grayscale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("grayscale image",grey_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# WE APPLY A GAUSSIAN bLUR INTO THE ABOVE IMAGE
blurred_image = cv2.GaussianBlur(grey_image,(5,5),0)
# cv2.imshow('Blur image',blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# edge detection by using canny in cv2
edges = cv2.Canny(blurred_image,50,150)

# original Image
cv2.imshow("original image",image)
cv2.waitKey(0)

cv2.imshow("Greyscale image",grey_image)
cv2.waitKey(0)

cv2.imshow("Blurred image",blurred_image)
cv2.waitKey(0)

cv2.imshow("Edge",edges)
cv2.waitKey(0)

cv2.destroyAllWindows()