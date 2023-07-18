from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class TimePoint:
    time: datetime.time
    x: int
    y: int

    def xy(self):
        return self.x, self.y


@dataclass(frozen=True)
class Click(TimePoint):
    pass


@dataclass(frozen=True)
class Release(TimePoint):
    pass


@dataclass(frozen=True)
class Drag:
    click: Click
    release: Release
