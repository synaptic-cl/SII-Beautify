FROM python:3.7

RUN pip install --upgrade pip &&\
    pip install pipx pipenv &&\
    pipx ensurepath

WORKDIR /app

COPY . .

RUN pipenv install --dev

CMD ["pipenv", "run", "pytest"]

