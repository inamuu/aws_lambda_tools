Notify SlowQueryLogs to Slack
===

- SlowQueryLogsをSlackへ通知させるためのLambdaです。
- Auroraのパラメータグループでスローログを有効にし、ログをファイルにするとCloudwatchLogsにスロークエリログが出力されるようになります。

## テスト方法

環境変数として下記を設定します。

```
export SLACK_POSTURL=https://XXX
export SLACK_CHANNEL=XXX
```

python-lambda-localを使うことで手元でテスト可能です。

```sh
$ pip install python-lambda-local
```

event.json を用意しているので、下記を実行します。

```sh
$ envchain SLACK python-lambda-local -f lambda_handler lambda.py event.json
```

## メモ

実際に動いているDBでスローログを出すには下記sleepクエリが良いです。

```sql
select sleep(10);
```

