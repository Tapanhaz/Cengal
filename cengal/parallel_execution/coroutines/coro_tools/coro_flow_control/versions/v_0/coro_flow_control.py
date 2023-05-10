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


__all__ = ['GracefulCoroDestroy', 'graceful_coro_destroyer', 'agraceful_coro_destroyer']


from typing import Optional, Type, Any, Hashable
from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, CoroID, ExplicitWorker, Worker, CoroWrapperBase, get_interface_for_an_explicit_loop
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro_to, put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import ThrowCoro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoro, WaitCoroRequest, CoroutineNotFoundError
from cengal.code_flow_control.smart_values import ValueExistence


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.17"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class GracefulCoroDestroy(Exception):
    pass


def graceful_coro_destroyer(
        i: Interface, 
        phase_time_limit: Optional[float], 
        coro_id: CoroID, 
        ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, 
        tree: bool = True, 
        first_phase_is_wait: bool = True, 
        last_phase_is_kill: bool = True, 
    ):
    phase_time_limit = phase_time_limit or 0
    try:
        if first_phase_is_wait:
            try:
                i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=False, tree=tree, result_required=False).single(coro_id))
            except TimeoutError:
                pass

        if (ex_type is not None) or (ex_value is not None):
            if not i(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree):
                raise CoroutineNotFoundError
            
            try:
                i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=False, tree=tree, result_required=False).single(coro_id))
            except TimeoutError:
                pass

        if not i(ThrowCoro, coro_id, GracefulCoroDestroy, tree=tree):
            raise CoroutineNotFoundError
        
        try:
            i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=last_phase_is_kill, tree=tree, result_required=False).single(coro_id))
        except TimeoutError:
            pass
        
    except CoroutineNotFoundError:
        pass
    finally:
        i(Yield)


async def agraceful_coro_destroyer(
        i: Interface, 
        phase_time_limit: Optional[float], 
        coro_id: CoroID, 
        ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, 
        tree: bool = True, 
        first_phase_is_wait: bool = True,
        last_phase_is_kill: bool = True, 
    ):
    phase_time_limit = phase_time_limit or 0
    try:
        if first_phase_is_wait:
            try:
                await i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=False, tree=tree, result_required=False).single(coro_id))
            except TimeoutError:
                pass

        if (ex_type is not None) or (ex_value is not None):
            if not await i(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree):
                raise CoroutineNotFoundError
            
            try:
                await i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=False, tree=tree, result_required=False).single(coro_id))
            except TimeoutError:
                pass

        if not await i(ThrowCoro, coro_id, GracefulCoroDestroy, tree=tree):
            raise CoroutineNotFoundError
        
        try:
            await i(WaitCoro, WaitCoroRequest(phase_time_limit, kill_on_timeout=last_phase_is_kill, tree=tree, result_required=False).single(coro_id))
        except TimeoutError:
            pass
        
    except CoroutineNotFoundError:
        pass
    finally:
        await i(Yield)
