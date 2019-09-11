# SII Beautify

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
