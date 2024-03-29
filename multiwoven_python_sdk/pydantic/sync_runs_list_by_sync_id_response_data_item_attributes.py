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


class SyncRunsListBySyncIdResponseDataItemAttributes(BaseModel):
    sync_id: typing.Optional[int] = Field(None, alias='sync_id')

    status: typing.Optional[str] = Field(None, alias='status')

    started_at: typing.Optional[datetime] = Field(None, alias='started_at')

    finished_at: typing.Optional[datetime] = Field(None, alias='finished_at')

    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    total_query_rows: typing.Optional[int] = Field(None, alias='total_query_rows')

    total_rows: typing.Optional[int] = Field(None, alias='total_rows')

    successful_rows: typing.Optional[int] = Field(None, alias='successful_rows')

    failed_rows: typing.Optional[int] = Field(None, alias='failed_rows')

    error: typing.Optional[typing.Optional[str]] = Field(None, alias='error')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')
    class Config:
        arbitrary_types_allowed = True
