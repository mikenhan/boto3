# AWS Boto3

A collection of boto3 scripts that I have written to call AWS APIs for services such as:
* S3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install boto3.

```bash
pip install boto3
```

## Usage

After installation ensure AWS credentials are set up `(ie. ~/.aws/credentials)`
```bash
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

Then we configure a default region `(~/.aws/config)`

```bash
[default]
region = us-west-2
```

Then we can run the individual python scripts from our terminal
```
python3 {folder_name}/{script}.py
```
