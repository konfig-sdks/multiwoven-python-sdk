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

from multiwoven_python_sdk.type.sync_runs_list_by_sync_id_response_data import SyncRunsListBySyncIdResponseData
from multiwoven_python_sdk.type.sync_runs_list_by_sync_id_response_links import SyncRunsListBySyncIdResponseLinks

class RequiredSyncRunsListBySyncIdResponse(TypedDict):
    pass

class OptionalSyncRunsListBySyncIdResponse(TypedDict, total=False):
    data: SyncRunsListBySyncIdResponseData

    links: SyncRunsListBySyncIdResponseLinks

class SyncRunsListBySyncIdResponse(RequiredSyncRunsListBySyncIdResponse, OptionalSyncRunsListBySyncIdResponse):
    pass
