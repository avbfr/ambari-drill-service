#!/usr/bin/env python

import os
from resource_management import *
from resource_management.libraries.script.script import Script

config = Script.get_config()

drill_run_dir = config['configurations']['drill-env']['drill_run_dir']
