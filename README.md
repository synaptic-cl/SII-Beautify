# SII Beautify

Convert XML file from SII (http://home.sii.cl) to PDF, HTML or JSON.

## How to use

Options:

* `xml`: file path you want to convert
* `format`:
  * `html`
  * `pdf`
  * `json`

**Example HTML**

```bash
curl --request POST \
-F format=html \
-F xml=@/xml/file.xml \
https://us-central1-slack-services.cloudfunctions.net/sii_beautify
```



**Example PDF **

```bash
curl --request POST \
-F format=pdf \
-F xml=@/xml/file.xml \
-o file.pdf
https://us-central1-slack-services.cloudfunctions.net/sii_beautify
```



**Example JSON**

```bash
curl --request POST \
-F format=json \
-F xml=@/xml/file.xml \
https://us-central1-slack-services.cloudfunctions.net/sii_beautify
```



## Development

### pre requirements

You need install `pre-commit`

* MacOs `brew install pre-commit`

### Install

```bash
docker-compose build
pre-commit install
```



### Test

```bash
docker-compose run --rm app pipenv run pytest
```

Coverage

```bash
# coverage 100%
docker-compose run --rm app pipenv run pytest --cov --cov-fail-under=100

# Report HTML
docker-compose run --rm app pipenv run pytest --cov --cov-report=html
```



### How install packages

```bash
docker-compose run --rm app pipenv install flask
```



## Deploy in GCP functions

Quickstart https://cloud.google.com/functions/docs/quickstart-python



```bash
gcloud functions deploy sii_beautify --runtime python37 --trigger-http --memory 128MB
```
