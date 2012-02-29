#!/usr/bin/env python
#
# pyepg/main.py - Main processing function
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

# System
import os, sys, datetime

# PyEPG
import pyepg.log             as log
import pyepg.conf            as conf
import pyepg.cache           as cache
import pyepg.grabber.atlas   as grabber
from pyepg.model import EPG

# ###########################################################################
# Run
# ###########################################################################

def main ( conf_root = None , conf_over = {} ):

  # Defaults
  if conf_root is None:
    conf_root = os.path.expanduser('~/.pyepg')
  conf_path  = os.path.join(conf_root, 'config')
  cache_path = os.path.join(conf_root, 'cache')

  # Load configuration
  conf.init(conf_path, conf_over)

  # Initialise log
  log.init()

  # Initialise the cache
  cache.init(cache_path) 

  # Initialise EPG
  epg = EPG()

  # Get config
  channels = conf.get('channels', [])
  days     = conf.get('days', 7)
  today    = datetime.datetime.today()

  # Get grabber/formatter
  def _import ( fmt, n ):
    return __import__(fmt % n, globals(), locals(), [n])
  grabber   = _import('pyepg.grabber.%s',   conf.get('grabber', 'atlas'))
  formatter = _import('pyepg.formatter.%s', conf.get('formatter', 'epg'))

  # Get EPG
  grabber.grab(epg, channels, today, today + datetime.timedelta(days=days))

  # Output
  formatter.format(epg, sys.stdout)

  # Stats
  log.info('Channel  Count: %d' % len(epg.get_channels()))
  log.info('Brand    Count: %d' % len(epg.get_brands()))
  log.info('Series   Count: %d' % len(epg.get_series()))
  log.info('Episode  Count: %d' % len(epg.get_episodes()))
  log.info('Schedule Count: %d' % epg.get_sched_count())

# ###########################################################################
# Editor
# ###########################################################################