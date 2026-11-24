"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
/output/entry.txt. Deterministic: no input, no network, no randomness —
the same label on every run.
"""

from pathlib import Path

# Straight-faced safety notice; the hazard is a duplicate self, and the
# punch lands in the final words.
ENTRY = (
    "WARNING: If you meet yourself, do not make eye contact. "
    "He knows what you did."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
