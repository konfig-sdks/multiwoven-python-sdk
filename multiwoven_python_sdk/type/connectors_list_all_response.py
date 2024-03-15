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

from multiwoven_python_sdk.type.connectors_list_all_response_data import ConnectorsListAllResponseData
from multiwoven_python_sdk.type.connectors_list_all_response_links import ConnectorsListAllResponseLinks

class RequiredConnectorsListAllResponse(TypedDict):
    pass

class OptionalConnectorsListAllResponse(TypedDict, total=False):
    data: ConnectorsListAllResponseData

    links: ConnectorsListAllResponseLinks

class ConnectorsListAllResponse(RequiredConnectorsListAllResponse, OptionalConnectorsListAllResponse):
    pass
