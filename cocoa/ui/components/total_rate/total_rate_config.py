from pydantic import BaseModel, StrictInt, StrictStr
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


class TotalRateConfig(BaseModel):
    unit: StrictStr | None = None
    precision: StrictInt = 3
    attributes: List[Attributizer] | None = None
    color: Colorizer | None = None
    highlight: HighlightColorizer | None = None
    horizontal_alignment: HorizontalAlignment = "center"
    terminal_mode: TerminalDisplayMode = "compatability"
