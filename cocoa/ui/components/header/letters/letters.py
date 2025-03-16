from typing import Literal

from .fonts import Letter, create_bubbles, create_cyberpunk
from .formatted_letter import FormattedLetter

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


class Letters:
    def __init__(
        self,
        font: str = "cyberpunk",
    ):
        self._fonts = {
            "bubbles": create_bubbles,
            "cyberpunk": create_cyberpunk,
        }

        font_set = self._fonts.get(
            font,
            create_cyberpunk,
        )()

        self._alphabet: dict[str, Letter] = font_set.font

    def __iter__(self):
        for plaintext_letter, ascii_letter in self._alphabet.items():
            yield (
                plaintext_letter,
                FormattedLetter(
                    plaintext_letter=plaintext_letter,
                    ascii=ascii_letter.format(),
                    height=ascii_letter.height,
                    width=ascii_letter.width,
                ),
            )

    def __contains__(self, plaintext_letter: str):
        return plaintext_letter in self._alphabet

    def get_letter(self, plaintext_letter: str):
        selected_letter = self._alphabet.get(plaintext_letter)

        if selected_letter is None:
            return selected_letter

        return FormattedLetter(
            plaintext_letter=plaintext_letter,
            ascii=selected_letter.format(),
            height=selected_letter.height,
            width=selected_letter.width,
        )
