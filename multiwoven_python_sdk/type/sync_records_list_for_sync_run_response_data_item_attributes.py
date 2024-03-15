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

from multiwoven_python_sdk.type.sync_records_list_for_sync_run_response_data_item_attributes_record import SyncRecordsListForSyncRunResponseDataItemAttributesRecord

class RequiredSyncRecordsListForSyncRunResponseDataItemAttributes(TypedDict):
    pass

class OptionalSyncRecordsListForSyncRunResponseDataItemAttributes(TypedDict, total=False):
    sync_id: int

    sync_run_id: int

    record: SyncRecordsListForSyncRunResponseDataItemAttributesRecord

    status: str

    action: str

    error: typing.Optional[str]

    created_at: datetime

    updated_at: datetime

class SyncRecordsListForSyncRunResponseDataItemAttributes(RequiredSyncRecordsListForSyncRunResponseDataItemAttributes, OptionalSyncRecordsListForSyncRunResponseDataItemAttributes):
    pass