# coding: utf-8
"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from multiwoven_python_sdk.client_custom import ClientCustom
from multiwoven_python_sdk.configuration import Configuration
from multiwoven_python_sdk.api_client import ApiClient
from multiwoven_python_sdk.type_util import copy_signature
from multiwoven_python_sdk.apis.tags.connector_definitions_api import ConnectorDefinitionsApi
from multiwoven_python_sdk.apis.tags.connectors_api import ConnectorsApi
from multiwoven_python_sdk.apis.tags.models_api import ModelsApi
from multiwoven_python_sdk.apis.tags.reports_api import ReportsApi
from multiwoven_python_sdk.apis.tags.sync_records_api import SyncRecordsApi
from multiwoven_python_sdk.apis.tags.sync_runs_api import SyncRunsApi
from multiwoven_python_sdk.apis.tags.syncs_api import SyncsApi



class Multiwoven(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.connector_definitions: ConnectorDefinitionsApi = ConnectorDefinitionsApi(api_client)
        self.connectors: ConnectorsApi = ConnectorsApi(api_client)
        self.models: ModelsApi = ModelsApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.sync_records: SyncRecordsApi = SyncRecordsApi(api_client)
        self.sync_runs: SyncRunsApi = SyncRunsApi(api_client)
        self.syncs: SyncsApi = SyncsApi(api_client)
