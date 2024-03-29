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


class ConnectorsDiscoverCatalogInfoResponseDataAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            connector_id = schemas.IntSchema
            workspace_id = schemas.IntSchema
        
            @staticmethod
            def catalog() -> typing.Type['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog']:
                return ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog
            catalog_hash = schemas.StrSchema
            __annotations__ = {
                "connector_id": connector_id,
                "workspace_id": workspace_id,
                "catalog": catalog,
                "catalog_hash": catalog_hash,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connector_id"]) -> MetaOapg.properties.connector_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalog"]) -> 'ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalog_hash"]) -> MetaOapg.properties.catalog_hash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["connector_id", "workspace_id", "catalog", "catalog_hash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connector_id"]) -> typing.Union[MetaOapg.properties.connector_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalog"]) -> typing.Union['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalog_hash"]) -> typing.Union[MetaOapg.properties.catalog_hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["connector_id", "workspace_id", "catalog", "catalog_hash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        connector_id: typing.Union[MetaOapg.properties.connector_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        catalog: typing.Union['ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog', schemas.Unset] = schemas.unset,
        catalog_hash: typing.Union[MetaOapg.properties.catalog_hash, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectorsDiscoverCatalogInfoResponseDataAttributes':
        return super().__new__(
            cls,
            *args,
            connector_id=connector_id,
            workspace_id=workspace_id,
            catalog=catalog,
            catalog_hash=catalog_hash,
            _configuration=_configuration,
            **kwargs,
        )

from multiwoven_python_sdk.model.connectors_discover_catalog_info_response_data_attributes_catalog import ConnectorsDiscoverCatalogInfoResponseDataAttributesCatalog
