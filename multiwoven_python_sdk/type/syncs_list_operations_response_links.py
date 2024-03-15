# coding: utf-8

"""
    MultiWoven API

    Open-source Reverse ETL that makes data segmentation, sync and activation both easy and fully secure.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


RequiredSyncsListOperationsResponseLinks = TypedDict("RequiredSyncsListOperationsResponseLinks", {
    })

OptionalSyncsListOperationsResponseLinks = TypedDict("OptionalSyncsListOperationsResponseLinks", {
    "self": str,

    "first": str,

    "prev": str,

    "next": str,

    "last": str,
    }, total=False)

class SyncsListOperationsResponseLinks(RequiredSyncsListOperationsResponseLinks, OptionalSyncsListOperationsResponseLinks):
    pass
