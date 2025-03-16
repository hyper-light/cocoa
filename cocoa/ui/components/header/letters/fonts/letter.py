import textwrap
from typing import Literal

Formatting = Literal["start", "end", "both"]


class Letter:
    def __init__(
        self,
        ascii: str,
    ):
        self.ascii = ascii
        self.height: int = 0
        self.width: int = 0

    def format(
        self,
        last_letter: bool = False,
    ):
        ascii_lines = [
            line.rstrip()
            for line in textwrap.dedent(
                self.ascii,
            ).split("\n")
            if len(line.strip(" ")) > 0
        ]

        self.width = max([len(line) for line in ascii_lines])

        for idx, line in enumerate(ascii_lines):
            ascii_lines[idx] = line

            line_length = len(line)

            if line_length < self.width:
                diff = self.width - line_length
                ascii_lines[idx] += " " * diff

        self.height = len(ascii_lines)

        return "\n".join(ascii_lines)
