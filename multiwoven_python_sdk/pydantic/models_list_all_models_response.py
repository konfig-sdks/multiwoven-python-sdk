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
from pydantic import BaseModel, Field, RootModel

from multiwoven_python_sdk.pydantic.models_list_all_models_response_data import ModelsListAllModelsResponseData
from multiwoven_python_sdk.pydantic.models_list_all_models_response_links import ModelsListAllModelsResponseLinks

class ModelsListAllModelsResponse(BaseModel):
    data: typing.Optional[ModelsListAllModelsResponseData] = Field(None, alias='data')

    links: typing.Optional[ModelsListAllModelsResponseLinks] = Field(None, alias='links')
    class Config:
        arbitrary_types_allowed = True
