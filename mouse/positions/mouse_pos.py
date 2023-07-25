from __future__ import annotations
from dataclasses import dataclass

from ..drags.drag import TimePoint


@dataclass(frozen=True)
class MousePos(TimePoint):
    pass
