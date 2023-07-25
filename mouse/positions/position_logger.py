from __future__ import annotations
from typing import Callable, Any
from threading import Thread
import datetime

import pyautogui

from .mouse_pos import MousePos


class PositionLogger:
    def __init__(self, callback: Callable[[MousePos], Any] | None = None):
        self.listner = Thread(target=self._create_mouse_pos)
        self.callback = callback
        self.is_alive = False

    def _create_mouse_pos(self):
        while True:
            x, y = pyautogui.position()
            mouse_pos = MousePos(datetime.datetime.now().time(), x, y)
            if self.callback is not None:
                self.callback(mouse_pos)
            if not self.is_alive:
                break

    def start(self):
        self.listner.start()

    def stop(self):
        self.is_alive = False

    def __enter__(self):
        self.is_alive = True
        self.listner.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        return
