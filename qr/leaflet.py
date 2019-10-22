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


class LeafletColorManager:
    intervals = [
        LeafletInterval(
            index*LEAFLET_COLOR_STEP,
            (index*LEAFLET_COLOR_STEP)+LEAFLET_COLOR_STEP if index <= len(LEAFLET_COLORS)-2 else inf,
            color
        )
        for index, color in enumerate(LEAFLET_COLORS)
    ]

    @classmethod
    def pick(cls, value: int):
        if value < 0:
            raise ValueError('Não é possível procurar um valor menor do que 0!')
        for interval in cls.intervals:
            color = interval.pick(value)
            if color is not None:
                return color
        raise Exception('Não foi encontrado um valor para o intervalo!')
