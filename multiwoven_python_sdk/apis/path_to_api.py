import typing_extensions

from multiwoven_python_sdk.paths import PathValues
from multiwoven_python_sdk.apis.paths.api_v1_models import ApiV1Models
from multiwoven_python_sdk.apis.paths.api_v1_models_id import ApiV1ModelsId
from multiwoven_python_sdk.apis.paths.api_v1_connector_definitions import ApiV1ConnectorDefinitions
from multiwoven_python_sdk.apis.paths.api_v1_connector_definitions_connector_name import ApiV1ConnectorDefinitionsConnectorName
from multiwoven_python_sdk.apis.paths.api_v1_connector_definitions_check_connection import ApiV1ConnectorDefinitionsCheckConnection
from multiwoven_python_sdk.apis.paths.api_v1_connectors import ApiV1Connectors
from multiwoven_python_sdk.apis.paths.api_v1_connectors_id import ApiV1ConnectorsId
from multiwoven_python_sdk.apis.paths.api_v1_connectors_id_discover import ApiV1ConnectorsIdDiscover
from multiwoven_python_sdk.apis.paths.api_v1_connectors_id_query_source import ApiV1ConnectorsIdQuerySource
from multiwoven_python_sdk.apis.paths.api_v1_syncs import ApiV1Syncs
from multiwoven_python_sdk.apis.paths.api_v1_syncs_id import ApiV1SyncsId
from multiwoven_python_sdk.apis.paths.api_v1_syncs_configurations import ApiV1SyncsConfigurations
from multiwoven_python_sdk.apis.paths.api_v1_reports import ApiV1Reports
from multiwoven_python_sdk.apis.paths.api_v1_syncs_sync_id_sync_runs import ApiV1SyncsSyncIdSyncRuns
from multiwoven_python_sdk.apis.paths.api_v1_syncs_sync_id_sync_runs_sync_run_id_sync_records import ApiV1SyncsSyncIdSyncRunsSyncRunIdSyncRecords

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_MODELS: ApiV1Models,
        PathValues.API_V1_MODELS_ID: ApiV1ModelsId,
        PathValues.API_V1_CONNECTOR_DEFINITIONS: ApiV1ConnectorDefinitions,
        PathValues.API_V1_CONNECTOR_DEFINITIONS_CONNECTOR_NAME: ApiV1ConnectorDefinitionsConnectorName,
        PathValues.API_V1_CONNECTOR_DEFINITIONS_CHECK_CONNECTION: ApiV1ConnectorDefinitionsCheckConnection,
        PathValues.API_V1_CONNECTORS: ApiV1Connectors,
        PathValues.API_V1_CONNECTORS_ID: ApiV1ConnectorsId,
        PathValues.API_V1_CONNECTORS_ID_DISCOVER: ApiV1ConnectorsIdDiscover,
        PathValues.API_V1_CONNECTORS_ID_QUERY_SOURCE: ApiV1ConnectorsIdQuerySource,
        PathValues.API_V1_SYNCS: ApiV1Syncs,
        PathValues.API_V1_SYNCS_ID: ApiV1SyncsId,
        PathValues.API_V1_SYNCS_CONFIGURATIONS: ApiV1SyncsConfigurations,
        PathValues.API_V1_REPORTS: ApiV1Reports,
        PathValues.API_V1_SYNCS_SYNC_ID_SYNC_RUNS: ApiV1SyncsSyncIdSyncRuns,
        PathValues.API_V1_SYNCS_SYNC_ID_SYNC_RUNS_SYNC_RUN_ID_SYNC_RECORDS: ApiV1SyncsSyncIdSyncRunsSyncRunIdSyncRecords,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_MODELS: ApiV1Models,
        PathValues.API_V1_MODELS_ID: ApiV1ModelsId,
        PathValues.API_V1_CONNECTOR_DEFINITIONS: ApiV1ConnectorDefinitions,
        PathValues.API_V1_CONNECTOR_DEFINITIONS_CONNECTOR_NAME: ApiV1ConnectorDefinitionsConnectorName,
        PathValues.API_V1_CONNECTOR_DEFINITIONS_CHECK_CONNECTION: ApiV1ConnectorDefinitionsCheckConnection,
        PathValues.API_V1_CONNECTORS: ApiV1Connectors,
        PathValues.API_V1_CONNECTORS_ID: ApiV1ConnectorsId,
        PathValues.API_V1_CONNECTORS_ID_DISCOVER: ApiV1ConnectorsIdDiscover,
        PathValues.API_V1_CONNECTORS_ID_QUERY_SOURCE: ApiV1ConnectorsIdQuerySource,
        PathValues.API_V1_SYNCS: ApiV1Syncs,
        PathValues.API_V1_SYNCS_ID: ApiV1SyncsId,
        PathValues.API_V1_SYNCS_CONFIGURATIONS: ApiV1SyncsConfigurations,
        PathValues.API_V1_REPORTS: ApiV1Reports,
        PathValues.API_V1_SYNCS_SYNC_ID_SYNC_RUNS: ApiV1SyncsSyncIdSyncRuns,
        PathValues.API_V1_SYNCS_SYNC_ID_SYNC_RUNS_SYNC_RUN_ID_SYNC_RECORDS: ApiV1SyncsSyncIdSyncRunsSyncRunIdSyncRecords,
    }
)
