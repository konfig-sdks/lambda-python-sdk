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

from lambda_python_sdk.type.instance import Instance

class RequiredInstanceGetDetailsResponse(TypedDict):
    data: Instance

class OptionalInstanceGetDetailsResponse(TypedDict, total=False):
    pass

class InstanceGetDetailsResponse(RequiredInstanceGetDetailsResponse, OptionalInstanceGetDetailsResponse):
    pass
