import tensorflow as tf
import cv2
import numpy as np
print(f"TensorFlow version: {tf.__version__}")

# camera preview

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first img
    rval, img = vc.read()
else:
    rval = False

while rval:

    cv2.imshow("preview", img)
    rval, img = vc.read()

    # resize function
    # w.i.p

    scale_percent = 25
    img_r_x = int(img.shape[1] * scale_percent / 100)
    img_r_y = int(img.shape[0] * scale_percent / 100)

    img = cv2.resize(img, (img_r_x, img_r_y), interpolation=cv2.INTER_AREA)

    img_y, img_x, img_channels = img.shape

    # flip camera feed
    img = cv2.flip(img, 1)

    # convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img ocr
    cv2.putText(img, "DAPPER HANDSHAKE", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 1)
    cv2.putText(img, f"Resolution: {img_x}, {img_y}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 1)

    # exit app on ESC
    key = cv2.waitKey(20)
    if key == 27:
        break

vc.release()
cv2.destroyWindow("preview")