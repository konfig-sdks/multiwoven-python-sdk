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

from multiwoven_python_sdk.type.connector_definitions_get_by_name_response_connector_spec_connection_specification import ConnectorDefinitionsGetByNameResponseConnectorSpecConnectionSpecification

class RequiredConnectorDefinitionsGetByNameResponseConnectorSpec(TypedDict):
    pass

class OptionalConnectorDefinitionsGetByNameResponseConnectorSpec(TypedDict, total=False):
    documentation_url: str

    connection_specification: ConnectorDefinitionsGetByNameResponseConnectorSpecConnectionSpecification

    supports_normalization: bool

    supports_dbt: bool

    stream_type: str

class ConnectorDefinitionsGetByNameResponseConnectorSpec(RequiredConnectorDefinitionsGetByNameResponseConnectorSpec, OptionalConnectorDefinitionsGetByNameResponseConnectorSpec):
    pass
