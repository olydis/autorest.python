﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import unittest
import subprocess
import sys
import isodate
import os
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "RequiredOptional"))

from msrest.exceptions import DeserializationError, SerializationError, ValidationError

from requiredoptional import AutoRestRequiredOptionalTestService
from requiredoptional.models import StringWrapper, ArrayWrapper, ClassWrapper

import pytest

@pytest.fixture
def client():
    return AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            base_url="http://localhost:3000")

class TestRequiredOptional(object):

    def test_required_optional(self, client):

        client.config.required_global_path = "required_path"
        client.config.required_global_query = "required_query"

        client.implicit.put_optional_query(None)
        client.implicit.put_optional_body(None)
        client.implicit.put_optional_header(None)

        client.implicit.get_optional_global_query(None)

        client.explicit.post_optional_integer_parameter(None)
        client.explicit.post_optional_integer_property(None)
        client.explicit.post_optional_integer_header(None)

        client.explicit.post_optional_string_parameter(None)
        client.explicit.post_optional_string_property(None)
        client.explicit.post_optional_string_header(None)

        client.explicit.post_optional_class_parameter(None)
        client.explicit.post_optional_class_property(None)

        client.explicit.post_optional_array_parameter(None)
        client.explicit.post_optional_array_property(None)
        client.explicit.post_optional_array_header(None)

    def test_required_optional_negative(self, client):

        client.config.required_global_path = None
        client.config.required_global_query = None

        with pytest.raises(ValidationError):
            client.implicit.get_required_path(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_string_header(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_string_parameter(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_string_property(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_array_header(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_array_parameter(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_array_property(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_class_parameter(None)

        with pytest.raises(ValidationError):
            client.explicit.post_required_class_property(None)

        with pytest.raises(ValidationError):
            client.implicit.get_required_global_path()

        with pytest.raises(ValidationError):
            client.implicit.get_required_global_query()


if __name__ == '__main__':


    unittest.main()
