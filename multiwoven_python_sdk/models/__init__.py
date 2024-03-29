# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from multiwoven_python_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from multiwoven_python_sdk.model.connector_definitions_check_connection_request import ConnectorDefinitionsCheckConnectionRequest
from multiwoven_python_sdk.model.connector_definitions_check_connection_request_connection_spec import ConnectorDefinitionsCheckConnectionRequestConnectionSpec
from multiwoven_python_sdk.model.connector_definitions_check_connection_response import ConnectorDefinitionsCheckConnectionResponse
from multiwoven_python_sdk.model.connector_definitions_get_based_on_type_response import ConnectorDefinitionsGetBasedOnTypeResponse
from multiwoven_python_sdk.model.connector_definitions_get_based_on_type_response_item import ConnectorDefinitionsGetBasedOnTypeResponseItem
from multiwoven_python_sdk.model.connector_definitions_get_based_on_type_response_item_connector_spec import ConnectorDefinitionsGetBasedOnTypeResponseItemConnectorSpec
from multiwoven_python_sdk.model.connector_definitions_get_based_on_type_response_item_connector_spec_connection_specification import ConnectorDefinitionsGetBasedOnTypeResponseItemConnectorSpecConnectionSpecification
from multiwoven_python_sdk.model.connector_definitions_get_based_on_type_response_item_tags import ConnectorDefinitionsGetBasedOnTypeResponseItemTags
from multiwoven_python_sdk.model.connector_definitions_get_by_name_response import ConnectorDefinitionsGetByNameResponse
from multiwoven_python_sdk.model.connector_definitions_get_by_name_response_connector_spec import ConnectorDefinitionsGetByNameResponseConnectorSpec
from multiwoven_python_sdk.model.connector_definitions_get_by_name_response_connector_spec_connection_specification import ConnectorDefinitionsGetByNameResponseConnectorSpecConnectionSpecification
from multiwoven_python_sdk.model.connector_definitions_get_by_name_response_tags import ConnectorDefinitionsGetByNameResponseTags
from multiwoven_python_sdk.model.connectors_create_new_connector_request import ConnectorsCreateNewConnectorRequest
from multiwoven_python_sdk.model.connectors_create_new_connector_request_connector import ConnectorsCreateNewConnectorRequestConnector
from multiwoven_python_sdk.model.connectors_create_new_connector_request_connector_configuration import ConnectorsCreateNewConnectorRequestConnectorConfiguration
from multiwoven_python_sdk.model.connectors_create_new_connector_response import ConnectorsCreateNewConnectorResponse
from multiwoven_python_sdk.model.connectors_create_new_connector_response_data import ConnectorsCreateNewConnectorResponseData
from multiwoven_python_sdk.model.connectors_create_new_connector_response_data_attributes import ConnectorsCreateNewConnectorResponseDataAttributes
from multiwoven_python_sdk.model.connectors_create_new_connector_response_data_attributes_configuration import ConnectorsCreateNewConnectorResponseDataAttributesConfiguration
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response import ConnectorsDiscoverCatalogInfoResponse
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data import ConnectorsDiscoverCatalogInfoResponseData
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes import ConnectorsDiscoverCatalogInfoResponseDataAttributes
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog_streams import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreams
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog_streams_item import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItem
from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog_streams_item_json_schema import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema
from multiwoven_python_sdk.model.connectors_get_by_id_response import ConnectorsGetByIdResponse
from multiwoven_python_sdk.model.connectors_get_by_id_response_data import ConnectorsGetByIdResponseData
from multiwoven_python_sdk.model.connectors_get_by_id_response_data_attributes import ConnectorsGetByIdResponseDataAttributes
from multiwoven_python_sdk.model.connectors_get_by_id_response_data_attributes_configuration import ConnectorsGetByIdResponseDataAttributesConfiguration
from multiwoven_python_sdk.model.connectors_list_all_response import ConnectorsListAllResponse
from multiwoven_python_sdk.model.connectors_list_all_response_data import ConnectorsListAllResponseData
from multiwoven_python_sdk.model.connectors_list_all_response_data_item import ConnectorsListAllResponseDataItem
from multiwoven_python_sdk.model.connectors_list_all_response_data_item_attributes import ConnectorsListAllResponseDataItemAttributes
from multiwoven_python_sdk.model.connectors_list_all_response_data_item_attributes_configuration import ConnectorsListAllResponseDataItemAttributesConfiguration
from multiwoven_python_sdk.model.connectors_list_all_response_links import ConnectorsListAllResponseLinks
from multiwoven_python_sdk.model.connectors_query_source_request import ConnectorsQuerySourceRequest
from multiwoven_python_sdk.model.connectors_query_source_response import ConnectorsQuerySourceResponse
from multiwoven_python_sdk.model.connectors_query_source_response_item import ConnectorsQuerySourceResponseItem
from multiwoven_python_sdk.model.connectors_update_by_id_request import ConnectorsUpdateByIdRequest
from multiwoven_python_sdk.model.connectors_update_by_id_request_connector import ConnectorsUpdateByIdRequestConnector
from multiwoven_python_sdk.model.connectors_update_by_id_request_connector_configuration import ConnectorsUpdateByIdRequestConnectorConfiguration
from multiwoven_python_sdk.model.connectors_update_by_id_response import ConnectorsUpdateByIdResponse
from multiwoven_python_sdk.model.connectors_update_by_id_response_data import ConnectorsUpdateByIdResponseData
from multiwoven_python_sdk.model.connectors_update_by_id_response_data_attributes import ConnectorsUpdateByIdResponseDataAttributes
from multiwoven_python_sdk.model.connectors_update_by_id_response_data_attributes_configuration import ConnectorsUpdateByIdResponseDataAttributesConfiguration
from multiwoven_python_sdk.model.models_create_model_request import ModelsCreateModelRequest
from multiwoven_python_sdk.model.models_create_model_request_model import ModelsCreateModelRequestModel
from multiwoven_python_sdk.model.models_create_model_response import ModelsCreateModelResponse
from multiwoven_python_sdk.model.models_create_model_response_data import ModelsCreateModelResponseData
from multiwoven_python_sdk.model.models_create_model_response_data_attributes import ModelsCreateModelResponseDataAttributes
from multiwoven_python_sdk.model.models_get_by_id_response import ModelsGetByIdResponse
from multiwoven_python_sdk.model.models_get_by_id_response_data import ModelsGetByIdResponseData
from multiwoven_python_sdk.model.models_get_by_id_response_data_attributes import ModelsGetByIdResponseDataAttributes
from multiwoven_python_sdk.model.models_list_all_models_response import ModelsListAllModelsResponse
from multiwoven_python_sdk.model.models_list_all_models_response_data import ModelsListAllModelsResponseData
from multiwoven_python_sdk.model.models_list_all_models_response_data_item import ModelsListAllModelsResponseDataItem
from multiwoven_python_sdk.model.models_list_all_models_response_data_item_attributes import ModelsListAllModelsResponseDataItemAttributes
from multiwoven_python_sdk.model.models_list_all_models_response_links import ModelsListAllModelsResponseLinks
from multiwoven_python_sdk.model.models_update_model_by_id_request import ModelsUpdateModelByIdRequest
from multiwoven_python_sdk.model.models_update_model_by_id_request_model import ModelsUpdateModelByIdRequestModel
from multiwoven_python_sdk.model.models_update_model_by_id_response import ModelsUpdateModelByIdResponse
from multiwoven_python_sdk.model.models_update_model_by_id_response_data import ModelsUpdateModelByIdResponseData
from multiwoven_python_sdk.model.models_update_model_by_id_response_data_attributes import ModelsUpdateModelByIdResponseDataAttributes
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response import ReportsGetDataBasedOnTypeResponse
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response_data import ReportsGetDataBasedOnTypeResponseData
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response_data_sync_run_triggered import ReportsGetDataBasedOnTypeResponseDataSyncRunTriggered
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response_data_sync_run_triggered_item import ReportsGetDataBasedOnTypeResponseDataSyncRunTriggeredItem
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response_data_total_sync_run_rows import ReportsGetDataBasedOnTypeResponseDataTotalSyncRunRows
from multiwoven_python_sdk.model.reports_get_data_based_on_type_response_data_total_sync_run_rows_item import ReportsGetDataBasedOnTypeResponseDataTotalSyncRunRowsItem
from multiwoven_python_sdk.model.sync_records_list_for_sync_run404_response import SyncRecordsListForSyncRun404Response
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response import SyncRecordsListForSyncRunResponse
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_data import SyncRecordsListForSyncRunResponseData
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_data_item import SyncRecordsListForSyncRunResponseDataItem
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_data_item_attributes import SyncRecordsListForSyncRunResponseDataItemAttributes
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_data_item_attributes_record import SyncRecordsListForSyncRunResponseDataItemAttributesRecord
from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_links import SyncRecordsListForSyncRunResponseLinks
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id404_response import SyncRunsListBySyncId404Response
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id_response import SyncRunsListBySyncIdResponse
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id_response_data import SyncRunsListBySyncIdResponseData
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id_response_data_item import SyncRunsListBySyncIdResponseDataItem
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id_response_data_item_attributes import SyncRunsListBySyncIdResponseDataItemAttributes
from multiwoven_python_sdk.model.sync_runs_list_by_sync_id_response_links import SyncRunsListBySyncIdResponseLinks
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_request import SyncsCreateNewSyncOperationRequest
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_request_sync import SyncsCreateNewSyncOperationRequestSync
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_request_sync_configuration import SyncsCreateNewSyncOperationRequestSyncConfiguration
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_response import SyncsCreateNewSyncOperationResponse
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_response_attributes import SyncsCreateNewSyncOperationResponseAttributes
from multiwoven_python_sdk.model.syncs_create_new_sync_operation_response_attributes_configuration import SyncsCreateNewSyncOperationResponseAttributesConfiguration
from multiwoven_python_sdk.model.syncs_get_report_data_response import SyncsGetReportDataResponse
from multiwoven_python_sdk.model.syncs_get_report_data_response_data import SyncsGetReportDataResponseData
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations import SyncsGetReportDataResponseDataConfigurations
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypes
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_static import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesStatic
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_static_boolean import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesStaticBoolean
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_static_null import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesStaticNull
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_static_number import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesStaticNumber
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_static_string import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesStaticString
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplate
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_filter import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateFilter
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_filter_cast import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateFilterCast
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_filter_regex_replace import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateFilterRegexReplace
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_variable import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateVariable
from multiwoven_python_sdk.model.syncs_get_report_data_response_data_configurations_catalog_mapping_types_template_variable_current_timestamp import SyncsGetReportDataResponseDataConfigurationsCatalogMappingTypesTemplateVariableCurrentTimestamp
from multiwoven_python_sdk.model.syncs_list_operations_response import SyncsListOperationsResponse
from multiwoven_python_sdk.model.syncs_list_operations_response_data import SyncsListOperationsResponseData
from multiwoven_python_sdk.model.syncs_list_operations_response_data_item import SyncsListOperationsResponseDataItem
from multiwoven_python_sdk.model.syncs_list_operations_response_data_item_attributes import SyncsListOperationsResponseDataItemAttributes
from multiwoven_python_sdk.model.syncs_list_operations_response_data_item_attributes_configuration import SyncsListOperationsResponseDataItemAttributesConfiguration
from multiwoven_python_sdk.model.syncs_list_operations_response_links import SyncsListOperationsResponseLinks
from multiwoven_python_sdk.model.syncs_show_details_response import SyncsShowDetailsResponse
from multiwoven_python_sdk.model.syncs_show_details_response_attributes import SyncsShowDetailsResponseAttributes
from multiwoven_python_sdk.model.syncs_show_details_response_attributes_configuration import SyncsShowDetailsResponseAttributesConfiguration
from multiwoven_python_sdk.model.syncs_update_specific_sync_request import SyncsUpdateSpecificSyncRequest
from multiwoven_python_sdk.model.syncs_update_specific_sync_request_sync import SyncsUpdateSpecificSyncRequestSync
from multiwoven_python_sdk.model.syncs_update_specific_sync_request_sync_configuration import SyncsUpdateSpecificSyncRequestSyncConfiguration
from multiwoven_python_sdk.model.syncs_update_specific_sync_response import SyncsUpdateSpecificSyncResponse
from multiwoven_python_sdk.model.syncs_update_specific_sync_response_data import SyncsUpdateSpecificSyncResponseData
from multiwoven_python_sdk.model.syncs_update_specific_sync_response_data_attributes import SyncsUpdateSpecificSyncResponseDataAttributes
from multiwoven_python_sdk.model.syncs_update_specific_sync_response_data_attributes_configuration import SyncsUpdateSpecificSyncResponseDataAttributesConfiguration
