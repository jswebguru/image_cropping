import cv2
import numpy as np

image = cv2.imread('update.jpg')
font = cv2.FONT_HERSHEY_COMPLEX
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the HSV colorspace
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower = np.array([161, 155, 84], dtype="uint8")
upper = np.array([179, 255, 255], dtype="uint8")
mask = cv2.inRange(hsv, lower, upper)
color_detection = cv2.bitwise_and(image, image, mask=mask)

img_gray = cv2.cvtColor(color_detection, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', img_gray)
cv2.waitKey(0)
# contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
# coordinate_x = 0
# coordinate_y = 0
#
# for cnt in contours:
#     cnt_rect = cv2.boundingRect(cnt)
#     x, y, w, h = cnt_rect
#     if x > coordinate_x:
#         coordinate_x = x
#     if y > coordinate_y:
#         coordinate_y = y

# crop_img = image[100:coordinate_y, 100:coordinate_x]
# print(f'coordinate is {coordinate_x}, {coordinate_y}')
# cv2.imwrite('output.jpg', crop_img)


# Find Canny edges
edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
cv2.waitKey(0)
# cv2.destroyWindow()
#
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=3)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(color_detection, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imshow('Lined image', image)
cv2.waitKey(0)
cv2.destroyWindow()
# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
# contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Showing the final image.
# cv2.imshow('image2', image)
# cv2.waitKey(0)

# print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
#
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
