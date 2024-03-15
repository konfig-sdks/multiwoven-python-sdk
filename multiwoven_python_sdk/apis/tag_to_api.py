import typing_extensions

from multiwoven_python_sdk.apis.tags import TagValues
from multiwoven_python_sdk.apis.tags.connectors_api import ConnectorsApi
from multiwoven_python_sdk.apis.tags.syncs_api import SyncsApi
from multiwoven_python_sdk.apis.tags.models_api import ModelsApi
from multiwoven_python_sdk.apis.tags.connector_definitions_api import ConnectorDefinitionsApi
from multiwoven_python_sdk.apis.tags.reports_api import ReportsApi
from multiwoven_python_sdk.apis.tags.sync_runs_api import SyncRunsApi
from multiwoven_python_sdk.apis.tags.sync_records_api import SyncRecordsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONNECTORS: ConnectorsApi,
        TagValues.SYNCS: SyncsApi,
        TagValues.MODELS: ModelsApi,
        TagValues.CONNECTOR_DEFINITIONS: ConnectorDefinitionsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SYNC_RUNS: SyncRunsApi,
        TagValues.SYNC_RECORDS: SyncRecordsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONNECTORS: ConnectorsApi,
        TagValues.SYNCS: SyncsApi,
        TagValues.MODELS: ModelsApi,
        TagValues.CONNECTOR_DEFINITIONS: ConnectorDefinitionsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SYNC_RUNS: SyncRunsApi,
        TagValues.SYNC_RECORDS: SyncRecordsApi,
    }
)
