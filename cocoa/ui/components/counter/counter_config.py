from pydantic import BaseModel, StrictInt, StrictStr
from cocoa.ui.styling.colors import (
    Colorizer,
    HighlightColorizer,
)
from cocoa.ui.styling.attributes import Attributizer
from cocoa.ui.config.mode import TerminalDisplayMode
from typing import List, Literal


HorizontalAlignment = Literal["left", "center", "right"]


class CounterConfig(BaseModel):
    unit: StrictStr | None = None
    precision: StrictInt = 3
    initial_amount: StrictInt = 0
    color: Colorizer | None = None
    highlight: HighlightColorizer | None = None
    attributes: List[Attributizer] | None = None
    horizontal_alignment: HorizontalAlignment = "center"
    terminal_mode: TerminalDisplayMode = "compatability"
