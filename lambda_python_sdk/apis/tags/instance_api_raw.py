# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
    Generated by: https://konfigthis.com
"""

from lambda_python_sdk.paths.instance_operations_launch.post import CreateInstancesRaw
from lambda_python_sdk.paths.instances_id.get import GetDetailsRaw
from lambda_python_sdk.paths.instances.get import ListRunningInstancesRaw
from lambda_python_sdk.paths.instance_operations_restart.post import RestartInstancesRaw
from lambda_python_sdk.paths.instance_operations_terminate.post import TerminateInstanceRaw


class InstanceApiRaw(
    CreateInstancesRaw,
    GetDetailsRaw,
    ListRunningInstancesRaw,
    RestartInstancesRaw,
    TerminateInstanceRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass