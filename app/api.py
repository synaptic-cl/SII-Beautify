import io
import json

from flask import Flask, request, send_file

from .services import to_html
from .utils import html_to_pdf, is_xml, xml_to_dict

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    type_format = request.values.get("format", "").lower()
    if not request.files:
        return json.dumps({"error": "You must send a file"}), 400
    file = request.files.get("xml")
    xml = file.stream.read()
    if not is_xml(xml):
        return json.dumps({"error": "File xml it's invalid"}), 400

    if type_format == "json":
        return xml_to_dict(xml)

    html = to_html(xml)
    if type_format == "html":
        return html

    if type_format == "pdf":
        pdf = html_to_pdf(html)
        return send_file(io.BytesIO(pdf), mimetype="application/pdf")
