from __future__ import annotations
from abc import abstractmethod, ABCMeta

import numpy as np


class ImageCropper(metaclass=ABCMeta):
    @abstractmethod
    def crop(image: np.ndarray) -> np.ndarray | None:
        ...
