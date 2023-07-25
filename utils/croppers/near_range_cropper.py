from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RangePoint:
    WIDTH: ClassVar[int] = 1920
    HEIGHT: ClassVar[int] = 1280
    x: int
    y: int

    def __post_init__(self):
        if self.x < 0:
            object.__setattr__(self, "x", 0)
        if self.y < 0:
            object.__setattr__(self, "y", 0)
        if self.x > self.WIDTH:
            object.__setattr__(self, "x", self.WIDTH)
        if self.y > self.HEIGHT:
            object.__setattr__(self, "y", self.HEIGHT)

    def __sub__(self, other: RangePoint):
        return RangePoint(self.x - other.x, self.y - other.y)

    def __add__(self, other: RangePoint):
        return RangePoint(self.x + other.x, self.y + other.y)


class NearRangeCropper:
    """
    周辺の画像を切り抜く役割を果たす．

    """

    MERGIN_WIDTH_PIXEL = RangePoint.WIDTH // 4
    MARGIN_HEIGHT_PIXEL = 100

    @classmethod
    def _calculate_near_range(cls, x, y):
        point = RangePoint(x, y)
        mergin_point = RangePoint(cls.MERGIN_WIDTH_PIXEL, cls.MARGIN_HEIGHT_PIXEL)
        max_range = point + mergin_point
        min_range = point - mergin_point
        return min_range.x, min_range.y, max_range.x, max_range.y

    @classmethod
    def crop(cls, image: np.ndarray, x: int, y: int):
        min_x, min_y, max_x, max_y = cls._calculate_near_range(x, y)
        cropped_image = image[min_y:max_y, min_x:max_x]
        return cropped_image
