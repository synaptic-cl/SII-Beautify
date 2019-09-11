import io
import os

from app.utils import (
    html_to_pdf,
    is_html,
    is_json,
    is_xml,
    render_template,
    to_currency,
    xml_to_dict,
)

PATH = os.path.dirname(os.path.abspath(__file__))


def test_is_xml():
    assert is_xml(open(os.path.join(PATH, "sii.xml"), "rb").read())


def test_is_html():
    assert is_html("<!DOCTYPE html><html><body></body></html>")


def test_xml_to_dict():
    file = open(os.path.join(PATH, "sii.xml"), "rb").read()
    assert isinstance(xml_to_dict(file), dict)


def test_xml_to_dict_none():
    assert not xml_to_dict("")


def test_to_currency():
    value = to_currency(1000)
    assert value == "$1.000 CLP"


def test_to_currency_none():
    value = to_currency(None)
    assert value == "$0 CLP"


def test_html_to_pdf():
    pdf = html_to_pdf("<!DOCTYPE html><html><body></body></html>")
    assert str(io.BytesIO(pdf).getvalue()).find("PDF-") >= 0


def test_is_json():
    assert is_json('{"test": "OK"}')


def test_is_json_false():
    assert not is_json('{"test": "OK"')


def test_render_template():
    response = render_template("template.html", emisorName="Test")
    assert response.find("Test") >= 0
