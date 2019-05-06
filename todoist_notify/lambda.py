# coding: utf-8

import json
import requests
import os
import sys
from todoist.api import TodoistAPI

SLACK_CHANNEL = os.environ['SLACK_CHANNEL']
SLACK_POSTURL = os.environ['SLACK_POSTURL']
NOTIFY_USER = os.environ['NOTIFY_USER']
todoistapi = TodoistAPI(os.environ['TODOISTAPITOKEN'])

def tasklist(name):
    list = todoistapi.state['projects']
    for projects_id in list:
        #if projects_id['name'] == args.tasks:
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
    print('### タスク一覧(id, 内容)')
    for name in items:
        if name['project_id'] == tasks_project_id:
            taskid = name['id']
            taskcontent = name['content']
            message = (str(
                '- '
                + taskcontent))
            slackmessage.append(taskcontent)
    message = '\n'.join(slackmessage)
    return message

def lambda_handler(event, context):
    name = os.environ['TODOIST_PJT']
    msg = tasklist(name)
    slack_message = {
        'channel': SLACK_CHANNEL,
        'icon_emoji': ":robot_face:",
        'text': msg,
    }
    requests.post(SLACK_POSTURL, data=json.dumps(slack_message))

## for Debug
#if __name__ == '__main__':
#    name = os.environ['TODOIST_PJT']
#    tasklist(name)
