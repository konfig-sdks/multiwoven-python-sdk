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


class SyncRecordsListForSyncRunResponseDataItemAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            sync_id = schemas.IntSchema
            sync_run_id = schemas.IntSchema
        
            @staticmethod
            def record() -> typing.Type['SyncRecordsListForSyncRunResponseDataItemAttributesRecord']:
                return SyncRecordsListForSyncRunResponseDataItemAttributesRecord
            status = schemas.StrSchema
            action = schemas.StrSchema
            
            
            class error(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "sync_id": sync_id,
                "sync_run_id": sync_run_id,
                "record": record,
                "status": status,
                "action": action,
                "error": error,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_id"]) -> MetaOapg.properties.sync_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_run_id"]) -> MetaOapg.properties.sync_run_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["record"]) -> 'SyncRecordsListForSyncRunResponseDataItemAttributesRecord': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sync_id", "sync_run_id", "record", "status", "action", "error", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_id"]) -> typing.Union[MetaOapg.properties.sync_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_run_id"]) -> typing.Union[MetaOapg.properties.sync_run_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["record"]) -> typing.Union['SyncRecordsListForSyncRunResponseDataItemAttributesRecord', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sync_id", "sync_run_id", "record", "status", "action", "error", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sync_id: typing.Union[MetaOapg.properties.sync_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sync_run_id: typing.Union[MetaOapg.properties.sync_run_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        record: typing.Union['SyncRecordsListForSyncRunResponseDataItemAttributesRecord', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, None, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SyncRecordsListForSyncRunResponseDataItemAttributes':
        return super().__new__(
            cls,
            *args,
            sync_id=sync_id,
            sync_run_id=sync_run_id,
            record=record,
            status=status,
            action=action,
            error=error,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )

from multiwoven_python_sdk.model.sync_records_list_for_sync_run_response_data_item_attributes_record import SyncRecordsListForSyncRunResponseDataItemAttributesRecord
