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


class Instance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Virtual machine (VM) in Lambda Cloud
    """


    class MetaOapg:
        required = {
            "file_system_names",
            "id",
            "ssh_key_names",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def BOOTING(cls):
                    return cls("booting")
                
                @schemas.classproperty
                def UNHEALTHY(cls):
                    return cls("unhealthy")
                
                @schemas.classproperty
                def TERMINATING(cls):
                    return cls("terminating")
                
                @schemas.classproperty
                def TERMINATED(cls):
                    return cls("terminated")
            
            
            class ssh_key_names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
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
        
            @staticmethod
            def name() -> typing.Type['InstanceName']:
                return InstanceName
            
            
            class ip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ip':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def region() -> typing.Type['Region']:
                return Region
        
            @staticmethod
            def instance_type() -> typing.Type['InstanceType']:
                return InstanceType
            
            
            class hostname(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hostname':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class jupyter_token(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jupyter_token':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class jupyter_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'jupyter_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "status": status,
                "ssh_key_names": ssh_key_names,
                "file_system_names": file_system_names,
                "name": name,
                "ip": ip,
                "region": region,
                "instance_type": instance_type,
                "hostname": hostname,
                "jupyter_token": jupyter_token,
                "jupyter_url": jupyter_url,
            }
    
    file_system_names: MetaOapg.properties.file_system_names
    id: MetaOapg.properties.id
    ssh_key_names: MetaOapg.properties.ssh_key_names
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssh_key_names"]) -> MetaOapg.properties.ssh_key_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_system_names"]) -> MetaOapg.properties.file_system_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> 'InstanceName': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> 'Region': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instance_type"]) -> 'InstanceType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jupyter_token"]) -> MetaOapg.properties.jupyter_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jupyter_url"]) -> MetaOapg.properties.jupyter_url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "ssh_key_names", "file_system_names", "name", "ip", "region", "instance_type", "hostname", "jupyter_token", "jupyter_url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssh_key_names"]) -> MetaOapg.properties.ssh_key_names: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_system_names"]) -> MetaOapg.properties.file_system_names: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union['InstanceName', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union['Region', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instance_type"]) -> typing.Union['InstanceType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jupyter_token"]) -> typing.Union[MetaOapg.properties.jupyter_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jupyter_url"]) -> typing.Union[MetaOapg.properties.jupyter_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "ssh_key_names", "file_system_names", "name", "ip", "region", "instance_type", "hostname", "jupyter_token", "jupyter_url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_system_names: typing.Union[MetaOapg.properties.file_system_names, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        ssh_key_names: typing.Union[MetaOapg.properties.ssh_key_names, list, tuple, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        name: typing.Union['InstanceName', schemas.Unset] = schemas.unset,
        ip: typing.Union[MetaOapg.properties.ip, None, str, schemas.Unset] = schemas.unset,
        region: typing.Union['Region', schemas.Unset] = schemas.unset,
        instance_type: typing.Union['InstanceType', schemas.Unset] = schemas.unset,
        hostname: typing.Union[MetaOapg.properties.hostname, None, str, schemas.Unset] = schemas.unset,
        jupyter_token: typing.Union[MetaOapg.properties.jupyter_token, None, str, schemas.Unset] = schemas.unset,
        jupyter_url: typing.Union[MetaOapg.properties.jupyter_url, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Instance':
        return super().__new__(
            cls,
            *args,
            file_system_names=file_system_names,
            id=id,
            ssh_key_names=ssh_key_names,
            status=status,
            name=name,
            ip=ip,
            region=region,
            instance_type=instance_type,
            hostname=hostname,
            jupyter_token=jupyter_token,
            jupyter_url=jupyter_url,
            _configuration=_configuration,
            **kwargs,
        )

from lambda_python_sdk.model.instance_name import InstanceName
from lambda_python_sdk.model.instance_type import InstanceType
from lambda_python_sdk.model.region import Region
from lambda_python_sdk.model.ssh_key_name import SshKeyName
