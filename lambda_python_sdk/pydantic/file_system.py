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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lambda_python_sdk.pydantic.region import Region
from lambda_python_sdk.pydantic.user import User

class FileSystem(BaseModel):
    # Unique identifier (ID) of a file system
    id: str = Field(alias='id')

    # Name of a file system
    name: str = Field(alias='name')

    # A date and time, formatted as an ISO 8601 time stamp
    created: str = Field(alias='created')

    created_by: User = Field(alias='created_by')

    # Absolute path indicating where on instances the file system will be mounted
    mount_point: str = Field(alias='mount_point')

    region: Region = Field(alias='region')

    # Whether the file system is currently in use by an instance. File systems that are in use cannot be deleted.
    is_in_use: bool = Field(alias='is_in_use')

    # Approximate amount of storage used by the file system, in bytes. This value is an estimate that is updated every several hours.
    bytes_used: typing.Optional[int] = Field(None, alias='bytes_used')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )