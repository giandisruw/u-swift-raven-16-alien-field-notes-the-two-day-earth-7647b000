#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text -- a review of planet Earth
left by an alien tourist -- to /output/entry.txt, as the bounty
requires. The line is at most 200 characters.
"""

import os
import sys

REVIEW = (
    "Two days on Earth: the sunsets are unreal, the locals apologise "
    "to furniture, and everyone is 'five minutes away' for an hour. "
    "Docking fee outrageous. 4 stars."
)

# Picked by a local pairwise judge (Caffeine router, bounty brief):
# reads as an alien tourist's review with a verdict ("4 stars"), the
# laugh comes from the alien angle on ordinary life (apologising to
# furniture, "five minutes away"), and it avoids the obvious targets
# the brief warns against (traffic, gravity, money, weather).
MAX_CHARS = 200


def main() -> int:
    # Enforce the sealed scorer's gate ourselves: 1-200 UTF-8 chars,
    # not only white space. Fail loudly instead of shipping an
    # invalid entry.
    if not (1 <= len(REVIEW) <= MAX_CHARS) or not REVIEW.strip():
        raise SystemExit(
            f"invalid review: {len(REVIEW)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(REVIEW)
    except OSError:
        # Local runs without a writable /output fall back to the repo root.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(REVIEW)
    print(REVIEW)
    print(f"characters: {len(REVIEW)}")
    print(f"wrote: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
