#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

from cengal.performance_test_lib.performance_test_lib import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


@test_function_run_time
def test_function(joiner=None):
    copy.copy(joiner)


class TestClass:
    def __init__(self, int_value):
        self.int_value = int_value

    @test_function_run_time
    def func(self, second_value):
        self.int_value += second_value


def example_for__with_statement():
    joiner = b''
    with test_run_time('Joiner', 100000) as index:
        while index.result > 0:
            joiner.join(list())

            index.result -= 1


def example_for__standalone_function():
    test_function('', performance_test_lib__test_name='Standalone', performance_test_lib__iterations_qnt=100000)


def example_for__class_method():
    tc = TestClass(10)
    tc.func(1, performance_test_lib__iterations_qnt=1000000)
    print(tc.int_value)  # 1000010


if __name__ == "__main__":
    example_for__with_statement()
    example_for__standalone_function()
    example_for__class_method()
