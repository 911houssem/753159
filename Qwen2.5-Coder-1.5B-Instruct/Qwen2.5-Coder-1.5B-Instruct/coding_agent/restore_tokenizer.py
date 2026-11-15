#!/usr/bin/env python3
"""Rebuild the original tokenizer.json from the small text chunks in this repository."""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = HERE / "tokenizer_parts"
OUTPUT = HERE.parent / "tokenizer.json"
EXPECTED_SHA256 = "c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539"


def main() -> int:
    chunks = sorted(PARTS.glob("tokenizer.json.part*"))
    if len(chunks) != 13:
        raise SystemExit(f"Expected 13 tokenizer chunks, found {len(chunks)}")

    # Read bytes to preserve original line endings exactly (including on Windows).
    data = b"".join(path.read_bytes() for path in chunks)
    actual = hashlib.sha256(data).hexdigest()
    if actual != EXPECTED_SHA256:
        raise SystemExit(f"Tokenizer integrity check failed: {actual}")

    OUTPUT.write_bytes(data)
    print(f"Restored {OUTPUT.name}; SHA-256 verified: {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
