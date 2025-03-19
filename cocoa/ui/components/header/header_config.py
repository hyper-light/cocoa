from typing import Dict, List, Literal

from pydantic import BaseModel, StrictStr

from cocoa.ui.config.mode import TerminalDisplayMode
from cocoa.ui.styling.attributes import Attributizer
from cocoa.ui.styling.colors import Colorizer, HighlightColorizer

from .letters import FormatterSet, SupportedFonts, SupportedLetters

HeaderHorizontalAlignment = Literal["left", "center", "right"]
HeaderVerticalAlignment = Literal["top", "center", "bottom"]


class HeaderConfig(BaseModel):
    header_text: StrictStr
    color: Colorizer | None = None
    horizontal_alignment: HeaderHorizontalAlignment = "left"
    vertical_alignment: HeaderVerticalAlignment = "center"
    highlight: HighlightColorizer | None = None
    attributes: List[Attributizer] | None = None
    terminal_mode: TerminalDisplayMode = "compatability"
    formatters: Dict[SupportedLetters, FormatterSet] | None = None
    font: SupportedFonts = "cyberpunk"
