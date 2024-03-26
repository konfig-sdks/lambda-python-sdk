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

from lambda_python_sdk.type.ssh_key import SshKey

class RequiredKeyAddSshKeyResponse(TypedDict):
    data: SshKey

class OptionalKeyAddSshKeyResponse(TypedDict, total=False):
    pass

class KeyAddSshKeyResponse(RequiredKeyAddSshKeyResponse, OptionalKeyAddSshKeyResponse):
    pass