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

import select
from .net_io_abstract import *

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


class IOMethodSelect(IOMethodBase):
    def __init__(self, interface: NetIOBase):
        super().__init__(interface)
        self.input_check_sockets = set()
        self.output_check_sockets = set()
        self.exception_check_sockets = set()

    def loop_iteration(self, timeout=None):
        timeout = timeout or -1

        readable, writable, exceptional = select.select(self.input_check_sockets,
                                                        self.output_check_sockets,
                                                        self.exception_check_sockets,
                                                        timeout)

        for fileno in readable:
            # Read available. We can try to read even even if an error occurred
            connection = self.interface.connection_by_fileno[fileno]
            if ConnectionType.passive == connection.connection_info.connection_type:
                self.interface.on_accept_connection(connection)
            else:
                self.interface.on_read(connection)

        for fileno in exceptional:
            # Some error. Connection should be closed
            connection = self.interface.connection_by_fileno[fileno]
            self.should_be_closed.add(connection.conn)

        writable -= exceptional

        for fileno in writable:
            # Write available. We will not write data if an error occurred
            connection = self.interface.connection_by_fileno[fileno]
            if ConnectionState.waiting_for_connection == connection.connection_state:
                if not connection.conn.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR):
                    # Connected successfully:
                    self.interface.on_connected(connection)
                else:
                    # Some connection error - will be closed:
                    self.should_be_closed.add(connection.conn)
            else:
                self.interface.on_write(connection)

        self._close_all()

    def _close_all(self):
        should_be_closed = self.should_be_closed
        self.should_be_closed = set()
        for conn in should_be_closed:
            fileno = conn.fileno()
            if fileno in self.interface.connection_by_fileno:
                connection = self.interface.connection_by_fileno[fileno]
                self.interface.on_close(connection)  # self.remove_connection() should be run from inside of this
                #   callback
            else:
                self.remove_connection(conn)

    def destroy(self):
        self._close_all()

    def add_connection(self, conn: socket.socket):
        fileno = conn.fileno()
        self.exception_check_sockets.add(fileno)
        self.input_check_sockets.add(fileno)

    def remove_connection(self, conn: socket.socket):
        fileno = conn.fileno()
        if fileno in self.exception_check_sockets:
            self.exception_check_sockets.remove(fileno)
        if fileno in self.input_check_sockets:
            self.input_check_sockets.remove(fileno)
        if fileno in self.output_check_sockets:
            self.output_check_sockets.remove(fileno)

    def set__need_write(self, conn: socket.socket, state=True):
        fileno = conn.fileno()
        if fileno in self.exception_check_sockets:
            if state:
                self.output_check_sockets.add(fileno)
            else:
                if fileno in self.output_check_sockets:
                    self.output_check_sockets.remove(fileno)

    def set__should_be_closed(self, conn: socket.socket):
        self.should_be_closed.add(conn)
