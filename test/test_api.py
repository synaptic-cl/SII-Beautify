import io
import json
import os

import pytest

from app.utils import is_html, is_json

PATH = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def client():
    from app import api

    app = api.app

    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    return testing_client
    ctx.pop()


def test_xml_to_html(client):
    with client as c:
        file = io.BytesIO(open(os.path.join(PATH, "sii.xml"), "rb").read())
        response = c.post("/", data={"format": "html", "xml": (file, "sii.xml")})
        assert response.status_code == 200
        assert is_html(response.data)


def test_xml_to_html_upper_format(client):
    with client as c:
        file = io.BytesIO(open(os.path.join(PATH, "sii.xml"), "rb").read())
        response = c.post("/", data={"format": "HTML", "xml": (file, "sii.xml")})
        assert response.status_code == 200
        assert is_html(response.data)


def test_xml_to_pdf(client):
    with client as c:
        file = io.BytesIO(open(os.path.join(PATH, "sii.xml"), "rb").read())
        response = c.post("/", data={"format": "pdf", "xml": (file, "sii.xml")})
        assert response.status_code == 200
        assert isinstance(str(response.data), str)
        assert str(response.data).find("PDF-")


def test_xml_to_json(client):
    with client as c:
        file = io.BytesIO(open(os.path.join(PATH, "sii.xml"), "rb").read())
        response = c.post("/", data={"format": "json", "xml": (file, "sii.xml")})
        assert response.status_code == 200
        assert is_json(response.data)


def test_xml_error_without_file(client):
    with client as c:
        response = c.post("/", data={"format": "json", "xml": ""})
        assert response.status_code == 400
        assert is_json(response.data)
        assert json.loads(response.data)["error"] == "You must send a file"


def test_xml_error_not_xml(client):
    with client as c:
        file = io.BytesIO(b"")
        response = c.post("/", data={"format": "json", "xml": (file, "sii.xml")})
        assert response.status_code == 400
        assert is_json(response.data)
        assert json.loads(response.data)["error"] == "File xml it's invalid"
