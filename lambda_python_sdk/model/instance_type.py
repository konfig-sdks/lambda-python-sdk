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


class InstanceType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Hardware configuration and pricing of an instance type
    """


    class MetaOapg:
        required = {
            "specs",
            "name",
            "description",
            "price_cents_per_hour",
        }
        
        class properties:
            description = schemas.StrSchema
            name = schemas.StrSchema
            price_cents_per_hour = schemas.IntSchema
        
            @staticmethod
            def specs() -> typing.Type['InstanceTypeSpecs']:
                return InstanceTypeSpecs
            __annotations__ = {
                "description": description,
                "name": name,
                "price_cents_per_hour": price_cents_per_hour,
                "specs": specs,
            }
    
    specs: 'InstanceTypeSpecs'
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    price_cents_per_hour: MetaOapg.properties.price_cents_per_hour
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price_cents_per_hour"]) -> MetaOapg.properties.price_cents_per_hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["specs"]) -> 'InstanceTypeSpecs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "price_cents_per_hour", "specs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price_cents_per_hour"]) -> MetaOapg.properties.price_cents_per_hour: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["specs"]) -> 'InstanceTypeSpecs': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "price_cents_per_hour", "specs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        specs: 'InstanceTypeSpecs',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        price_cents_per_hour: typing.Union[MetaOapg.properties.price_cents_per_hour, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InstanceType':
        return super().__new__(
            cls,
            *args,
            specs=specs,
            name=name,
            description=description,
            price_cents_per_hour=price_cents_per_hour,
            _configuration=_configuration,
            **kwargs,
        )

from lambda_python_sdk.model.instance_type_specs import InstanceTypeSpecs