# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from multiwoven_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_MODELS = "/api/v1/models"
    API_V1_MODELS_ID = "/api/v1/models/{id}"
    API_V1_CONNECTOR_DEFINITIONS = "/api/v1/connector_definitions"
    API_V1_CONNECTOR_DEFINITIONS_CONNECTOR_NAME = "/api/v1/connector_definitions/{connector_name}"
    API_V1_CONNECTOR_DEFINITIONS_CHECK_CONNECTION = "/api/v1/connector_definitions/check_connection"
    API_V1_CONNECTORS = "/api/v1/connectors"
    API_V1_CONNECTORS_ID = "/api/v1/connectors/{id}"
    API_V1_CONNECTORS_ID_DISCOVER = "/api/v1/connectors/{id}/discover"
    API_V1_CONNECTORS_ID_QUERY_SOURCE = "/api/v1/connectors/{id}/query_source"
    API_V1_SYNCS = "/api/v1/syncs"
    API_V1_SYNCS_ID = "/api/v1/syncs/{id}"
    API_V1_SYNCS_CONFIGURATIONS = "/api/v1/syncs/configurations"
    API_V1_REPORTS = "/api/v1/reports"
    API_V1_SYNCS_SYNC_ID_SYNC_RUNS = "/api/v1/syncs/{sync_id}/sync_runs"
    API_V1_SYNCS_SYNC_ID_SYNC_RUNS_SYNC_RUN_ID_SYNC_RECORDS = "/api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}/sync_records"
