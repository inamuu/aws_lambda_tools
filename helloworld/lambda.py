# coding: utf-8

import json
import requests
import os

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_POSTURL = os.environ['SLACK_POSTURL']

def lambda_handler(event, context):
    slack_message = {
        'channel': SLACK_CHANNEL,
        'icon_emoji': ":robot_face:",
        'text': 'helloworld',
    }
    requests.post(SLACK_POSTURL, data=json.dumps(slack_message))
