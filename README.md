# SII Beautify

Converto XML from SII (http://home.sii.cl) to PDF, HTML or JSON



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
https://sii_beautify.services.synaptic.cl
```



**Example PDF **

```bash
curl --request POST \
-F format=pdf \
-F xml=@/xml/file.xml \
-o file.pdf
https://sii_beautify.services.synaptic.cl
```



**Example JSON**

```bash
curl --request POST \
-F format=json \
-F xml=@/xml/file.xml \
https://sii_beautify.services.synaptic.cl
```





## pre requirements

You need install `pre-commit`

* MacOs `brew install pre-commit`


## Install

# On Docker (recommend)
```bash
docker-compose build
pre-commit install
```

# Local

```bash
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pre-commit install
```

# How install packages

```bash
docker-compose run --rm app pipenv install flask
```

## Credits
This package was created with Cookiecutter and the [sourceryai/python-best-practices-cookiecutter](https://github.com/sourceryai/python-best-practices-cookiecutter) project template.
