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

from multiwoven_python_sdk.pydantic.syncs_get_report_data_response_data_configurations_catalog_mapping_types import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypes

class SyncsGetReportDataResponseDataConfigurations(BaseModel):
    catalog_mapping_types: typing.Optional[SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypes] = Field(None, alias='catalog_mapping_types')
    class Config:
        arbitrary_types_allowed = True
