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

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'searchcommands_app', 'lib'))
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib.six.moves import range

### Event gen transition commands
cmd_kill_1 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/mix.yml\""
cmd_kill_2 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/mix_bad.yml\""
cmd_1 = "nohup /home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/mix_bad.yml &"
cmd_2 = "nohup /home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/mix.yml &"

@Configuration()
class EventStatusCommand(GeneratingCommand):
    action = Option(require=True, validate=validators.Integer(0))

    def generate(self):
        self.logger.debug("Changing status of Bad Events:", self.action)
        action = self.action
        if action==1:
            subprocess.run(cmd_kill_1, shell=True)
            subprocess.run(cmd_kill_2, shell=True)
            subprocess.run(cmd_1, shell=True)
            out = "Bad Events Turned On"
        elif action==0:
            subprocess.run(cmd_kill_2, shell=True)
            subprocess.run(cmd_kill_1, shell=True)
            subprocess.run(cmd_2, shell=True)
            out = "Bad Events Turned Off"

        yield {'_time': time.time(), '_raw': out}

dispatch(EventStatusCommand, sys.argv, sys.stdin, sys.stdout, __name__)