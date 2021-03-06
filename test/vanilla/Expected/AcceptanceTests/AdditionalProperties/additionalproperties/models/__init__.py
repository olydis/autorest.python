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

try:
    from .error_py3 import Error, ErrorException
    from .pet_ap_true_py3 import PetAPTrue
    from .pet_ap_object_py3 import PetAPObject
    from .pet_ap_string_py3 import PetAPString
    from .pet_ap_in_properties_py3 import PetAPInProperties
    from .pet_ap_in_properties_with_ap_string_py3 import PetAPInPropertiesWithAPString
except (SyntaxError, ImportError):
    from .error import Error, ErrorException
    from .pet_ap_true import PetAPTrue
    from .pet_ap_object import PetAPObject
    from .pet_ap_string import PetAPString
    from .pet_ap_in_properties import PetAPInProperties
    from .pet_ap_in_properties_with_ap_string import PetAPInPropertiesWithAPString

__all__ = [
    'Error', 'ErrorException',
    'PetAPTrue',
    'PetAPObject',
    'PetAPString',
    'PetAPInProperties',
    'PetAPInPropertiesWithAPString',
]
