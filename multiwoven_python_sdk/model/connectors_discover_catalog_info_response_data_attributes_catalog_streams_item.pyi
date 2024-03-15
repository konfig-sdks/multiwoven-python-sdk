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


class ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            action = schemas.StrSchema
        
            @staticmethod
            def json_schema() -> typing.Type['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema']:
                return ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema
            url = schemas.StrSchema
            request_method = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "action": action,
                "json_schema": json_schema,
                "url": url,
                "request_method": request_method,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["json_schema"]) -> 'ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_method"]) -> MetaOapg.properties.request_method: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "action", "json_schema", "url", "request_method", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["json_schema"]) -> typing.Union['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_method"]) -> typing.Union[MetaOapg.properties.request_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "action", "json_schema", "url", "request_method", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        json_schema: typing.Union['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema', schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        request_method: typing.Union[MetaOapg.properties.request_method, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItem':
        return super().__new__(
            cls,
            *args,
            name=name,
            action=action,
            json_schema=json_schema,
            url=url,
            request_method=request_method,
            _configuration=_configuration,
            **kwargs,
        )

from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog_streams_item_json_schema import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalogStreamsItemJsonSchema