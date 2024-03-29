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


class SyncRecordsListForSyncRunResponseDataItemAttributesRecord(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    state: typing.Optional[str] = Field(None, alias='state')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    phone_number: typing.Optional[int] = Field(None, alias='phone_number')

    email_address: typing.Optional[str] = Field(None, alias='email_address')
    class Config:
        arbitrary_types_allowed = True
