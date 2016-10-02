"""
form.py is dedicated to defining different utilities for resolving data
from an image.
"""

import vision
import math
import cv2 as cv2

class Form():
    pass

class Field():
    def __init__(self, x1, y1, x2, y2): # x1 and y1 is the coordinate pair for the top left corner in percent.
        # x2 and y2 are the coordinate pair of the bottom left corner.
        self.x1, self.y1 = int(x1), int(y1)
        self.x2, self.y2 = int(x2), int(y2)
    def evaluate(self, image): # Override me!
        raise Exception("Evaluate method needs to be overriden.")

class BooleanField(Field):
    def evaluate(self, image): # This assumes each box is 1/2 horizontal space.
        box1_x2 = int((self.x2-self.x1)/2+self.x1) # The first box ends halfway through the image.
        box1 = image[self.y1:self.y2, self.x1:box1_x2]
        box2 = image[self.y1:self.y2, box1_x2:self.x2]
        box1_percent = vision.get_fullness_percent(box1)
        box2_percent = vision.get_fullness_percent(box2)
        if box1_percent > box2_percent:
            return True # The first box always evaluates as true.
        else:
            return False

class Alpha(Form): # The first form
    fields = {

    }
