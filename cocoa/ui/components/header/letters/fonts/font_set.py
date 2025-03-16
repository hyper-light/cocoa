from .letter import Letter


class FontSet:
    def __init__(
        self,
        font: dict[str, Letter],
    ):
        self.font = font
