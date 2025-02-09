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


__all__ = ['KillSingleCoroParams', 'KillCoroList', 'kill_coro_list_on', 'try_kill_coro_list_on', 'akill_coro_list_on', 'atry_kill_coro_list_on', 'kill_coro_list', 'try_kill_coro_list', 'akill_coro_list', 'atry_kill_coro_list']


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.introspection.inspect import get_exception, get_exception_tripple
from typing import Sequence, Tuple, List, Optional, Any, cast, Dict, Union, Set


class KillSingleCoroParams:
    def __init__(self, coro_id: CoroID, tree: bool = False) -> None:
        self.coro_id: CoroID = coro_id
        self.tree: bool = tree
    
    def __call__(self, new_coro_id: Optional[CoroID] = None) -> Tuple:
        return self.coro_id if new_coro_id is None else new_coro_id
    
    def __bool__(self):
        return self.tree


class KillCoroList(TypedService[List[Tuple[Optional[bool], Optional[Exception]]]], ServiceWithADirectRequestMixin):
    def __init__(self, loop: CoroScheduler):
        super(KillCoroList, self).__init__(loop)
        self.direct_requests: List[Tuple] = list()

    def single_task_registration_or_immediate_processing(
            self, coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]
    ) -> Tuple[bool, Sequence[Tuple[bool, Optional[Exception]]], Any]:
        results = list()
        try:
            put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
            for request in coro_list:
                exception = None
                result = None
                try:
                    if isinstance(request, KillSingleCoroParams):
                        coro_id = request.coro_id
                        if request:
                            children: Set[CoroID] = put_coro.get_set_of_all_children(coro_id)
                        
                        result = self._loop.kill_coro_by_id(coro_id)
                        if request:
                            for child in children:
                                self._loop.kill_coro_by_id(child)
                    else:
                        coro_id = request
                        result = self._loop.kill_coro_by_id(coro_id)
                except:
                    exception = get_exception()
                
                results.append((result, exception))
        except:
            return True, results, get_exception()

        return True, results, None

    def full_processing_iteration(self):
        put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
        direct_requests_buff = self.direct_requests
        self.direct_requests = type(direct_requests_buff)()
        for coro_list in direct_requests_buff:
            for request in coro_list:
                exception = None
                try:
                    if isinstance(request, KillSingleCoroParams):
                        coro_id = request.coro_id
                        if request:
                            children: Set[CoroID] = put_coro.get_set_of_all_children(coro_id)
                        
                        self._loop.kill_coro_by_id(coro_id)
                        if request:
                            for child in children:
                                self._loop.kill_coro_by_id(child)
                    else:
                        coro_id = request
                        self._loop.kill_coro_by_id(coro_id)
                except:
                    ex_type, exception, tracback = get_exception_tripple()
                    if __debug__: dlog(ex_type, exception, tracback)
                    raise

        self.make_dead()
    
    def _add_direct_request(self, coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[None]:
        self.direct_requests.append(coro_list)
        self.make_live()
        return ValueExistence()

    def in_work(self) -> bool:
        result: bool = bool(self.direct_requests)
        return self.thrifty_in_work(result)


def kill_coro_list_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Sequence[Tuple[bool, Optional[Exception]]]]:
    return make_request_to_service_with_context(context, KillCoroList, coro_list)


def try_kill_coro_list_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Optional[Sequence[Tuple[bool, Optional[Exception]]]]]:
    return try_make_request_to_service_with_context(context, KillCoroList, coro_list)


async def akill_coro_list_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Sequence[Tuple[bool, Optional[Exception]]]]:
    return await amake_request_to_service_with_context(context, KillCoroList, coro_list)


async def atry_kill_coro_list_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Optional[Sequence[Tuple[bool, Optional[Exception]]]]]:
    return await atry_make_request_to_service_with_context(context, KillCoroList, coro_list)


def kill_coro_list(coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Sequence[Tuple[bool, Optional[Exception]]]]:
    return make_request_to_service(KillCoroList, coro_list)


def try_kill_coro_list(coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Optional[Sequence[Tuple[bool, Optional[Exception]]]]]:
    return try_make_request_to_service(KillCoroList, coro_list)


async def akill_coro_list(coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Sequence[Tuple[bool, Optional[Exception]]]]:
    return await amake_request_to_service(KillCoroList, coro_list)


async def atry_kill_coro_list(coro_list: Sequence[Union[CoroID, KillSingleCoroParams]]) -> ValueExistence[Optional[Sequence[Tuple[bool, Optional[Exception]]]]]:
    return await atry_make_request_to_service(KillCoroList, coro_list)
