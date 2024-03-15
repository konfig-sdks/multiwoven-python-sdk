# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredModelsCreateModelResponseDataAttributes(TypedDict):
    pass

class OptionalModelsCreateModelResponseDataAttributes(TypedDict, total=False):
    description: str

    name: str

    query: str

    query_type: str

    primary_key: str

    connector_id: int

    created_at: datetime

    updated_at: datetime

class ModelsCreateModelResponseDataAttributes(RequiredModelsCreateModelResponseDataAttributes, OptionalModelsCreateModelResponseDataAttributes):
    pass
