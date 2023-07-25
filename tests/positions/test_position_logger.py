from __future__ import annotations
import sys
import unittest

import pyautogui

sys.path.append(".")
from mouse.positions import PositionLogger, MousePos


class PositionLoggerTest(unittest.TestCase):
    def test_pos_log(self):
        actual_mouse_pos: MousePos | None = None

        def _test_pos_log(pos: MousePos):
            nonlocal actual_mouse_pos
            actual_mouse_pos = pos

        expected = (200, 400)
        with PositionLogger(_test_pos_log):
            pyautogui.moveTo(expected)

        self.assertEqual((actual_mouse_pos.x, actual_mouse_pos.y), expected)


if __name__ == "__main__":
    unittest.main()
