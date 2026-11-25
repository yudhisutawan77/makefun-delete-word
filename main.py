#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary -- entry program.

The brief asks for exactly one word to erase from the dictionary forever,
with nothing else attached. This program writes that single word to
/output/entry.txt so the gate can check it and the pairwise judge can
compare it against the rest of the field.

The word is "queue". Five letters, four of them silent: it is literally
the letter Q with four letters queuing behind it. Delete it and the joke
lands at first sight -- the word itself is a queue of letters, and the
language loses its word for standing in line. The humour comes from the
word's own spelling, not from shock, and it is a fresher pick than the
field's first thoughts ("moist", "synergy", "irregardless"), while still
instantly understood by any reader.
"""

import os
import sys

WORD_TO_ERASE = "queue"


def resolve_entry_path(raw_out: str) -> str:
    """ENTRY_OUT may name the output file itself or its directory;
    accept either, so the harness layout never breaks the write."""
    if raw_out.endswith(".txt"):
        return raw_out
    return os.path.join(raw_out, "entry.txt")


def validate_word(word: str) -> str:
    """Enforce the gate locally: 1-77 characters, not only whitespace,
    and exactly one token with no spaces or line breaks."""
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if not 1 <= len(word) <= 77:
        raise ValueError("entry must be 1-77 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    return word


def main() -> int:
    text = validate_word(WORD_TO_ERASE)
    path = resolve_entry_path(os.environ.get("ENTRY_OUT", "/output"))
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
