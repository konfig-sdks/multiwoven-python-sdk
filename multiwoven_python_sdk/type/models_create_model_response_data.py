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

from multiwoven_python_sdk.type.models_create_model_response_data_attributes import ModelsCreateModelResponseDataAttributes

class RequiredModelsCreateModelResponseData(TypedDict):
    pass

class OptionalModelsCreateModelResponseData(TypedDict, total=False):
    id: str

    type: str

    attributes: ModelsCreateModelResponseDataAttributes

class ModelsCreateModelResponseData(RequiredModelsCreateModelResponseData, OptionalModelsCreateModelResponseData):
    pass
