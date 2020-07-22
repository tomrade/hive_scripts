#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import print_function
#from __future__ import unicode_literals

import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper
import argparse
import datetime
import json



parser = argparse.ArgumentParser()
parser.add_argument("-t","--timestamp", help="when the motion was detected '%Y-%m-%d_%H-%M-%S'", required=True)
parser.add_argument("-e","--event_id", help="motion event id", required=True)
parser.add_argument("-n","--name", help="Camera Name", required=False, default="motion eye")
parser.add_argument("-c","--config", help="Config File Containing API details", required=True)
args = parser.parse_args()

# parse date from motioneye
# %Y-%m-%d_%H-%M-%S
# 2020-07-22_13-27-39
ts_value = datetime.datetime.strptime(args.timestamp, '%Y-%m-%d_%H-%M-%S')
# this needs to be millisecond epoch for the api so see that in the date bit below :(


# Todo Config file
# Create API object
with open(args.config,'r') as config_file:
    config = json.load(config_file)

api = TheHiveApi('{}:{}'.format(config['hive_host'],config['hive_port']), config['hive_api_key'])

# Create UUID
sourceRef = str(uuid.uuid4())[0:6]
# Create Alert Object
alert = Alert(title='Motion Detected on Camera: {}'.format(args.name),
              tlp=3,
              tags=['motioneye', 'cctv'],
              description='Motion was detected at camera "{}". Event ID:{}'.format(args.name, args.event_id),
              type='external',
              source=args.name,
              sourceRef=sourceRef,
              date = int(ts_value.timestamp() * 1000)
            )

# POST Alert
response = api.create_alert(alert)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)