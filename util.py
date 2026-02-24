# util.py
import numpy as np
import cv2

def get_limits(color):
    """Get HSV lower and upper limits for a given BGR color"""
    
    # Convert BGR to HSV
    color = np.uint8([[color]])  # color is expected in BGR
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)[0][0]
    
    # Define range around the color
    hue = hsv_color[0]
    
    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for red
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for red
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    
    return lowerLimit, upperLimit