#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run -- Make.fun entry.

Writes the chosen two-line explanation (a toaster, explained to a
10-year-old through an analogy, plus one honest sentence about what
the analogy maps and what it leaves out) to /output/entry.txt.
Standard library only.
"""

import os

LINE_1 = "A toaster is like a tiny sun trapped in a box that gives your bread a warm hug on both sides until it turns golden and crunchy."
LINE_2 = "It maps the heat and the golden colour, but leaves out that a real sun never pops your toast up when it is done."

OUTPUT_PATH = "/output/entry.txt"


def main():
    lines = (LINE_1, LINE_2)
    for line in lines:
        assert 1 <= len(line) <= 200, "line must be 1-200 characters: %r" % line
        assert line.count(".") == 1 and line.endswith("."), (
            "each line must be a single sentence: %r" % line
        )
    assert len(lines) == 2, "entry must be exactly 2 lines"

    text = LINE_1 + "\n" + LINE_2
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    verify_entry(text)

    print("line 1: %d chars" % len(LINE_1))
    print("line 2: %d chars" % len(LINE_2))


def verify_entry(expected_text):
    """Re-open /output/entry.txt and assert it holds exactly the two lines.

    Guards against a partial write or stray trailing newline: the file
    must byte-match the entry, with no trailing newline.
    """
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        actual = f.read()
    assert actual == expected_text, (
        "entry.txt mismatch: expected %r, got %r" % (expected_text, actual)
    )
    assert not actual.endswith("\n"), "entry.txt must not end with a newline"
    assert len(actual.split("\n")) == 2, "entry.txt must hold exactly 2 lines"


if __name__ == "__main__":
    main()
