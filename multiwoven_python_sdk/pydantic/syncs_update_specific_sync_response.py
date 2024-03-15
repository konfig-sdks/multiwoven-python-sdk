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

from multiwoven_python_sdk.pydantic.syncs_update_specific_sync_response_data import SyncsUpdateSpecificSyncResponseData

class SyncsUpdateSpecificSyncResponse(BaseModel):
    success: typing.Optional[bool] = Field(None, alias='success')

    message: typing.Optional[str] = Field(None, alias='message')

    data: typing.Optional[SyncsUpdateSpecificSyncResponseData] = Field(None, alias='data')
    class Config:
        arbitrary_types_allowed = True
