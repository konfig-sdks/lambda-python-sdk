# coding: utf-8
"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from lambda_python_sdk.client_custom import ClientCustom
from lambda_python_sdk.configuration import Configuration
from lambda_python_sdk.api_client import ApiClient
from lambda_python_sdk.type_util import copy_signature
from lambda_python_sdk.apis.tags.file_system_api import FileSystemApi
from lambda_python_sdk.apis.tags.instance_api import InstanceApi
from lambda_python_sdk.apis.tags.instance_type_api import InstanceTypeApi
from lambda_python_sdk.apis.tags.key_api import KeyApi
from lambda_python_sdk.apis.tags.ssh_key_api import SSHKeyApi



class Lambda(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.file_system: FileSystemApi = FileSystemApi(api_client)
        self.instance: InstanceApi = InstanceApi(api_client)
        self.instance_type: InstanceTypeApi = InstanceTypeApi(api_client)
        self.key: KeyApi = KeyApi(api_client)
        self.ssh_key: SSHKeyApi = SSHKeyApi(api_client)