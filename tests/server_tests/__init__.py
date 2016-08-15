import cv2
import sys
import unittest

import server

class TestScanner(unittest.TestCase):
    def test_result_shape(self):
        '''checks that the corrected image has the correct ratio. This is, of
        course, US-Letter. Screw the rest of the world and their commie A4
        paper. MURICA!'''
        image = cv2.imread('tests/resources/some_paper.jpg')
        corrected = server.scan.correct_image(image)
        corrected_shape = corrected.shape
        corrected_ratio = float(corrected_shape[0]) / float(corrected_shape[1])
        self.assertEqual(corrected_ratio, 11 / 8.5)