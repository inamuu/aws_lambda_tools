# coding: utf-8

import os
import base64
import gzip
import json
import logging
from io import BytesIO
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

Slack_Webhook_URL = os.environ['SLACK_POSTURL']
Slack_Channel = os.environ['SLACK_CHANNEL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    buffer = BytesIO(base64.b64decode(json.dumps(event['awslogs']['data'])))
    with gzip.GzipFile(mode='rb', fileobj=buffer) as sb:
        data = sb.read()

    log = json.loads(data.decode('utf-8'))
    message = str(log['logEvents'][0]['message'])

    headers = {"Content-Type" : "application/json"}
    slack_message = {
        'text': '*New Slow Query Alert*',
        'channel': Slack_Channel,
        'attachments': [
            {
                'color': '#36464f',
                'text': message,
                'footer': 'Amazon RDS'
            }
        ]
    }

    req = Request(Slack_Webhook_URL, json.dumps(slack_message).encode('utf-8'), headers=headers)
    try:
        response = urlopen(req)
        response.read()
        logger.info('Message posted to %s', Slack_Webhook_URL)
    except HTTPError as e:
        logger.error('Request failed: %d %s', e.code, e.reason)
    except URLError as e:
        logger.error('Server connection failed: %s', e.reason)
