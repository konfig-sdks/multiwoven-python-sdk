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

from multiwoven_python_sdk.type.models_update_model_by_id_request_model import ModelsUpdateModelByIdRequestModel

class RequiredModelsUpdateModelByIdRequest(TypedDict):
    pass

class OptionalModelsUpdateModelByIdRequest(TypedDict, total=False):
    model: ModelsUpdateModelByIdRequestModel

class ModelsUpdateModelByIdRequest(RequiredModelsUpdateModelByIdRequest, OptionalModelsUpdateModelByIdRequest):
    pass
