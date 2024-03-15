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

from multiwoven_python_sdk.type.connectors_discover_catalog_info_response_data_attributes_catalog import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog

class RequiredConnectorsDiscoverCatalogInfoResponseDataAttributes(TypedDict):
    pass

class OptionalConnectorsDiscoverCatalogInfoResponseDataAttributes(TypedDict, total=False):
    connector_id: int

    workspace_id: int

    catalog: ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog

    catalog_hash: str

class ConnectorsDiscoverCatalogInfoResponseDataAttributes(RequiredConnectorsDiscoverCatalogInfoResponseDataAttributes, OptionalConnectorsDiscoverCatalogInfoResponseDataAttributes):
    pass
