import numpy
import cv2
import time

"""
Take A Photo

This script uses OpenCV to take a picture
from a webcam or USB camera device.
"""

camera_port = 0
camera = cv2.VideoCapture(camera_port)

# Wait, otherwise the image will be over-dark
time.sleep(0.1)
return_value, image = camera.read()
cv2.imwrite("opencv.png", image) # image is a numpy.ndarray

image = image/255.0

del(camera)
time.sleep(30)

