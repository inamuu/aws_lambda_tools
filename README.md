# aws_lambda_tools

Samples and tools develop AWS Lambda functions.

# Getting Started

```
pip install python-lambda-local
pip install lambda-uploader
```

# Local Test

```sh
$ python-lambda-local -f <Handler> <Python File Name> <JSON File(Event)>
```

# Upload function

```sh
$ cd TOOLPATH
$ lambda-uploader --profile=PROFILENAME
Î» Building Package
Î» Uploading Package
Î» Fin
```

# References

- http://blog.serverworks.co.jp/tech/2017/03/06/post-55106/