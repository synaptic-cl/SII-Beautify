import json
import os
from xml.etree import ElementTree as ET

import jinja2
import pdfkit
import xmltodict
from bs4 import BeautifulSoup


def is_xml(xml):
    try:
        ET.fromstring(xml)
        return True
    except Exception as e:
        print(e)
        return False


def is_html(html):
    return bool(BeautifulSoup(html, "html.parser").find())


def is_json(json_file):
    try:
        json.loads(json_file)
        return True
    except Exception as e:
        print(e)
        return False


def xml_to_dict(xml):
    if is_xml(xml):
        return xmltodict.parse(xml)
    return {}


def to_currency(value):
    if not value:
        value = 0
    if type(value) == str:
        value = float(value)
    return f"${value:,.0f} CLP".replace("$-", "-$").replace(",", ".")


def html_to_pdf(html):
    return pdfkit.from_string(html, False)


def render_template(file, **data):
    path = os.path.dirname(os.path.abspath(__file__))
    templateLoader = jinja2.FileSystemLoader(searchpath=path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(file)
    return template.render(**data)
