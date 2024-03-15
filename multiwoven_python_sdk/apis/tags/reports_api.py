# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from multiwoven_python_sdk.paths.api_v1_reports.get import GetDataBasedOnType
from multiwoven_python_sdk.apis.tags.reports_api_raw import ReportsApiRaw


class ReportsApi(
    GetDataBasedOnType,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ReportsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ReportsApiRaw(api_client)
