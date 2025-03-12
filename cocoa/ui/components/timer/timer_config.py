from pydantic import BaseModel, StrictStr, StrictInt
from cocoa.ui.config.mode import TerminalDisplayMode
from cocoa.ui.styling.attributes import (
    Attributizer,
)
from cocoa.ui.styling.colors import (
    Colorizer,
    HighlightColorizer,
)
from typing import List, Literal


HorizontalAlignment = Literal["left", "center", "right"]


class TimerConfig(BaseModel):
    attributes: List[Attributizer] | None = None
    color: Colorizer | None = None
    highlight: HighlightColorizer | None = None
    horizontal_alignment: HorizontalAlignment = "left"
    terminal_mode: TerminalDisplayMode = "compatability"
