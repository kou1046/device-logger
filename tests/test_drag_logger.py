from __future__ import annotations
import sys

sys.path.append(".")
from drags import Drag, DragLogger
from drags.drag import Click
import unittest

import pyautogui


class DragLoggerTest(unittest.TestCase):
    def test_press(self):
        result: None | tuple = None

        def _test_press(click: Click):
            nonlocal result
            result = click.xy()

        logger = DragLogger(on_press=_test_press)
        logger.start()
        expected = (200, 500)
        pyautogui.click(*expected)

        self.assertEqual(expected, result)

    def test_drag(self):
        actual_click_pos: None | tuple = None
        actual_release_pos: None | tuple = None

        def _test_drag(drag: Drag):
            nonlocal actual_click_pos, actual_release_pos
            actual_click_pos = drag.click.xy()
            actual_release_pos = drag.release.xy()

        logger = DragLogger(on_drag=_test_drag)
        logger.start()
        expected_click_pos = (300, 400)
        delta_pos = (100, 50)

        pyautogui.moveTo(expected_click_pos)
        pyautogui.drag(*delta_pos)

        expected_release_pos = (
            expected_click_pos[0] + delta_pos[0],
            expected_click_pos[1] + delta_pos[1],
        )

        self.assertEqual(actual_click_pos, expected_click_pos)
        self.assertEqual(actual_release_pos, expected_release_pos)


if __name__ == "__main__":
    unittest.main()
