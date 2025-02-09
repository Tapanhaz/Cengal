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


from cengal.file_system.file_manager import current_src_file_dir, path_relative_to_current_src
from cengal.file_system.directory_manager import filtered_file_list_traversal, FilteringType
from cengal.file_system.path_manager import path_relative_to_src, RelativePath
from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.text_processing.text_processing import find_text, replace_slice
from cengal.text_processing.brackets_processing import BracketPair, Bracket, replace_text_with_brackets, find_text_with_brackets
from os.path import splitext, join


head_string = \
'''#!/usr/bin/env python
# coding=utf-8'''


license_string = \
'''# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
# limitations under the License.'''
license_bracket_pair: BracketPair = BracketPair([Bracket('# Copyright ©')], [Bracket('# limitations under the License.')])


module_docstring_string = \
'''"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""'''


credits_string = \
'''__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"'''
credits_bracket_pair: BracketPair = BracketPair([Bracket('__author__ =')], [Bracket('__status__ = "Production"')])


def main():
    cengal_root_dir: str = path_relative_to_current_src('../..')
    travers_result = filtered_file_list_traversal(cengal_root_dir, FilteringType.including, {'.pyx', '.py'}, remove_empty_items=True, use_spinner=False)
    files_processed: int = 0
    try:
        for dir_path, dirs, files in travers_result:
            for file in files:
                file_path = join(dir_path, file)
                print()
                print(f'... Processing: {file_path}')
                try:
                    with open(file_path, 'r+b') as file:
                        text, text_encoding, bom_bytes = detect_and_decode(file.read())
                        if not bom_bytes:
                            text_encoding = 'utf-8'
                        
                        head_string_pos = find_text(text, head_string, 0, len(head_string) * 2)
                        license_string_pos = find_text_with_brackets(text, license_bracket_pair)
                        module_docstring_string_pos = find_text(text, module_docstring_string)
                        credits_string_pos = find_text_with_brackets(text, credits_bracket_pair)
                        
                        replace_only: bool = bool(head_string_pos is not None) and bool(license_string_pos is not None) and bool(credits_string_pos is not None)
                        if replace_only:
                            text, _ = replace_text_with_brackets(text, license_bracket_pair, license_string, 1)
                            text, _ = replace_text_with_brackets(text, credits_bracket_pair, credits_string, 1)
                        else:
                            head_string_pos = find_text(text, head_string, 0, len(head_string) * 2)
                            if head_string_pos is not None:
                                text, _ = replace_slice(text, head_string_pos, str())
                            
                            license_string_pos = find_text_with_brackets(text, license_bracket_pair)
                            if license_string_pos is not None:
                                text, _ = replace_slice(text, license_string_pos, str())
                            
                            module_docstring_string_pos = find_text(text, module_docstring_string)
                            if module_docstring_string_pos is not None:
                                text, _ = replace_slice(text, module_docstring_string_pos, str())
                            
                            credits_string_pos = find_text_with_brackets(text, credits_bracket_pair)
                            if credits_string_pos is not None:
                                text, _ = replace_slice(text, credits_string_pos, str())

                            new_head: str = head_string + '\n\n' + license_string + '\n\n\n' + module_docstring_string + '\n\n\n' + credits_string + '\n\n\n'
                            text = new_head + text
                        
                        file.seek(0, 0)
                        file.truncate(0)
                        data = bom_bytes + text.encode(text_encoding)
                        file.write(data)
                        files_processed += 1
                finally:
                    print(f'Done: {file_path}')
    finally:
        print()
        print(f'Files procesed: {files_processed}')


if '__main__' == __name__:
    main()
