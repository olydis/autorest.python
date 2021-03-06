# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.string_operations import StringOperations
from .operations.enum_operations import EnumOperations
from . import models


class AutoRestSwaggerBATServiceConfiguration(Configuration):
    """Configuration for AutoRestSwaggerBATService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestSwaggerBATServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestswaggerbatservice/{}'.format(VERSION))


class AutoRestSwaggerBATService(object):
    """Test Infrastructure for AutoRest Swagger BAT

    :ivar config: Configuration for client.
    :vartype config: AutoRestSwaggerBATServiceConfiguration

    :ivar string: String operations
    :vartype string: bodystring.operations.StringOperations
    :ivar enum: Enum operations
    :vartype enum: bodystring.operations.EnumOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestSwaggerBATServiceConfiguration(base_url)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.string = StringOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.enum = EnumOperations(
            self._client, self.config, self._serialize, self._deserialize)
