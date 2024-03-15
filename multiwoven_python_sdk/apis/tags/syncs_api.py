# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from multiwoven_python_sdk.paths.api_v1_syncs.post import CreateNewSyncOperation
from multiwoven_python_sdk.paths.api_v1_syncs_id.delete import DeleteSyncOperation
from multiwoven_python_sdk.paths.api_v1_syncs_configurations.get import GetReportData
from multiwoven_python_sdk.paths.api_v1_syncs.get import ListOperations
from multiwoven_python_sdk.paths.api_v1_syncs_id.get import ShowDetails
from multiwoven_python_sdk.paths.api_v1_syncs_id.put import UpdateSpecificSync
from multiwoven_python_sdk.apis.tags.syncs_api_raw import SyncsApiRaw


class SyncsApi(
    CreateNewSyncOperation,
    DeleteSyncOperation,
    GetReportData,
    ListOperations,
    ShowDetails,
    UpdateSpecificSync,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SyncsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SyncsApiRaw(api_client)
