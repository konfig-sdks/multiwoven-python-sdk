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


class ReportsGetDataBasedOnTypeResponseDataSyncRunTriggeredItem(BaseModel):
    time_slice: typing.Optional[datetime] = Field(None, alias='time_slice')

    total_count: typing.Optional[int] = Field(None, alias='total_count')

    failed_count: typing.Optional[int] = Field(None, alias='failed_count')

    success_count: typing.Optional[int] = Field(None, alias='success_count')
    class Config:
        arbitrary_types_allowed = True
