# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from multiwoven_python_sdk import schemas  # noqa: F401


class ConnectorsListAllResponseDataItemAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            connector_type = schemas.StrSchema
            workspace_id = schemas.IntSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
        
            @staticmethod
            def configuration() -> typing.Type['ConnectorsListAllResponseDataItemAttributesConfiguration']:
                return ConnectorsListAllResponseDataItemAttributesConfiguration
            connector_name = schemas.StrSchema
            icon = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "connector_type": connector_type,
                "workspace_id": workspace_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "configuration": configuration,
                "connector_name": connector_name,
                "icon": icon,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connector_type"]) -> MetaOapg.properties.connector_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'ConnectorsListAllResponseDataItemAttributesConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connector_name"]) -> MetaOapg.properties.connector_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "connector_type", "workspace_id", "created_at", "updated_at", "configuration", "connector_name", "icon", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connector_type"]) -> typing.Union[MetaOapg.properties.connector_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['ConnectorsListAllResponseDataItemAttributesConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connector_name"]) -> typing.Union[MetaOapg.properties.connector_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "connector_type", "workspace_id", "created_at", "updated_at", "configuration", "connector_name", "icon", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        connector_type: typing.Union[MetaOapg.properties.connector_type, str, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        configuration: typing.Union['ConnectorsListAllResponseDataItemAttributesConfiguration', schemas.Unset] = schemas.unset,
        connector_name: typing.Union[MetaOapg.properties.connector_name, str, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectorsListAllResponseDataItemAttributes':
        return super().__new__(
            cls,
            *args,
            name=name,
            connector_type=connector_type,
            workspace_id=workspace_id,
            created_at=created_at,
            updated_at=updated_at,
            configuration=configuration,
            connector_name=connector_name,
            icon=icon,
            _configuration=_configuration,
            **kwargs,
        )

from multiwoven_python_sdk.model.connectors_list_all_response_data_item_attributes_configuration import ConnectorsListAllResponseDataItemAttributesConfiguration
