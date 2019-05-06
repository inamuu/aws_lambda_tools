# Set environment using envchain.

See https://techlife.cookpad.com/entry/envchain

```sh
$ brew install https://raw.githubusercontent.com/sorah/envchain/master/brew/envchain.rb
```

```sh
$ envchain --set slack SLACK_POSTURL
$ envchain --set slack SLACK_CHANNEL
```

# Test Code

Run python-lambda-local

```sh
$ envchain slack python-lambda-local -f lambda_handler lambda.py event.json
[root - INFO - 2019-05-03 21:36:15,339] Event: {}
[root - INFO - 2019-05-03 21:36:15,340] START RequestId: 0f9e73be-e070-4011-bec7-c30adff2dbc6 Version:
[root - INFO - 2019-05-03 21:36:15,788] END RequestId: 0f9e73be-e070-4011-bec7-c30adff2dbc6
[root - INFO - 2019-05-03 21:36:15,788] REPORT RequestId: 0f9e73be-e070-4011-bec7-c30adff2dbc6  Duration: 403.88 ms
[root - INFO - 2019-05-03 21:36:15,789] RESULT:
None
```

# Upload code to aws lambda

```sh
$ lambda-uploader --profile=AWS_PROFILENAME
```
