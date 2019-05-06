# coding: utf-8

import json
import requests
import os
import sys
from todoist.api import TodoistAPI

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_POSTURL = os.environ['SLACK_POSTURL']
todoistapi = TodoistAPI(os.environ['TODOISTAPITOKEN'], cache=False)
todoistapi.sync()

def tasklist(name):
    list = todoistapi.state['projects']
    for projects_id in list:
        if projects_id['name'] == name:
            tasks_project_id = projects_id['id']
            break

    try:
        tasks_project_id
    except NameError:
        print("プロジェクト名が正しくありません。プロジェクト名を正しく入力してください。")
        sys.exit()

    items = todoistapi.state['items']
    slackmessage = []
    title = "*[定期通知] プロジェクト " + name + " のタスクリスト*\n"
    for name in items:
        if name['checked'] == 0:
            if name['project_id'] == tasks_project_id:
                taskcontent = '- ' + name['content']
                slackmessage.append(taskcontent)
    message = title + '\n'.join(slackmessage)
    return message

def lambda_handler(event, context):
    name = os.environ['TODOIST_PJT']
    msg = tasklist(name)
    slack_message = {
        'channel': SLACK_CHANNEL,
        'icon_emoji': ":todoist:",
        'text': msg,
    }
    requests.post(SLACK_POSTURL, data=json.dumps(slack_message))

## for Debug
#if __name__ == '__main__':
#    name = os.environ['TODOIST_PJT']
#    tasklist(name)
