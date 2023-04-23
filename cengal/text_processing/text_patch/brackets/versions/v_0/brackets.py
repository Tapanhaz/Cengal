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
__version__ = "3.1.11"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.text_processing.brackets_processing import find_text_in_brackets, BracketPair
from cengal.text_processing.text_processing import Text, replace_text, replace_slice, DEFAULT_ENCODING
from typing import List, Tuple, Optional, Callable


def patch_text(text: Text, patch: List[Tuple[BracketPair, Text]], encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    for brackets_pair, after in patch:
        old_text_slice = find_text_in_brackets(data, brackets_pair, encoding=encoding, normalizer=normalizer)
        if old_text_slice is None:
            continue

        data, _ = replace_slice(data, old_text_slice, after, encoding=encoding, normalizer=normalizer)

    return text
