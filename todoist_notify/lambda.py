# coding: utf-8

import json
import requests
import os
import sys
from todoist.api import TodoistAPI

#SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
#SLACK_POSTURL = os.environ['SLACK_POSTURL']
TDIAPI = TodoistAPI(os.environ['TODOISTAPITOKEN'], cache=False)
TDIAPI.sync()
name = os.environ['TODOIST_PJT']

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
    slackmessage = []

    for item in items:
        l_content = item['content']
        l_pjt_id = [ pjt['name'] for pjt in pjts if item['project_id'] == pjt['id'] ]
        l_sec_id = [ sect['name'] for sect in sects if item['section_id'] == sect['id']]
        print('+++')
        print(l_pjt_id)
        print(l_content)
        print(l_sec_id)
        #if item['checked'] == 0 and item['project_id'] == tasks_project_id:

            #taskcontent = '- ' + item['content']
            #slackmessage.append(taskcontent)
            #print(taskcontent)
        #print(slackmessage)
    message = '\n'.join(slackmessage)
    return message

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
    tasklist(name)
