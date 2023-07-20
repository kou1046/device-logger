import unittest
import os
import sys

sys.path.append(".")

import cv2

from croppers import ColorImageCropper

TEST_YELLOR_RGB = [51, 204, 255]
THRESHOLD = 5


class CropperTest(unittest.TestCase):
    def test_color_crop(self):
        cropper = ColorImageCropper(TEST_YELLOR_RGB, THRESHOLD)
        test1_img = cv2.imread(os.path.join(os.path.dirname(__file__), "test1.png"))
        test2_img = cv2.imread(os.path.join(os.path.dirname(__file__), "test2.png"))

        result1 = cropper.crop(test1_img)
        result2 = cropper.crop(test2_img) is not None

        expected1 = None
        expected2 = True

        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)


if __name__ == "__main__":
    unittest.main()
