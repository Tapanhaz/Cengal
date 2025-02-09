#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"

from cengal.data_manipulation.tree_traversal import *

from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.help_tools import json_to_printable_string, make_readable_json
import json
from cengal.data_manipulation.serialization import test_data_factory, TestDataType
from cengal.data_manipulation.objects_counter import objects_counter, objects_counter_recursive, object_counter_uni
from cengal.introspection.inspect import intro_func_repr
from pprint import pprint


def on_node(node, child, index):
    print(f'\nNODE: <<< {intro_func_repr(True)} >>>')


def on_child(node, child, index):
    print(f'\nCHILD: <<< {intro_func_repr(True)} >>>')


def test_objects_counter():
    print(f'\n<<< {intro_func_repr()} >>>')
    data = {
            1: 'Hello',
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'dd': {
                        43: [0],
                        15: {
                            'world': 42
                        }
                    }
                }
            ],
            'To all!': '!!1'
        }
    print(make_readable_json(json.dumps(data)))

    tt: TreeTraversal = TreeTraversal(data, on_node, on_child)
    tt(TreeTraversalType.recursive)
    # tt(TreeTraversalType.stack_based)
    # tt()


def main():
    test_objects_counter()


if '__main__' == __name__:
    main()
