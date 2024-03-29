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

from multiwoven_python_sdk.type.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_filter import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateFilter
from multiwoven_python_sdk.type.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_variable import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateVariable

class RequiredSyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate(TypedDict):
    pass

class OptionalSyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate(TypedDict, total=False):
    variable: SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateVariable

    filter: SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateFilter

class SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate(RequiredSyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate, OptionalSyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate):
    pass
