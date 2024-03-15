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

from multiwoven_python_sdk.pydantic.connectors_discover_catalog_info_response_data_attributes import ConnectorsDiscoverCatalogInfoResponseDataAttributes

class ConnectorsDiscoverCatalogInfoResponseData(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    type: typing.Optional[str] = Field(None, alias='type')

    attributes: typing.Optional[ConnectorsDiscoverCatalogInfoResponseDataAttributes] = Field(None, alias='attributes')
    class Config:
        arbitrary_types_allowed = True
