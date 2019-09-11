FROM python:3.7

RUN apt-get update && apt-get upgrade -y
RUN apt-get install xfonts-75dpi xfonts-base -y
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb
RUN dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb

RUN pip install --upgrade pip &&\
    pip install pipx pipenv &&\
    pipx ensurepath

WORKDIR /app

COPY Pipfile .
# COPY setup.cfg .

RUN pipenv install --dev

CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0"]

