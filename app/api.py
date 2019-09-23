import io
import json

from flask import Flask, Response, request, send_file

from .services import to_html
from .utils import html_to_pdf, is_xml, xml_to_dict

app = Flask(__name__)


@app.route("/", methods=["POST"])
@app.route("/sii_beautify/", methods=["POST"])
def index():
    type_format = request.values.get("format", "").lower()
    if not type_format or type_format not in ["html", "json", "pdf"]:
        message_type_format = "You must add `format=[html,json,pdf]` to formData"
        return json.dumps({"error": message_type_format}), 400
    if not request.files:
        return json.dumps({"error": "You must send a file"}), 400
    file = request.files.get("xml")
    xml = file.stream.read()
    if not is_xml(xml):
        return json.dumps({"error": "File xml it's invalid"}), 400

    if type_format == "json":
        return Response(json.dumps(xml_to_dict(xml)), mimetype="application/json")

    html = to_html(xml)
    if type_format == "html":
        return Response(html, mimetype="application/json")

    if type_format == "pdf":
        pdf = html_to_pdf(html)
        return send_file(io.BytesIO(pdf), mimetype="application/pdf")
