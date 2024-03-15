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


class SyncsCreateNewSyncOperationResponseAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            source_id = schemas.IntSchema
            destination_id = schemas.IntSchema
            model_id = schemas.IntSchema
        
            @staticmethod
            def configuration() -> typing.Type['SyncsCreateNewSyncOperationResponseAttributesConfiguration']:
                return SyncsCreateNewSyncOperationResponseAttributesConfiguration
            
            
            class schedule_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "automated": "AUTOMATED",
                    }
                
                @schemas.classproperty
                def AUTOMATED(cls):
                    return cls("automated")
            
            
            class sync_mode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "full_refresh": "FULL_REFRESH",
                    }
                
                @schemas.classproperty
                def FULL_REFRESH(cls):
                    return cls("full_refresh")
            sync_interval = schemas.IntSchema
            
            
            class sync_interval_unit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "minutes": "MINUTES",
                    }
                
                @schemas.classproperty
                def MINUTES(cls):
                    return cls("minutes")
            stream_name = schemas.StrSchema
            status = schemas.StrSchema
            __annotations__ = {
                "source_id": source_id,
                "destination_id": destination_id,
                "model_id": model_id,
                "configuration": configuration,
                "schedule_type": schedule_type,
                "sync_mode": sync_mode,
                "sync_interval": sync_interval,
                "sync_interval_unit": sync_interval_unit,
                "stream_name": stream_name,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination_id"]) -> MetaOapg.properties.destination_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'SyncsCreateNewSyncOperationResponseAttributesConfiguration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule_type"]) -> MetaOapg.properties.schedule_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_mode"]) -> MetaOapg.properties.sync_mode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_interval"]) -> MetaOapg.properties.sync_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sync_interval_unit"]) -> MetaOapg.properties.sync_interval_unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_name"]) -> MetaOapg.properties.stream_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["source_id", "destination_id", "model_id", "configuration", "schedule_type", "sync_mode", "sync_interval", "sync_interval_unit", "stream_name", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination_id"]) -> typing.Union[MetaOapg.properties.destination_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> typing.Union[MetaOapg.properties.model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['SyncsCreateNewSyncOperationResponseAttributesConfiguration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule_type"]) -> typing.Union[MetaOapg.properties.schedule_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_mode"]) -> typing.Union[MetaOapg.properties.sync_mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_interval"]) -> typing.Union[MetaOapg.properties.sync_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sync_interval_unit"]) -> typing.Union[MetaOapg.properties.sync_interval_unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_name"]) -> typing.Union[MetaOapg.properties.stream_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["source_id", "destination_id", "model_id", "configuration", "schedule_type", "sync_mode", "sync_interval", "sync_interval_unit", "stream_name", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        source_id: typing.Union[MetaOapg.properties.source_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        destination_id: typing.Union[MetaOapg.properties.destination_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        model_id: typing.Union[MetaOapg.properties.model_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        configuration: typing.Union['SyncsCreateNewSyncOperationResponseAttributesConfiguration', schemas.Unset] = schemas.unset,
        schedule_type: typing.Union[MetaOapg.properties.schedule_type, str, schemas.Unset] = schemas.unset,
        sync_mode: typing.Union[MetaOapg.properties.sync_mode, str, schemas.Unset] = schemas.unset,
        sync_interval: typing.Union[MetaOapg.properties.sync_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sync_interval_unit: typing.Union[MetaOapg.properties.sync_interval_unit, str, schemas.Unset] = schemas.unset,
        stream_name: typing.Union[MetaOapg.properties.stream_name, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SyncsCreateNewSyncOperationResponseAttributes':
        return super().__new__(
            cls,
            *args,
            source_id=source_id,
            destination_id=destination_id,
            model_id=model_id,
            configuration=configuration,
            schedule_type=schedule_type,
            sync_mode=sync_mode,
            sync_interval=sync_interval,
            sync_interval_unit=sync_interval_unit,
            stream_name=stream_name,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from multiwoven_python_sdk.model.syncs_create_new_sync_operation_response_attributes_configuration import SyncsCreateNewSyncOperationResponseAttributesConfiguration
