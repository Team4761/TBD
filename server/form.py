"""
form.py is dedicated to defining different utilities for resolving data
from an image.
"""

import vision
import math
import cv2 as cv2

class Form():
    pass

"""
Field(x1,y1,x2,y2)
int x1	=	the x coordinate of the top left corner in the image of the Field box.
int y1  =	the y coordinate of the top left corner
int x2  =	the x coordinate of the bottom right corner of the image.
int y2	=	the y coordinate of the bottom right corner.
"""
class Field(object):
    def __init__(self, x1, y1, x2, y2): # x1 and y1 is the coordinate pair for the top left corner in pixels.
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

"""
MultiField(x1,y1,x2,y2,number
x1, y1, x2, y2 are the same as super Field.
int number =	the number of options in the field.
"""
class MultiField(Field):
    def __init__(self, x1, y1, x2, y2, number):
        super(MultiField, self).__init__(x1, y1, x2, y2)
        self.number = number
    """
    int MultiField.evaluate(image)
    image =     The image to search and evalute the answer to the field.
    This method will return which bubble left to right is the most full and selected. It is zero indexed.
    """
    def evaluate(self, image):
        box_width = int((self.x2-self.x1)/self.number)
        max_fullness = 0 # The current maximum fullness in percent.
        n = 0 # The field number that has the maximum fullness.
        for i in range(0, self.number):
            left_x = self.x1 + box_width * i
            right_x = self.x1 + box_width * (i+1)
            box = image[self.y1:self.y2, left_x:right_x] # NOTE: It's always y and then x when splicing with numpy for some reason.
            box_percent = vision.get_fullness_percent(box)
            if box_percent > max_fullness:
                n = i
                max_fullness = box_percent
        return n

class Alpha(Form): # The first form
    fields = {

    }
