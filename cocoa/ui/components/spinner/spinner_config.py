from pydantic import BaseModel, StrictStr, StrictBool
from cocoa.ui.config.mode import TerminalDisplayMode
from cocoa.ui.styling.colors import Colorizer, HighlightColorizer
from cocoa.ui.styling.attributes import Attributizer
from typing import List
from .spinner_types import SpinnerName


class SpinnerConfig(BaseModel):
    ready_attributes: List[Attributizer] | None = None
    ready_color: Colorizer | None = None
    ready_highlight: HighlightColorizer | None = None
    active_color: Colorizer | None = None
    active_highlight: HighlightColorizer | None = None
    active_attributes: List[Attributizer] | None = None
    fail_attrbutes: List[Attributizer] | None = None
    fail_char: StrictStr = "✘"
    fail_color: Colorizer | None = None
    fail_highlight: HighlightColorizer | None = None
    ok_attributes: List[Attributizer] | None = None
    ok_char: StrictStr = "✔"
    ok_color: Colorizer | None = None
    ok_highlight: HighlightColorizer | None = None
    reverse_spinner_direction: StrictBool = False
    spinner: SpinnerName
    terminal_mode: TerminalDisplayMode = "compatability"
