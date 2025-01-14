# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredRegion(TypedDict):
    # Long name of a region
    description: str

    # Short name of a region
    name: str

class OptionalRegion(TypedDict, total=False):
    pass

class Region(RequiredRegion, OptionalRegion):
    pass
