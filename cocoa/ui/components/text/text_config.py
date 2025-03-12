from pydantic import BaseModel, StrictStr
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


class TextConfig(BaseModel):
    text: StrictStr
    color: Colorizer | None = None
    highlight: HighlightColorizer | None = None
    attributes: List[Attributizer] | None = None
    horizontal_alignment: HorizontalAlignment = "center"
    terminal_mode: TerminalDisplayMode = "compatability"
