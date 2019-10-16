from typing import Union

from intervals import closedopen, inf

from qr.constants import (LEAFLET_COLOR_STEP, LEAFLET_COLORS)


class LeafletInterval:
    def __init__(self, lower: int, upper: Union[int, None], color: str):
        self.interval = closedopen(lower, upper)
        self.color = color

    def __str__(self):
        return f'{self.interval} - {self.color}'

    def pick(self, value: int):
        if value in self.interval:
            return self.color
        return None
