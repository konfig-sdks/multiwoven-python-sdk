<div align="left">

[![Visit Multiwoven](./header.png)](https://www.multiwoven.com&#x2F;)

# Multiwoven<a id="multiwoven"></a>

Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`multiwoven.connector_definitions.check_connection`](#multiwovenconnector_definitionscheck_connection)
  * [`multiwoven.connector_definitions.get_based_on_type`](#multiwovenconnector_definitionsget_based_on_type)
  * [`multiwoven.connector_definitions.get_by_name`](#multiwovenconnector_definitionsget_by_name)
  * [`multiwoven.connectors.create_new_connector`](#multiwovenconnectorscreate_new_connector)
  * [`multiwoven.connectors.delete_by_id`](#multiwovenconnectorsdelete_by_id)
  * [`multiwoven.connectors.discover_catalog_info`](#multiwovenconnectorsdiscover_catalog_info)
  * [`multiwoven.connectors.get_by_id`](#multiwovenconnectorsget_by_id)
  * [`multiwoven.connectors.list_all`](#multiwovenconnectorslist_all)
  * [`multiwoven.connectors.query_source`](#multiwovenconnectorsquery_source)
  * [`multiwoven.connectors.update_by_id`](#multiwovenconnectorsupdate_by_id)
  * [`multiwoven.models.create_model`](#multiwovenmodelscreate_model)
  * [`multiwoven.models.delete_model`](#multiwovenmodelsdelete_model)
  * [`multiwoven.models.get_by_id`](#multiwovenmodelsget_by_id)
  * [`multiwoven.models.list_all_models`](#multiwovenmodelslist_all_models)
  * [`multiwoven.models.update_model_by_id`](#multiwovenmodelsupdate_model_by_id)
  * [`multiwoven.reports.get_data_based_on_type`](#multiwovenreportsget_data_based_on_type)
  * [`multiwoven.sync_records.list_for_sync_run`](#multiwovensync_recordslist_for_sync_run)
  * [`multiwoven.sync_runs.list_by_sync_id`](#multiwovensync_runslist_by_sync_id)
  * [`multiwoven.syncs.create_new_sync_operation`](#multiwovensyncscreate_new_sync_operation)
  * [`multiwoven.syncs.delete_sync_operation`](#multiwovensyncsdelete_sync_operation)
  * [`multiwoven.syncs.get_report_data`](#multiwovensyncsget_report_data)
  * [`multiwoven.syncs.list_operations`](#multiwovensyncslist_operations)
  * [`multiwoven.syncs.show_details`](#multiwovensyncsshow_details)
  * [`multiwoven.syncs.update_specific_sync`](#multiwovensyncsupdate_specific_sync)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Multiwoven&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from multiwoven_python_sdk import Multiwoven, ApiException

multiwoven = Multiwoven(access_token="YOUR_BEARER_TOKEN")

try:
    # Checks the connection for a specified connector definition
    check_connection_response = multiwoven.connector_definitions.check_connection(
        type="source",
        name="string_example",
        connection_spec={},
    )
    print(check_connection_response)
except ApiException as e:
    print("Exception when calling ConnectorDefinitionsApi.check_connection: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from multiwoven_python_sdk import Multiwoven, ApiException

multiwoven = Multiwoven(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Checks the connection for a specified connector definition
        check_connection_response = (
            await multiwoven.connector_definitions.acheck_connection(
                type="source",
                name="string_example",
                connection_spec={},
            )
        )
        print(check_connection_response)
    except ApiException as e:
        print(
            "Exception when calling ConnectorDefinitionsApi.check_connection: %s\n" % e
        )
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from multiwoven_python_sdk import Multiwoven, ApiException

multiwoven = Multiwoven(access_token="YOUR_BEARER_TOKEN")

try:
    # Checks the connection for a specified connector definition
    check_connection_response = multiwoven.connector_definitions.raw.check_connection(
        type="source",
        name="string_example",
        connection_spec={},
    )
    pprint(check_connection_response.body)
    pprint(check_connection_response.body["result"])
    pprint(check_connection_response.body["details"])
    pprint(check_connection_response.headers)
    pprint(check_connection_response.status)
    pprint(check_connection_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ConnectorDefinitionsApi.check_connection: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `multiwoven.connector_definitions.check_connection`<a id="multiwovenconnector_definitionscheck_connection"></a>

Checks the connection for a specified connector definition

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_connection_response = multiwoven.connector_definitions.check_connection(
    type="source",
    name="string_example",
    connection_spec={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### name: `str`<a id="name-str"></a>

##### connection_spec: [`ConnectorDefinitionsCheckConnectionRequestConnectionSpec`](./multiwoven_python_sdk/type/connector_definitions_check_connection_request_connection_spec.py)<a id="connection_spec-connectordefinitionscheckconnectionrequestconnectionspecmultiwoven_python_sdktypeconnector_definitions_check_connection_request_connection_specpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectorDefinitionsCheckConnectionRequest`](./multiwoven_python_sdk/type/connector_definitions_check_connection_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorDefinitionsCheckConnectionResponse`](./multiwoven_python_sdk/pydantic/connector_definitions_check_connection_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connector_definitions/check_connection` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connector_definitions.get_based_on_type`<a id="multiwovenconnector_definitionsget_based_on_type"></a>

Retrieve connector definitions based on type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_based_on_type_response = multiwoven.connector_definitions.get_based_on_type(
    type="source",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of the connector (source or destination)

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorDefinitionsGetBasedOnTypeResponse`](./multiwoven_python_sdk/pydantic/connector_definitions_get_based_on_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connector_definitions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connector_definitions.get_by_name`<a id="multiwovenconnector_definitionsget_by_name"></a>

Retrieve specific connector definition based on its name

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_name_response = multiwoven.connector_definitions.get_by_name(
    connector_name="connector_name_example",
    type="source",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### connector_name: `str`<a id="connector_name-str"></a>

Name of the connector

##### type: `str`<a id="type-str"></a>

Type of the connector (source or destination)

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorDefinitionsGetByNameResponse`](./multiwoven_python_sdk/pydantic/connector_definitions_get_by_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connector_definitions/{connector_name}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.create_new_connector`<a id="multiwovenconnectorscreate_new_connector"></a>

Creates a connector

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_connector_response = multiwoven.connectors.create_new_connector(
    connector={
        "name": "name_example",
        "connector_type": "source",
        "connector_name": "connector_name_example",
        "configuration": {},
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### connector: [`ConnectorsCreateNewConnectorRequestConnector`](./multiwoven_python_sdk/type/connectors_create_new_connector_request_connector.py)<a id="connector-connectorscreatenewconnectorrequestconnectormultiwoven_python_sdktypeconnectors_create_new_connector_request_connectorpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectorsCreateNewConnectorRequest`](./multiwoven_python_sdk/type/connectors_create_new_connector_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsCreateNewConnectorResponse`](./multiwoven_python_sdk/pydantic/connectors_create_new_connector_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.delete_by_id`<a id="multiwovenconnectorsdelete_by_id"></a>

Deletes a specific connector by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
multiwoven.connectors.delete_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique ID of the connector

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.discover_catalog_info`<a id="multiwovenconnectorsdiscover_catalog_info"></a>

Discovers catalog information for a specified connector

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
discover_catalog_info_response = multiwoven.connectors.discover_catalog_info(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique ID of the connector

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsDiscoverCatalogInfoResponse`](./multiwoven_python_sdk/pydantic/connectors_discover_catalog_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors/{id}/discover` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.get_by_id`<a id="multiwovenconnectorsget_by_id"></a>

Retrieves a specific connector by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = multiwoven.connectors.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique ID of the connector

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsGetByIdResponse`](./multiwoven_python_sdk/pydantic/connectors_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.list_all`<a id="multiwovenconnectorslist_all"></a>

Lists all connectors

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = multiwoven.connectors.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsListAllResponse`](./multiwoven_python_sdk/pydantic/connectors_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.query_source`<a id="multiwovenconnectorsquery_source"></a>

Query your source data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_source_response = multiwoven.connectors.query_source(
    id=1,
    query="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

The ID of the connector to query

##### query: `str`<a id="query-str"></a>

SQL query to be executed

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectorsQuerySourceRequest`](./multiwoven_python_sdk/type/connectors_query_source_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsQuerySourceResponse`](./multiwoven_python_sdk/pydantic/connectors_query_source_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors/{id}/query_source` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.connectors.update_by_id`<a id="multiwovenconnectorsupdate_by_id"></a>

Updates a specific connector by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_by_id_response = multiwoven.connectors.update_by_id(
    id="id_example",
    connector={
        "name": "name_example",
        "connector_type": "source",
        "configuration": {},
        "connector_name": "connector_name_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Unique ID of the connector

##### connector: [`ConnectorsUpdateByIdRequestConnector`](./multiwoven_python_sdk/type/connectors_update_by_id_request_connector.py)<a id="connector-connectorsupdatebyidrequestconnectormultiwoven_python_sdktypeconnectors_update_by_id_request_connectorpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ConnectorsUpdateByIdRequest`](./multiwoven_python_sdk/type/connectors_update_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ConnectorsUpdateByIdResponse`](./multiwoven_python_sdk/pydantic/connectors_update_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/connectors/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.models.create_model`<a id="multiwovenmodelscreate_model"></a>

Creates a model

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_model_response = multiwoven.models.create_model(
    model={
        "name": "name_example",
        "query": "query_example",
        "query_type": "query_type_example",
        "connector_id": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`ModelsCreateModelRequestModel`](./multiwoven_python_sdk/type/models_create_model_request_model.py)<a id="model-modelscreatemodelrequestmodelmultiwoven_python_sdktypemodels_create_model_request_modelpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ModelsCreateModelRequest`](./multiwoven_python_sdk/type/models_create_model_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ModelsCreateModelResponse`](./multiwoven_python_sdk/pydantic/models_create_model_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/models` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.models.delete_model`<a id="multiwovenmodelsdelete_model"></a>

Deletes a model

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
multiwoven.models.delete_model(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/models/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.models.get_by_id`<a id="multiwovenmodelsget_by_id"></a>

Retrieves a model

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = multiwoven.models.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ModelsGetByIdResponse`](./multiwoven_python_sdk/pydantic/models_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/models/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.models.list_all_models`<a id="multiwovenmodelslist_all_models"></a>

Lists all models

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_models_response = multiwoven.models.list_all_models()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ModelsListAllModelsResponse`](./multiwoven_python_sdk/pydantic/models_list_all_models_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/models` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.models.update_model_by_id`<a id="multiwovenmodelsupdate_model_by_id"></a>

Updates a model

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_model_by_id_response = multiwoven.models.update_model_by_id(
    id=1,
    model={
        "name": "name_example",
        "query": "query_example",
        "query_type": "query_type_example",
        "connector_id": 1,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

##### model: [`ModelsUpdateModelByIdRequestModel`](./multiwoven_python_sdk/type/models_update_model_by_id_request_model.py)<a id="model-modelsupdatemodelbyidrequestmodelmultiwoven_python_sdktypemodels_update_model_by_id_request_modelpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ModelsUpdateModelByIdRequest`](./multiwoven_python_sdk/type/models_update_model_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ModelsUpdateModelByIdResponse`](./multiwoven_python_sdk/pydantic/models_update_model_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/models/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.reports.get_data_based_on_type`<a id="multiwovenreportsget_data_based_on_type"></a>

Get report data based on given type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_based_on_type_response = multiwoven.reports.get_data_based_on_type(
    type="workspace_activity",
    metric="sync_run_triggered",
    connector_ids=[1],
    time_period="one_week",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of the report to query.

##### metric: `str`<a id="metric-str"></a>

Specific metric of interest in the report.

##### connector_ids: List[`int`]<a id="connector_ids-listint"></a>

IDs of the connectors.

##### time_period: `str`<a id="time_period-str"></a>

Time period for the report.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetDataBasedOnTypeResponse`](./multiwoven_python_sdk/pydantic/reports_get_data_based_on_type_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.sync_records.list_for_sync_run`<a id="multiwovensync_recordslist_for_sync_run"></a>

Retrieves a list of sync records for a specific sync run, optionally filtered by status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_for_sync_run_response = multiwoven.sync_records.list_for_sync_run(
    sync_id=1,
    sync_run_id=1,
    status="string_example",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sync_id: `int`<a id="sync_id-int"></a>

The ID of the sync to list records for.

##### sync_run_id: `int`<a id="sync_run_id-int"></a>

The ID of the sync run to list records for.

##### status: `str`<a id="status-str"></a>

Optional status to filter the sync records by.

##### page: `int`<a id="page-int"></a>

Page number for pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`SyncRecordsListForSyncRunResponse`](./multiwoven_python_sdk/pydantic/sync_records_list_for_sync_run_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}/sync_records` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.sync_runs.list_by_sync_id`<a id="multiwovensync_runslist_by_sync_id"></a>

Retrieves a list of sync runs for a specific sync, optionally filtered by status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_sync_id_response = multiwoven.sync_runs.list_by_sync_id(
    sync_id=1,
    status="string_example",
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sync_id: `int`<a id="sync_id-int"></a>

The ID of the sync to list runs for.

##### status: `str`<a id="status-str"></a>

Optional status to filter the sync runs by.

##### page: `int`<a id="page-int"></a>

Page number for pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`SyncRunsListBySyncIdResponse`](./multiwoven_python_sdk/pydantic/sync_runs_list_by_sync_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/{sync_id}/sync_runs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.create_new_sync_operation`<a id="multiwovensyncscreate_new_sync_operation"></a>

Create a new sync operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_sync_operation_response = multiwoven.syncs.create_new_sync_operation(
    sync={
        "source_id": 1,
        "destination_id": 1,
        "model_id": 1,
        "schedule_type": "automated",
        "configuration": {},
        "stream_name": "stream_name_example",
        "sync_mode": "full_refresh",
        "sync_interval": 1,
        "sync_interval_unit": "minutes",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sync: [`SyncsCreateNewSyncOperationRequestSync`](./multiwoven_python_sdk/type/syncs_create_new_sync_operation_request_sync.py)<a id="sync-syncscreatenewsyncoperationrequestsyncmultiwoven_python_sdktypesyncs_create_new_sync_operation_request_syncpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SyncsCreateNewSyncOperationRequest`](./multiwoven_python_sdk/type/syncs_create_new_sync_operation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SyncsCreateNewSyncOperationResponse`](./multiwoven_python_sdk/pydantic/syncs_create_new_sync_operation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.delete_sync_operation`<a id="multiwovensyncsdelete_sync_operation"></a>

Delete a specific sync operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
multiwoven.syncs.delete_sync_operation(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the sync operation to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.get_report_data`<a id="multiwovensyncsget_report_data"></a>

Get report data based on given type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_data_response = multiwoven.syncs.get_report_data()
```

#### 🔄 Return<a id="🔄-return"></a>

[`SyncsGetReportDataResponse`](./multiwoven_python_sdk/pydantic/syncs_get_report_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/configurations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.list_operations`<a id="multiwovensyncslist_operations"></a>

List all sync operations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_operations_response = multiwoven.syncs.list_operations(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

Page number for pagination

##### page_size: `int`<a id="page_size-int"></a>

Number of items per page for pagination

#### 🔄 Return<a id="🔄-return"></a>

[`SyncsListOperationsResponse`](./multiwoven_python_sdk/pydantic/syncs_list_operations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.show_details`<a id="multiwovensyncsshow_details"></a>

Show details of a specific sync operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_response = multiwoven.syncs.show_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SyncsShowDetailsResponse`](./multiwoven_python_sdk/pydantic/syncs_show_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `multiwoven.syncs.update_specific_sync`<a id="multiwovensyncsupdate_specific_sync"></a>

Update a specific sync operation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_specific_sync_response = multiwoven.syncs.update_specific_sync(
    id="id_example",
    sync={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### sync: [`SyncsUpdateSpecificSyncRequestSync`](./multiwoven_python_sdk/type/syncs_update_specific_sync_request_sync.py)<a id="sync-syncsupdatespecificsyncrequestsyncmultiwoven_python_sdktypesyncs_update_specific_sync_request_syncpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SyncsUpdateSpecificSyncRequest`](./multiwoven_python_sdk/type/syncs_update_specific_sync_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SyncsUpdateSpecificSyncResponse`](./multiwoven_python_sdk/pydantic/syncs_update_specific_sync_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v1/syncs/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
