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


class ModelsListAllModelsResponseLinks(BaseModel):
    self_: typing.Optional[str] = Field(None, alias='self')

    first: typing.Optional[str] = Field(None, alias='first')

    prev: typing.Optional[str] = Field(None, alias='prev')

    next: typing.Optional[str] = Field(None, alias='next')

    last: typing.Optional[str] = Field(None, alias='last')
    class Config:
        arbitrary_types_allowed = True
