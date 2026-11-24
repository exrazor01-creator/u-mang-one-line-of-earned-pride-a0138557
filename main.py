"""Write one line of earned pride to /output/entry.txt.

The line: after years of teaching himself English from the labels on
cleaning bottles, a night janitor reads his daughter's report card
aloud, slowly, without asking her to translate. A small person, a
long quiet effort, a concrete scene - the effort is front-loaded so
the pride lands in the last clause, when he no longer needs her help.

Gate guard: the entry must be UTF-8 text of 1 to 240 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "After years of teaching himself English from the labels on "
    "cleaning bottles, the night janitor read his daughter's report "
    "card aloud, slowly, without asking her to translate."
)

MIN_CHARS = 1
MAX_CHARS = 240


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 and ch not in ("\n", "\r") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
