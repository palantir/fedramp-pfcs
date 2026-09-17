#!/usr/bin/env python3
"""Validate the PFCS public information JSON."""

import json
from pathlib import Path
from urllib.request import urlopen

from jsonschema import FormatChecker, ValidationError, validate
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
DOCUMENT_PATH = ROOT / "data" / "pfcs-public-information.json"
SCHEMA_URL = (
    "https://raw.githubusercontent.com/FedRAMP/schemas/main/"
    "fedramp-certification-package-overview-schema-2026-06-24.json"
)
COMMON_SCHEMA_URL = (
    "https://raw.githubusercontent.com/FedRAMP/schemas/main/"
    "fedramp-common-definitions-schema-2026-06-24.json"
)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def load_schema(url: str = SCHEMA_URL) -> dict:
    with urlopen(url) as response:
        return json.load(response)


def validate_document(data: dict) -> None:
    common_schema = load_schema(COMMON_SCHEMA_URL)
    registry = Registry().with_resource(
        common_schema["$id"], Resource.from_contents(common_schema)
    )
    validate(
        instance=data,
        schema=load_schema(),
        format_checker=FormatChecker(),
        registry=registry,
    )


def main() -> int:
    data = load_json(DOCUMENT_PATH)
    try:
        validate_document(data)
        print("Valid JSON")
        return 0
    except ValidationError as error:
        print(f"Invalid JSON: {error.message}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
