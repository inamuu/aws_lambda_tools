Chatwork Notify
===

Chatwork通知用Lambdaです。
Chatworkで特定のPrefixがついているRoomへ通知を行います。  

### セットアップ手順

1. pyenvでPython3.8をインストールします。
2. python -m venv ~/.venv/lancers/online_assistant_group_notify
3. source ~/.venv/lancers/chatwork_notify/bin/activate
4. pip install -U pip
5. pip install -r requirements.txt

### デバッグ

手元で検証する手順です。
下記を実行することでevent.jsonの結果がテストできます。

```sh
CHATWORK_API_TOKEN=XXXXXX SEARCH_PREFIX='通知しても良いルームのPrefix'  python-lambda-local -f lambda_handler lambda.py event.json
```
