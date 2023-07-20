from __future__ import annotations

import numpy as np
import cv2

from .image_cropper import ImageCropper


class ColorImageCropper(ImageCropper):
    def __init__(self, rgb: list[int], threshold: int):
        self.rgb = np.array(rgb)
        self.threshold = threshold

    def crop(self, image: np.ndarray) -> np.ndarray | None:
        mask_image = cv2.inRange(image, self.min_rgb, self.max_rgb)
        target_ys, target_xs = np.where(mask_image == 255)

        if not len(target_xs):
            return None

        return image[
            target_ys.min() : target_ys.max(), target_xs.min() : target_xs.max()
        ]

    @property
    def min_rgb(self):
        return self.rgb - self.threshold

    @property
    def max_rgb(self):
        return self.rgb + self.threshold
