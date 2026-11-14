"""Write Night Shift as deterministic UTF-8 bytes."""

import os
from pathlib import Path

POEM = """Night Shift

I stopped my belt. Across the aisle
Ruth kept feeding pillowcases
through the ironer.

We had agreed at lunch.
Now it was three. Her counter clicked.
I could stop my hands.
I could not stop hers.

Then she laid a pillowcase aside,
smoothed it flat, and pressed the switch.
The dryers swallowed Luis calling
something we could not hear.
We pointed. He stopped his too.

Ruth sat in the supervisor’s chair.
She asked what we would say
when he came back.

The ironer ticked as it cooled.
We had never heard it cool.
"""


def poem_bytes(poem: str) -> bytes:
    """Check the code-point contract before any filesystem changes."""
    if not 1 <= len(poem) <= 1000 or not poem.strip():
        raise ValueError("Poem must contain 1–1000 code points and be nonblank")
    return poem.encode("utf-8", errors="strict")


def write_entry(output_dir: Path, poem: str = POEM) -> None:
    payload = poem_bytes(poem)
    if not output_dir.is_absolute():
        output_dir = Path(__file__).resolve().parent / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(payload)


def main() -> None:
    write_entry(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))


if __name__ == "__main__":
    main()
