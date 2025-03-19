from typing import List

from pydantic import BaseModel, StrictInt, StrictStr

from .fonts import SupportedFonts


class FormattedWord(BaseModel):
    plaintext_word: StrictStr
    ascii: StrictStr
    ascii_lines: List[StrictStr]
    height: StrictInt
    width: StrictInt
    font: SupportedFonts
