from typing import Literal

from .bubbles import create_bubbles
from .cyberpunk import create_cyberpunk
from .letter import Letter

SupportedLetters = Literal[
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


SupportedFonts = Literal[
    "bubbles",
    "cyberpunk",
]


class Alphabet:
    def __init__(
        self,
        font: SupportedFonts = "cyberpunk",
    ):
        self._fonts = {
            "bubbles": create_bubbles,
            "cyberpunk": create_cyberpunk,
        }

        spacing, letters = self._fonts.get(font, create_cyberpunk)()

        self._alphabet = {
            plain_text: Letter(
                plain_text,
                ascii_text,
            )
            for plain_text, ascii_text in letters.items()
        }

        self.font = font
        self.spacing = spacing

    def __iter__(self):
        for plaintext_letter, ascii_letter in self._alphabet.items():
            yield (
                plaintext_letter,
                ascii_letter.format(),
            )

    def __contains__(self, plaintext_letter: str):
        return plaintext_letter in self._alphabet

    def get_letter(self, plaintext_letter: str):
        selected_letter = self._alphabet.get(plaintext_letter)

        if selected_letter is None:
            return selected_letter

        return selected_letter.format()
