from __future__ import annotations

from PIL import ImageGrab
import cv2
import numpy as np
from drags import DragLogger
from drags.drag import Click

from croppers import NearRangeColorCropper


def on_press(click: Click):
    x, y = click.xy()
    thresh = 5
    rgb = [51, 204, 255]

    cropper = NearRangeColorCropper(rgb, thresh)
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2RGB)
    cusor_nearrange_screen = cropper.crop(screenshot, x, y)

    print(cusor_nearrange_screen)

    if cusor_nearrange_screen is None:
        return

    cv2.imwrite("sample.png", cusor_nearrange_screen)


if __name__ == "__main__":
    with DragLogger(on_press=on_press) as logger:
        logger.join()
        logger.stop()
