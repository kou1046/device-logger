from __future__ import annotations
from dataclasses import dataclass

import numpy as np

from .color_image_cropper import ColorImageCropper
from .near_range_cropper import NearRangeCropper


class NearRangeColorCropper(ColorImageCropper):
    def crop(self, image: np.ndarray, x: int, y: int):
        nearrange_image = NearRangeCropper.crop(image, x, y)
        return super().crop(nearrange_image)
