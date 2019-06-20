import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt


def plt_img(img):
    '''
    Quick visualisation of the checked fields.
    '''
    plt.figure(figsize=(30, 30))
    plt.imshow(img, 'gray')
    plt.show()


def im_threshold(img):
    '''
    Thresholds values of light grey to white. Inverts colours to black page w/ white writing.
    '''
    # Thresholds light greys to white, and inverses the page to black.
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
    # img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    #         cv2.THRESH_BINARY,11,2)
    return thresh


def check_find(img, threshhold, mark_thresh, check_type):
    '''
    Returns an image labelled with all relevant checks.
    '''

    if cv2.getVersionMajor() in [2, 4]:
        contours, _ = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, _ = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_TRIPLEX
    document_height, document_width = img.shape[0], img.shape[1]
    mark_thresh = float(mark_thresh.strip('%')) / 100.0

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.1*cv2.arcLength(cnt, True), True)
        coords = approx.ravel()

        # If quadrilateral
        if len(approx) == 4:
            x, y, x2, y2 = coords[0], coords[1], coords[4], coords[5]
            feature_height, feature_width = (y2 - y), (x2 - x)
            # If the size of the quadrilateral found is significant (e.g. not hidden inside text)
            if feature_width > float(document_width)/100 and feature_height > float(document_width)/100:
                # If a square (± 5 pixels)
                if abs(feature_height - feature_width) < 5:
                    crop_img = img[y: y + feature_height, x: x + feature_width]
                    # Thresholds the image to binary black and white
                    _, crop_thresh = cv2.threshold(
                        crop_img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                    total = crop_img.shape[0] * crop_img.shape[1]
                    count_black = total - cv2.countNonZero(crop_thresh)
                    if count_black > float(total)*mark_thresh and (check_type == "filled" or check_type == "all"):
                        cv2.drawContours(img, [approx], 0, (0), 2)
                        cv2.putText(img, "Filled", (x, y), font, 1, (0))
                    elif check_type == "empty" or check_type == "all":
                        cv2.drawContours(img, [approx], 0, (0), 2)
                        cv2.putText(img, "Empty", (x, y), font, 0.5, (0))

        if len(approx) > 15:
            # TODO: Do something here if looking for radio buttons.
            continue
    return(img)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise ValueError(
            'Expected 3 arguments: an image directory, check type and a threshold percentage for classifying a shape as checked.')
    try:
        img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
    except cv2.error as e:
        print("Error reading image from directory provided.")
    check_type = sys.argv[2]
    mark_thresh = str(sys.argv[3])
    threshold = im_threshold(img)
    img = check_find(img, threshold, mark_thresh, check_type)
    # Plot image and save to file.
    plt_img(img)
    cv2.imwrite('edited.png', img)
