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


from cengal.introspection.inspect import *
from inspect import *


def main():
    # example code for resolving the builtin descriptor types
    class _foo:
        __slots__ = ['foo', 'bar']

        def __init__(self):
            self.bar = 2

    slot_descriptor = type(_foo.foo)
    print(f'{slot_descriptor = }')
    print(is_descriptor(_foo.foo))

    getset_descriptor = type(type(open(__file__)).name)
    print(f'{getset_descriptor = }')
    print(is_descriptor(type(open(__file__)).name))
    
    wrapper_descriptor = type(str.__dict__['__add__'])
    print(f'{wrapper_descriptor = }')
    print(is_descriptor(str.__dict__['__add__']))
    
    descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

    some_object = _foo()
    result = getattr_static(some_object, 'foo')
    result_type = type(result)
    if result_type in descriptor_types:
        print(f'{result_type = }')
        try:
            result = result.__get__(some_object)
            print(f'{result = }')
        except AttributeError:
            # descriptors can raise AttributeError to
            # indicate there is no underlying value
            # in which case the descriptor itself will
            # have to do
            print('descriptors can raise AttributeError to')
            pass

    result = getattr_static(some_object, 'bar')
    result_type = type(result)
    if result_type in descriptor_types:
        print(f'{result_type = }')
        try:
            result = result.__get__(some_object)
            print(f'{result = }')
        except AttributeError:
            # descriptors can raise AttributeError to
            # indicate there is no underlying value
            # in which case the descriptor itself will
            # have to do
            print('descriptors can raise AttributeError to')
            pass

if '__main__' == __name__:
    main()
