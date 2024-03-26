# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lambda_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lambda_python_sdk.api_response import AsyncGeneratorResponse
from lambda_python_sdk import api_client, exceptions
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

from lambda_python_sdk.model.instance_create_instances_request import InstanceCreateInstancesRequest as InstanceCreateInstancesRequestSchema
from lambda_python_sdk.model.instance_name import InstanceName as InstanceNameSchema
from lambda_python_sdk.model.instance_create_instances_response import InstanceCreateInstancesResponse as InstanceCreateInstancesResponseSchema
from lambda_python_sdk.model.error_response_body import ErrorResponseBody as ErrorResponseBodySchema

from lambda_python_sdk.type.instance_create_instances_request import InstanceCreateInstancesRequest
from lambda_python_sdk.type.error_response_body import ErrorResponseBody
from lambda_python_sdk.type.instance_name import InstanceName
from lambda_python_sdk.type.instance_create_instances_response import InstanceCreateInstancesResponse

from ...api_client import Dictionary
from lambda_python_sdk.pydantic.instance_create_instances_request import InstanceCreateInstancesRequest as InstanceCreateInstancesRequestPydantic
from lambda_python_sdk.pydantic.error_response_body import ErrorResponseBody as ErrorResponseBodyPydantic
from lambda_python_sdk.pydantic.instance_create_instances_response import InstanceCreateInstancesResponse as InstanceCreateInstancesResponsePydantic
from lambda_python_sdk.pydantic.instance_name import InstanceName as InstanceNamePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = InstanceCreateInstancesRequestSchema


request_body_instance_create_instances_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'basicAuth',
    'bearerAuth',
]
SchemaFor200ResponseBodyApplicationJson = InstanceCreateInstancesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: InstanceCreateInstancesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: InstanceCreateInstancesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponseBodySchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrorResponseBody


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrorResponseBody


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_instances_mapped_args(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if region_name is not None:
            _body["region_name"] = region_name
        if instance_type_name is not None:
            _body["instance_type_name"] = instance_type_name
        if ssh_key_names is not None:
            _body["ssh_key_names"] = ssh_key_names
        if file_system_names is not None:
            _body["file_system_names"] = file_system_names
        if quantity is not None:
            _body["quantity"] = quantity
        if name is not None:
            _body["name"] = name
        args.body = _body
        return args

    async def _acreate_instances_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Launch instances
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/instance-operations/launch',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_instance_create_instances_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_instances_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Launch instances
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/instance-operations/launch',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_instance_create_instances_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateInstancesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_instances(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_instances_mapped_args(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
        )
        return await self._acreate_instances_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_instances(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_instances_mapped_args(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
        )
        return self._create_instances_oapg(
            body=args.body,
        )

class CreateInstances(BaseApi):

    async def acreate_instances(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
        validate: bool = False,
        **kwargs,
    ) -> InstanceCreateInstancesResponsePydantic:
        raw_response = await self.raw.acreate_instances(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
            **kwargs,
        )
        if validate:
            return InstanceCreateInstancesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InstanceCreateInstancesResponsePydantic, raw_response.body)
    
    
    def create_instances(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
        validate: bool = False,
    ) -> InstanceCreateInstancesResponsePydantic:
        raw_response = self.raw.create_instances(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
        )
        if validate:
            return InstanceCreateInstancesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(InstanceCreateInstancesResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_instances_mapped_args(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
        )
        return await self._acreate_instances_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        region_name: str,
        instance_type_name: str,
        ssh_key_names: typing.List[SshKeyName],
        file_system_names: typing.Optional[typing.List[str]] = None,
        quantity: typing.Optional[int] = None,
        name: typing.Optional[InstanceName] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_instances_mapped_args(
            region_name=region_name,
            instance_type_name=instance_type_name,
            ssh_key_names=ssh_key_names,
            file_system_names=file_system_names,
            quantity=quantity,
            name=name,
        )
        return self._create_instances_oapg(
            body=args.body,
        )

