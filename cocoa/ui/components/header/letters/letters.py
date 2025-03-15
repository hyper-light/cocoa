from typing import Literal

from .fonts import create_bubbles, create_cyberpunk
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
            "cyberpunk": create_cyberpunk,
            "bubbles": create_bubbles,
        }

        self._alphabet: dict[str, str] = self._fonts.get(
            font,
            create_cyberpunk,
        )()

    def __iter__(self):
        for plaintext_letter, ascii_letter in self._alphabet.items():
            yield (
                plaintext_letter,
                self._format_letter(
                    ascii_letter,
                    plaintext_letter,
                ),
            )

    def __contains__(self, plaintext_letter: str):
        return plaintext_letter in self._alphabet

    def get_letter(self, plaintext_letter: str):
        selected_letter = self._alphabet.get(plaintext_letter)

        if selected_letter is None:
            return selected_letter

        return self._format_letter(
            selected_letter,
            plaintext_letter,
        )

    def _format_letter(
        self,
        indented_ascii_letter: str,
        plaintext_letter: str,
    ):
        letter_lines = [
            line for line in indented_ascii_letter.split("\n") if len(line.strip()) > 0
        ]

        leading_spaces_count: list[int] = []

        for line in letter_lines:
            space_count = 0

            for char in line:
                if char == " ":
                    space_count += 1

                else:
                    leading_spaces_count.append(space_count)
                    break

        dedent_spaces = min(leading_spaces_count)

        dedented_lines: list[str] = []
        line_widths: list[int] = []

        for line in letter_lines:
            dedented_line = line[dedent_spaces:].rstrip()

            line_widths.append(len(dedented_line))
            dedented_lines.append(dedented_line)

        letter_width = max(line_widths)

        for idx, line in enumerate(dedented_lines):
            line_length = len(line)
            dedented_lines[idx] += " " * (letter_width - line_length)

        return FormattedLetter(
            plaintext_letter=plaintext_letter,
            ascii="\n".join(dedented_lines),
            height=len(dedented_lines),
            width=letter_width,
        )
