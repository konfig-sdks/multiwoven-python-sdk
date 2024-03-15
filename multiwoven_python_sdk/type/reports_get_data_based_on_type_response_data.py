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

from multiwoven_python_sdk.type.reports_get_data_based_on_type_response_data_sync_run_triggered import ReportsGetDataBasedOnTypeResponseDataSyncRunTriggered
from multiwoven_python_sdk.type.reports_get_data_based_on_type_response_data_total_sync_run_rows import ReportsGetDataBasedOnTypeResponseDataTotalSyncRunRows

class RequiredReportsGetDataBasedOnTypeResponseData(TypedDict):
    pass

class OptionalReportsGetDataBasedOnTypeResponseData(TypedDict, total=False):
    sync_run_triggered: ReportsGetDataBasedOnTypeResponseDataSyncRunTriggered

    total_sync_run_rows: ReportsGetDataBasedOnTypeResponseDataTotalSyncRunRows

class ReportsGetDataBasedOnTypeResponseData(RequiredReportsGetDataBasedOnTypeResponseData, OptionalReportsGetDataBasedOnTypeResponseData):
    pass
