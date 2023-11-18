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


from pprint import pprint
from typing import Dict, List


def get_dict_item(keys, data: Dict):
    rv = data
    for key in keys:
        rv = rv[key]
    
    return rv


def get_dict_item_default(keys, data: Dict, default=None):
    rv = data
    for key in keys:
        try:
            rv = rv[key]
        except KeyError:
            return default
    
    return rv


def set_dict_item(keys, data: Dict, value):
    rv = data
    path_len = len(keys)
    for index, key in enumerate(keys):
        if index == path_len - 1:
            rv[key] = value
            break

        rv = rv[key]
        

def del_dict_item(keys, data: Dict):
    rv = data
    path_len = len(keys)
    for index, key in enumerate(keys):
        rv = rv[key]
        if index == path_len - 2:
            del rv[keys[-1]]
            break
    
    return rv
        

def try_del_dict_item(keys, data: Dict):
    try:
        del_dict_item(keys, data)
    except KeyError:
        pass


def srt_to_dict_path(str_path) -> List[str]:
    return eval(str_path)


j = {"app": {
    "Garden": {
        "Flowers": {
            "Red flower": "Rose",
            "White Flower": "Jasmine",
            "Yellow Flower": "Marigold"
        }
    },
    "Fruits": {
        "Yellow fruit": "Mango",
        "Green fruit": "Guava",
        "White Flower": "groovy"
    },
    "Trees": {
        "label": {
            "Yellow fruit": "Pumpkin",
            "White Flower": "Bogan"
        }
    }
}}
path_str = "['app', 'Garden', 'Flowers', 'White Flower']"

del_dict_item(srt_to_dict_path(path_str), j)
pprint(j)
try:
    print(get_dict_item(['app', 'Garden', 'Flowers', 'White Flower'], j))
except KeyError:
    print("Key not found")

print(get_dict_item_default(['app', 'Garden', 'Flowers', 'White Flower'], j))
set_dict_item(['app', 'Garden', 'Flowers', 'White Flower'], j, 'Jasmine')
pprint(j)
del_dict_item(srt_to_dict_path(path_str), j)
del_dict_item(srt_to_dict_path(path_str), j)
