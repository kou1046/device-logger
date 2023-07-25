from __future__ import annotations
from typing import Callable, Any
import datetime
from typing_extensions import SupportsIndex

from pynput import mouse

from .drag import Drag, Click, Release


class DragLogger:
    def __init__(
        self,
        on_press: Callable[[Click], Any] | None = None,
        on_drag: Callable[[Drag], Any] | None = None,
    ):
        self.listener = mouse.Listener(on_click=self._on_click())
        self.on_press = on_press
        self.on_drag = on_drag
        self.is_alive = False

    def _on_click(self):
        click_queue: Click | None = None

        def __on_click(x: int, y: int, button: mouse.Button, is_press: bool):
            nonlocal click_queue
            if not self.is_alive:
                return False

            if is_press and button.left and click_queue is None:
                click_queue = Click(datetime.datetime.now().time(), x, y)

                if self.on_press is None:
                    return
                self.on_press(click_queue)

            if not is_press and button.left and click_queue:
                release = Release(datetime.datetime.now().time(), x, y)
                drag = Drag(click_queue, release)
                click_queue = None

                if self.on_drag is None:
                    return
                self.on_drag(drag)

        return __on_click

    def start(self):
        self.listener.start()

    def stop(self):
        self.is_alive = False

    def join(self):
        self.listener.join()

    def __enter__(self):
        self.is_alive = True
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        return
