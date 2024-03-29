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

from multiwoven_python_sdk.pydantic.syncs_list_operations_response_data_item_attributes_configuration import SyncsListOperationsResponseDataItemAttributesConfiguration

class SyncsListOperationsResponseDataItemAttributes(BaseModel):
    source_id: typing.Optional[int] = Field(None, alias='source_id')

    destination_id: typing.Optional[int] = Field(None, alias='destination_id')

    model_id_: typing.Optional[int] = Field(None, alias='model_id')

    configuration: typing.Optional[SyncsListOperationsResponseDataItemAttributesConfiguration] = Field(None, alias='configuration')

    schedule_type: typing.Optional[Literal["automated"]] = Field(None, alias='schedule_type')

    sync_mode: typing.Optional[Literal["full_refresh"]] = Field(None, alias='sync_mode')

    sync_interval: typing.Optional[int] = Field(None, alias='sync_interval')

    sync_interval_unit: typing.Optional[Literal["minutes"]] = Field(None, alias='sync_interval_unit')

    stream_name: typing.Optional[str] = Field(None, alias='stream_name')

    status: typing.Optional[str] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
