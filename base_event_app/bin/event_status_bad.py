#!/usr/bin/env python
# coding=utf-8
#
# Copyright © 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import, division, print_function, unicode_literals
#import app
import os,sys
import time
import random
import subprocess

DEBUG = False
splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'searchcommands_app', 'lib'))
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib.six.moves import range

### Event gen transition commands
cmd_kill_1 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_good_mix.yaml\""
cmd_kill_2 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_bad_mix.yaml\""
cmd_1 = "nohup /home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_bad_mix.yaml &"
cmd_2 = "nohup /home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_good_mix.yaml &"

@Configuration()
class EventStatusCommand(GeneratingCommand):

    def generate(self):
        self.logger.debug("Changing status of Bad Events:"),
        subprocess.run(cmd_kill_1, shell=True),
        subprocess.run(cmd_kill_2, shell=True),
        subprocess.Popen(cmd_1, shell=True, stdout=open('/dev/null', 'w'),
                 stderr=open('error.log', 'a'), preexec_fn=os.setpgrp)
        out = "Bad Events Turned On!",
        time.sleep(5)
        
        yield {'_time': time.time(), '_raw': out}

dispatch(EventStatusCommand, sys.argv, sys.stdin, sys.stdout, __name__)