"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line for a crypto trader who was just
liquidated, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line: a classic fortune-cookie opening ("Your lucky numbers are...")
whose twist is that the lucky numbers are the ones the trader sold
before the pump — rueful, warm, specific to the loss, and the surprise
lands on the last word.
"""

import os

FORTUNE = "Your lucky numbers are the ones you sold before the pump."

# Competition caps: one line, at most 20 words, 1-160 characters.
assert 1 <= len(FORTUNE) <= 160
assert len(FORTUNE.split()) <= 20


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every byte, and the
    # tie-break favours the smaller text.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()
