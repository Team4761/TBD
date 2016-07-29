import cv2
import unittest

from server.vision import get_fullness_percent

class TestMiscVisionStuff(unittest.TestCase):
    def test_get_fullness_percent(self):
        image = cv2.imread('tests/resources/half_n_half.png')
        self.assertEqual(get_fullness_percent(image), 0.5)

if __name__ == '__main__':
    unittest.main()
