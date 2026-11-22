"""Write the curious-judge entry text to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

TEXT = (
    "On your desk lies a verdict slip, already filled in, in your handwriting. "
    "It names a text you have not read yet. "
    "The score is yours. The reasons are yours. The date is tomorrow. "
    "So tell me, judge — which text did you choose, "
    "and how did you know before you read a word of it?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
