from __future__ import annotations
from typing import Callable, Any
import datetime

from pynput import mouse

from .drag import Drag, Click, Release


class DragLogger:
    def __init__(self, on_drag: Callable[[Drag], Any] | None):
        self.listener = mouse.Listener(on_click=self._on_click())
        self.on_drag = on_drag

    def _on_click(self):
        click_queue: Click | None = None

        def __on_click(x: int, y: int, button: mouse.Button, is_press: bool):
            nonlocal click_queue
            if is_press and button.left and click_queue is None:
                click_queue = Click(datetime.datetime.now().time(), x, y)
            if not is_press and button.left and click_queue:
                release = Release(datetime.datetime.now().time(), x, y)
                drag = Drag(click_queue, release)
                if self.on_drag is not None:
                    self.on_drag(drag)
                click_queue = None

        return __on_click

    def start(self):
        with self.listener:
            self.listener.join()
