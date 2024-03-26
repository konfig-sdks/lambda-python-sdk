# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
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

from lambda_python_sdk import schemas  # noqa: F401


class InstanceCreateInstancesRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "instance_type_name",
            "region_name",
            "ssh_key_names",
        }
        
        class properties:
            region_name = schemas.StrSchema
            instance_type_name = schemas.StrSchema
            
            
            class ssh_key_names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 1
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['SshKeyName']:
                        return SshKeyName
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SshKeyName'], typing.List['SshKeyName']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ssh_key_names':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SshKeyName':
                    return super().__getitem__(i)
            
            
            class file_system_names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 1
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'file_system_names':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class quantity(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1
                    inclusive_minimum = 1
        
            @staticmethod
            def name() -> typing.Type['InstanceName']:
                return InstanceName
            __annotations__ = {
                "region_name": region_name,
                "instance_type_name": instance_type_name,
                "ssh_key_names": ssh_key_names,
                "file_system_names": file_system_names,
                "quantity": quantity,
                "name": name,
            }
    
    instance_type_name: MetaOapg.properties.instance_type_name
    region_name: MetaOapg.properties.region_name
    ssh_key_names: MetaOapg.properties.ssh_key_names
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region_name"]) -> MetaOapg.properties.region_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instance_type_name"]) -> MetaOapg.properties.instance_type_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssh_key_names"]) -> MetaOapg.properties.ssh_key_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_system_names"]) -> MetaOapg.properties.file_system_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'InstanceName': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["region_name", "instance_type_name", "ssh_key_names", "file_system_names", "quantity", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region_name"]) -> MetaOapg.properties.region_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instance_type_name"]) -> MetaOapg.properties.instance_type_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssh_key_names"]) -> MetaOapg.properties.ssh_key_names: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_system_names"]) -> typing.Union[MetaOapg.properties.file_system_names, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['InstanceName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["region_name", "instance_type_name", "ssh_key_names", "file_system_names", "quantity", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        instance_type_name: typing.Union[MetaOapg.properties.instance_type_name, str, ],
        region_name: typing.Union[MetaOapg.properties.region_name, str, ],
        ssh_key_names: typing.Union[MetaOapg.properties.ssh_key_names, list, tuple, ],
        file_system_names: typing.Union[MetaOapg.properties.file_system_names, list, tuple, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union['InstanceName', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstanceCreateInstancesRequest':
        return super().__new__(
            cls,
            *args,
            instance_type_name=instance_type_name,
            region_name=region_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from lambda_python_sdk.model.instance_name import InstanceName
from lambda_python_sdk.model.ssh_key_name import SshKeyName
