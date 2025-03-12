from pydantic import BaseModel, AnyUrl, StrictStr
from cocoa.ui.styling.colors import Colorizer, HighlightColorizer
from cocoa.ui.styling.attributes import Attributizer
from cocoa.ui.config.mode import TerminalDisplayMode
from typing import List


class LinkConfig(BaseModel):
    link_url: AnyUrl | None = None
    link_text: StrictStr
    color: Colorizer | None = None
    highlight: HighlightColorizer | None = None
    attributes: List[Attributizer] | None = None
    terminal_mode: TerminalDisplayMode = "compatability"
