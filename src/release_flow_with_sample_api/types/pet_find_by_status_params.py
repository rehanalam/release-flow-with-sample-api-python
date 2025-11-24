# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PetFindByStatusParams"]


class PetFindByStatusParams(TypedDict, total=False):
    status: Literal["available", "pending"]
    """Status values that need to be considered for filter."""

    type: Literal["available", "pending"]
    """Status by type value that need to be considered for filter"""
