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

from multiwoven_python_sdk.type.syncs_update_specific_sync_request_sync_configuration import SyncsUpdateSpecificSyncRequestSyncConfiguration

class RequiredSyncsUpdateSpecificSyncRequestSync(TypedDict):
    pass

class OptionalSyncsUpdateSpecificSyncRequestSync(TypedDict, total=False):
    source_id: int

    destination_id: int

    model_id: int

    schedule_type: str

    configuration: SyncsUpdateSpecificSyncRequestSyncConfiguration

    stream_name: str

    sync_mode: str

    sync_interval: int

    sync_interval_unit: str

class SyncsUpdateSpecificSyncRequestSync(RequiredSyncsUpdateSpecificSyncRequestSync, OptionalSyncsUpdateSpecificSyncRequestSync):
    pass