FROM python:3.7

RUN pip install --upgrade pip &&\
    pip install pipx pipenv &&\
    pipx ensurepath

WORKDIR /app

COPY Pipfile .

RUN pipenv install --dev

CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0"]

