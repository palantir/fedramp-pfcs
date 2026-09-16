#!/usr/bin/env python3
"""Render README.md from its template and the public information JSON."""

import argparse
import difflib
import json
from pathlib import Path

from jinja2 import Environment, StrictUndefined

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "pfcs-public-information.json"
TEMPLATE_PATH = ROOT / "README.template.md"
README_PATH = ROOT / "README.md"


def render_readme() -> str:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    template = Environment(
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    ).from_string(TEMPLATE_PATH.read_text(encoding="utf-8"))
    return template.render(**data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    check = parser.parse_args().check

    expected = render_readme()
    current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""

    if check and current != expected:
        print("README.md is out of date. Run `make readme`.")
        print(
            "".join(
                difflib.unified_diff(
                    current.splitlines(keepends=True),
                    expected.splitlines(keepends=True),
                    fromfile="README.md",
                    tofile="README.md (generated)",
                )
            )
        )
        return 1

    if check:
        print("README.md is current.")
    else:
        README_PATH.write_text(expected, encoding="utf-8")
        print("Updated README.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
