#!/usr/bin/env python
#
# pyepg/formatter/xmltv.py - Configuration
#
# Copyright (C) 2012 Adam Sutton <dev@adamsutton.me.uk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
"""

# ###########################################################################
# Imports
# ###########################################################################

import pyepg.formatter.exmltv as exmltv

# ###########################################################################
# Formatter API
# ###########################################################################

def format ( epg, out ):
  exmltv.format(epg, out, False)

# ###########################################################################
# Editor
# ###########################################################################
