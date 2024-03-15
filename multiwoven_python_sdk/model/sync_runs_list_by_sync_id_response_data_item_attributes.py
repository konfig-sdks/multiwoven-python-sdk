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


class SyncRunsListBySyncIdResponseDataItemAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            sync_id = schemas.IntSchema
            status = schemas.StrSchema
            started_at = schemas.DateTimeSchema
            finished_at = schemas.DateTimeSchema
            duration = schemas.Float32Schema
            total_query_rows = schemas.IntSchema
            total_rows = schemas.IntSchema
            successful_rows = schemas.IntSchema
            failed_rows = schemas.IntSchema
            
            
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
                "status": status,
                "started_at": started_at,
                "finished_at": finished_at,
                "duration": duration,
                "total_query_rows": total_query_rows,
                "total_rows": total_rows,
                "successful_rows": successful_rows,
                "failed_rows": failed_rows,
                "error": error,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_id"]) -> MetaOapg.properties.sync_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["started_at"]) -> MetaOapg.properties.started_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finished_at"]) -> MetaOapg.properties.finished_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_query_rows"]) -> MetaOapg.properties.total_query_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_rows"]) -> MetaOapg.properties.total_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["successful_rows"]) -> MetaOapg.properties.successful_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failed_rows"]) -> MetaOapg.properties.failed_rows: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sync_id", "status", "started_at", "finished_at", "duration", "total_query_rows", "total_rows", "successful_rows", "failed_rows", "error", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_id"]) -> typing.Union[MetaOapg.properties.sync_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["started_at"]) -> typing.Union[MetaOapg.properties.started_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finished_at"]) -> typing.Union[MetaOapg.properties.finished_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_query_rows"]) -> typing.Union[MetaOapg.properties.total_query_rows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_rows"]) -> typing.Union[MetaOapg.properties.total_rows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["successful_rows"]) -> typing.Union[MetaOapg.properties.successful_rows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failed_rows"]) -> typing.Union[MetaOapg.properties.failed_rows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sync_id", "status", "started_at", "finished_at", "duration", "total_query_rows", "total_rows", "successful_rows", "failed_rows", "error", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sync_id: typing.Union[MetaOapg.properties.sync_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        started_at: typing.Union[MetaOapg.properties.started_at, str, datetime, schemas.Unset] = schemas.unset,
        finished_at: typing.Union[MetaOapg.properties.finished_at, str, datetime, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        total_query_rows: typing.Union[MetaOapg.properties.total_query_rows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_rows: typing.Union[MetaOapg.properties.total_rows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        successful_rows: typing.Union[MetaOapg.properties.successful_rows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        failed_rows: typing.Union[MetaOapg.properties.failed_rows, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, None, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SyncRunsListBySyncIdResponseDataItemAttributes':
        return super().__new__(
            cls,
            *args,
            sync_id=sync_id,
            status=status,
            started_at=started_at,
            finished_at=finished_at,
            duration=duration,
            total_query_rows=total_query_rows,
            total_rows=total_rows,
            successful_rows=successful_rows,
            failed_rows=failed_rows,
            error=error,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )