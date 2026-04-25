#!/usr/bin/env python3
"""
Patch a downloaded QMMM/_geom.py to remove berny.geomlib dependency safely.

Edits performed:
  - Remove: "from berny import geomlib"
  - Insert a minimal Geometry dataclass (replacement for berny.geomlib.Geometry)
  - Replace:
        geomlib.Geometry(  -> Geometry(
        geomlib.Geometry   -> Geometry

Key safety fix:
  - Ensures 'import numpy as np' is available BEFORE the injected Geometry class.
    It only omits the injected numpy import if numpy is already imported ABOVE
    the insertion point (not merely somewhere later in the file).

Usage:
  python patch_geom.py /path/to/QMMM/_geom.py
  python patch_geom.py /path/to/QMMM/_geom.py --dry-run
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


GEOMETRY_BLOCK = """\
# --- Geometry container (replaces berny.geomlib.Geometry) ---
from dataclasses import dataclass
import numpy as np

@dataclass
class Geometry:
    \"\"\"Minimal geometry container: species + coords (+ optional lattice).

    Intended to replace berny.geomlib.Geometry, which stores element symbols and
    coordinates (in Angstrom) and is commonly accessed via .species and .coords.
    \"\"\"
    species: list
    coords: np.ndarray
    lattice: object = None

    def __post_init__(self):
        self.coords = np.array(self.coords, dtype=float)

    def __len__(self):
        return len(self.species)

    def __iter__(self):
        return iter(zip(self.species, self.coords))
# --- End geometry container ---
"""


def has_geometry_block(text: str) -> bool:
    return "replaces berny.geomlib.Geometry" in text and "class Geometry" in text


def remove_geomlib_import(text: str) -> str:
    # Remove exactly: from berny import geomlib
    return re.sub(
        r"(?m)^[ \t]*from[ \t]+berny[ \t]+import[ \t]+geomlib[ \t]*\r?\n",
        "",
        text,
    )


def replace_geomlib_geometry(text: str) -> str:
    text = text.replace("geomlib.Geometry(", "Geometry(")
    text = text.replace("geomlib.Geometry", "Geometry")
    return text


def find_insertion_index(lines: list[str]) -> int:
    """
    Find a safe insertion point after:
      - optional shebang
      - optional encoding comment
      - optional module docstring
      - a contiguous import block at top (import/from + blank lines)
    """
    i = 0

    # 1) Shebang
    if i < len(lines) and lines[i].startswith("#!"):
        i += 1

    # 2) Encoding (PEP 263)
    if i < len(lines) and re.match(r"^#.*coding[:=]", lines[i]):
        i += 1

    # 3) Optional module docstring
    if i < len(lines) and re.match(r'^[ \t]*("""|\'\'\')', lines[i]):
        quote = '"""' if '"""' in lines[i] else "'''"
        i += 1
        while i < len(lines) and quote not in lines[i]:
            i += 1
        if i < len(lines):
            i += 1  # include closing line

    # 4) Skip blank lines
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    # 5) Consume contiguous import block (allow blank lines inside)
    j = i
    while j < len(lines):
        s = lines[j].strip()
        if s == "":
            j += 1
            continue
        if s.startswith("import ") or s.startswith("from "):
            j += 1
            continue
        break

    return j


def insert_geometry_block(text: str) -> str:
    if has_geometry_block(text):
        return text

    lines = text.splitlines(True)
    insert_at = find_insertion_index(lines)

    # Check for numpy import BEFORE insertion point only
    prefix = "".join(lines[:insert_at])
    has_np_before = bool(
        re.search(r"(?m)^[ \t]*import[ \t]+numpy[ \t]+as[ \t]+np[ \t]*$", prefix)
    )

    block = GEOMETRY_BLOCK
    if has_np_before:
        # Safe to omit our numpy import because it's already available above
        block = re.sub(r"(?m)^import numpy as np\r?\n", "", block)

    insertion = "\n" + block.rstrip() + "\n\n"
    lines.insert(insert_at, insertion)
    return "".join(lines)


def patch_text(original: str) -> str:
    text = original
    text = remove_geomlib_import(text)
    text = replace_geomlib_geometry(text)
    text = insert_geometry_block(text)
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path, help="Path to downloaded _geom.py")
    ap.add_argument("--dry-run", action="store_true", help="Preview changes, do not write.")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backup.")
    args = ap.parse_args()

    path: Path = args.path
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    original = path.read_text(encoding="utf-8")
    patched = patch_text(original)

    if patched == original:
        print("No changes needed (already patched or no geomlib usage found).")
        return

    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"Would patch: {path}")
        if "from berny import geomlib" in original and "from berny import geomlib" not in patched:
            print(" - removed: from berny import geomlib")
        if "geomlib.Geometry" in original and "geomlib.Geometry" not in patched:
            print(" - replaced: geomlib.Geometry -> Geometry")
        if not has_geometry_block(original) and has_geometry_block(patched):
            print(" - inserted: Geometry dataclass block")
        return

    if not args.no_backup:
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(original, encoding="utf-8")
        print(f"Backup written: {backup}")

    path.write_text(patched, encoding="utf-8")
    print(f"Patched written: {path}")


if __name__ == "__main__":
    main()