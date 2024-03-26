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


class InstanceTypeGetListResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Dict of instance_type_name to instance_type and region availability.
    """


    class MetaOapg:
        
        
        class additional_properties(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "regions_with_capacity_available",
                    "instance_type",
                }
                
                class properties:
                
                    @staticmethod
                    def instance_type() -> typing.Type['InstanceType']:
                        return InstanceType
                    
                    
                    class regions_with_capacity_available(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Region']:
                                return Region
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Region'], typing.List['Region']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'regions_with_capacity_available':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Region':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "instance_type": instance_type,
                        "regions_with_capacity_available": regions_with_capacity_available,
                    }
            
            regions_with_capacity_available: MetaOapg.properties.regions_with_capacity_available
            instance_type: 'InstanceType'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["instance_type"]) -> 'InstanceType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["regions_with_capacity_available"]) -> MetaOapg.properties.regions_with_capacity_available: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["instance_type", "regions_with_capacity_available", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["instance_type"]) -> 'InstanceType': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["regions_with_capacity_available"]) -> MetaOapg.properties.regions_with_capacity_available: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["instance_type", "regions_with_capacity_available", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                regions_with_capacity_available: typing.Union[MetaOapg.properties.regions_with_capacity_available, list, tuple, ],
                instance_type: 'InstanceType',
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'additional_properties':
                return super().__new__(
                    cls,
                    *args,
                    regions_with_capacity_available=regions_with_capacity_available,
                    instance_type=instance_type,
                    _configuration=_configuration,
                    **kwargs,
                )
    
    def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
    ) -> 'InstanceTypeGetListResponseData':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lambda_python_sdk.model.instance_type import InstanceType
from lambda_python_sdk.model.region import Region