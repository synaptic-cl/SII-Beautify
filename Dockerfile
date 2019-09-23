FROM python:3.7-slim

LABEL maintainer="Héctor Villarroel hvillarroel@synaptic.cl"

RUN apt-get update \
    && apt-get install -y \
    git gcc libsasl2-dev \
    libldap2-dev libssl-dev graphviz

RUN pip install --upgrade pip &&\
    pip install pipenv

WORKDIR /app

COPY Pipfile .

RUN pipenv install --dev

CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0"]

