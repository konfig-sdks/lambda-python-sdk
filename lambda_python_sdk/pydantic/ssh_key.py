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

from lambda_python_sdk.pydantic.ssh_key_name import SshKeyName
from lambda_python_sdk.pydantic.ssh_private_key import SshPrivateKey
from lambda_python_sdk.pydantic.ssh_public_key import SshPublicKey

class SshKey(BaseModel):
    # Unique identifier (ID) of an SSH key
    id: str = Field(alias='id')

    name: SshKeyName = Field(alias='name')

    public_key: SshPublicKey = Field(alias='public_key')

    private_key: typing.Optional[SshPrivateKey] = Field(None, alias='private_key')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )