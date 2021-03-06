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

from msrest.serialization import Model


class CustomParameterGroup(Model):
    """Additional parameters for
    get_multiple_pages_fragment_with_grouping_next_link operation.

    All required parameters must be populated in order to send to Azure.

    :param api_version: Required. Sets the api version to use.
    :type api_version: str
    :param tenant: Required. Sets the tenant to use.
    :type tenant: str
    """

    _validation = {
        'api_version': {'required': True},
        'tenant': {'required': True},
    }

    _attribute_map = {
        'api_version': {'key': '', 'type': 'str'},
        'tenant': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, api_version: str, tenant: str, **kwargs) -> None:
        super(CustomParameterGroup, self).__init__(**kwargs)
        self.api_version = api_version
        self.tenant = tenant
