# coding: utf-8

import json
import requests
import os
import re
import sys

CHATWORK_API = "https://api.chatwork.com/v2/rooms/"
API_TOKEN = os.environ['CHATWORK_API_TOKEN']
SEARCH_PREFIX = os.environ['SEARCH_PREFIX']

def room_list():
    headers = { 'X-ChatWorkToken': API_TOKEN }
    room_lists = requests.get(CHATWORK_API, headers=headers)
    room_lists_json = json.loads(room_lists.content)

    roomid_array = []
    for room_list in room_lists_json:
        if SEARCH_PREFIX in room_list['name']:
            print(room_list['name'])
            roomid_array.append(room_list['room_id'])
    return roomid_array

def send_message(room_lists):
    for room_list in room_lists:
        post_url = CHATWORK_API + str(room_list) + '/messages'
        params = {
            'body': '本日の営業は終了いたしました(bow)' + '\n'
                    'またご連絡をお待ちしております。'
            }
        headers = { 'X-ChatWorkToken': API_TOKEN }
        resp = requests.post(post_url, headers=headers, params=params)
        print(resp.content)
    return

def lambda_handler(event, context):
    room_lists = room_list()
    send_message(room_lists)
