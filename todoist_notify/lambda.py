# coding: utf-8

import datetime
import json
import requests
import os
import re
import sys
from todoist.api import TodoistAPI

#SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
#SLACK_POSTURL = os.environ['SLACK_POSTURL']
TDIAPI = TodoistAPI(os.environ['TODOISTAPITOKEN'], cache=False)
TDIAPI.sync()
#name = os.environ['TODOIST_PJT']
name = 'Tasks'

def activity(name):
    actlogs = TDIAPI.activity.get()
    pjts = TDIAPI.state['projects']

    for projects_id in pjts:
        if projects_id['name'] == name:
            tasks_project_id = projects_id['id']
            break

    event_list = []
    for events in actlogs['events']:
        datetime_utc = datetime.datetime.now() - datetime.timedelta(hours = 9)
        today = datetime_utc.strftime("%Y-%m-%d")

        if events['event_type'] == 'completed' and re.sub('T.*', '' ,events['event_date']) in today and events['parent_project_id'] == tasks_project_id:
            print(events['extra_data'])
            event_list.append(events['extra_data']['content'])

def tasklist(name):

    #for projects_id in list:
    #    if projects_id['name'] == name:
    #        tasks_project_id = projects_id['id']
    #        break

    #try:
    #    tasks_project_id
    #except NameError:
    #    print("プロジェクト名が正しくありません。プロジェクト名を正しく入力してください。")
    #    sys.exit()

    pjts = TDIAPI.state['projects']
    items = TDIAPI.state['items']
    labels = TDIAPI.state['labels']
    sects = TDIAPI.state['sections']

    inbox_list = []
    doing_list = []
    review_list = []
    any_list = []

    print(labels)
    sys.exit()

    for item in items:
        l_content = item['content']
        l_pjt_name = [ pjt['name'] for pjt in pjts if item['project_id'] == pjt['id'] ]
        l_sec_name = [ sect['name'] for sect in sects if item['section_id'] == sect['id']]
        #print('+++')
        #print(l_pjt_id)
        #print(l_content)
        #print(l_sec_name[0])

        if l_sec_name is not None and l_sec_name[0] == 'ToDo':
            print(l_sec_name)
        #if item['checked'] == 0 and item['project_id'] == tasks_project_id:

            #taskcontent = '- ' + item['content']
            #slackmessage.append(taskcontent)
            #print(taskcontent)
        #print(slackmessage)
    #message = '\n'.join(slackmessage)
    return

def lambda_handler(event, context):
    msg = tasklist(name)
    title = "*[定期通知] プロジェクト " + name + " のタスクリスト*\n"
    slack_message = {
        'channel': SLACK_CHANNEL,
        'icon_emoji': ":todoist:",
        'text': title,
        "attachments": [
            {
                "color": "#36a64f",
                "fields": [
                    {
                        "value": msg,
                    },
                ],
            }
        ]
    }
    #requests.post(SLACK_POSTURL, data=json.dumps(slack_message))

## for Debug
if __name__ == '__main__':
    #tasklist(name)
    activity(name)
