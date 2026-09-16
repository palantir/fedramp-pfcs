from __future__ import annotations

import copy
from collections.abc import Callable
from typing import Any

import pytest
from jsonschema import ValidationError

from scripts.validate_json import (
    DOCUMENT_PATH,
    load_json,
    validate_document,
)


def test_committed_document_is_valid() -> None:
    validate_document(load_json(DOCUMENT_PATH))


def remove_required_property(document: dict[str, Any]) -> None:
    del document["serviceIdentification"]


def set_wrong_type(document: dict[str, Any]) -> None:
    document["contactInformation"] = "not an array"


def set_unsupported_enum(document: dict[str, Any]) -> None:
    document["serviceProperties"]["deploymentModel"] = "Private Cloud"


def set_invalid_date(document: dict[str, Any]) -> None:
    document["certifiedServices"][0]["dateAvailable"] = "not-a-date"


def set_invalid_url(document: dict[str, Any]) -> None:
    document["serviceIdentification"]["website"] = "not a valid URI"


@pytest.mark.parametrize(
    "mutation",
    [
        remove_required_property,
        set_wrong_type,
        set_unsupported_enum,
        set_invalid_date,
        set_invalid_url,
    ],
    ids=("required", "type", "enum", "date", "url"),
)
def test_invalid_documents_are_rejected(
    mutation: Callable[[dict[str, Any]], None],
) -> None:
    document = copy.deepcopy(load_json(DOCUMENT_PATH))
    mutation(document)

    with pytest.raises(ValidationError):
        validate_document(document)
