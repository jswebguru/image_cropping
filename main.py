import os
import cv2
import datetime
from settings import INPUT_PATH, OUTPUT_PATH


for image_file in os.listdir(INPUT_PATH):

    # Read the image file
    img_file = os.path.join(INPUT_PATH, image_file)
    image = cv2.imread(img_file)

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get binary image from the grayscale one
    _, binary = cv2.threshold(img_gray, 225, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the image
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        cnt_rect = cv2.boundingRect(cnt)
        x, y, w, h = cnt_rect

        if h > 50:
            # Detect the strike out part in the image
            # img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

            # Crop the strike out part in the image
            crop_img = image[y:(y + 10 + h), x:(x + 10 + w)]
            img_name = f"{datetime.datetime.now().isoformat().replace(':', '-')}.jpg"
            output = os.path.join(OUTPUT_PATH, img_name)
            cv2.imwrite(output, crop_img)
