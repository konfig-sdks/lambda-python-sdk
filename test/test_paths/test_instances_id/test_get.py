# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud

    The version of the OpenAPI document: 1.5.1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import lambda_python_sdk
from lambda_python_sdk.paths.instances_id import get
from lambda_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInstancesId(ApiTestMixin, unittest.TestCase):
    """
    InstancesId unit test stubs
        List details of a specific instance
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()