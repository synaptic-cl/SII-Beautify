from datetime import datetime

# import lxml.etree as ET
# import pdf417
from bs4 import BeautifulSoup

from .utils import render_template, to_currency


def to_html(xml):
    data = {}
    soup = BeautifulSoup(xml, "xml")
    emidorAddress = (
        f"{soup.find('DirOrigen').text}, "
        f"{soup.find('CmnaOrigen').text}, "
        f"{soup.find('CiudadOrigen').text}"
    )
    receptorAddress = (
        f"{soup.find('DirRecep').text}, "
        f"{soup.find('CmnaRecep').text}, "
        f"{soup.find('CiudadRecep').text}"
    )

    elem_neto = soup.find("MntNeto")
    elem_iva = soup.find("IVA")
    elem_total = soup.find("MntTotal")

    total_neto = to_currency(elem_neto.text) if elem_neto else None
    total_iva = to_currency(elem_iva.text) if elem_iva else None
    total = to_currency(elem_total.text) if elem_total else None

    details = []
    for row in soup.find_all("Detalle"):
        details.append(
            {
                "count": int(float(row.find("QtyItem").text)),
                "item": row.find("NmbItem").text,
                "description": row.find("DscItem").text,
                "price": to_currency(row.find("PrcItem").text),
            }
        )

    date_resolution = datetime.strptime(
        soup.find("TmstFirmaEnv").text, "%Y-%m-%dT%H:%M:%S"
    )

    # barcode = '<?xml version="1.0" encoding="ISO-8859-1"?>' + str(soup.find('TED'))
    # print(barcode)
    # print(ET.canonicalize(str(soup.find('TED'))))
    # print(bytes(str(soup.find('TED')),'iso-8859-1').decode('utf-8'))
    # # return ""
    # code = pdf417.encode(
    #     ET.canonicalize(bytes(str(soup.find('TED')),'iso-8859-1').decode('utf-8'))
    # )
    # code = pdf417.encode(barcode.encode('utf8').decode('utf8'))
    # code.save('img.jpg')
    # print(dir(pdf417))
    # print(barcode)

    data = {
        "emisorName": soup.find("RznSoc").text,
        "emisorRut": soup.find("RUTEmisor").text,
        "emisorGiro": soup.find("GiroEmis").text,
        "emidorAddress": emidorAddress,
        "folio": soup.find("Folio").text,
        "dateTransmitter": soup.find("FchEmis").text,
        "receptorName": soup.find("RznSocRecep").text,
        "receptorRut": soup.find("RUTRecep").text,
        "receptorGiro": soup.find("GiroRecep").text,
        "receptorAddress": receptorAddress,
        "details": details,
        "totalNeto": total_neto,
        "totalIva": total_iva,
        "total": total,
        "resolution": f"{soup.find('NroResol').text} de {date_resolution.year}",
        # "barcode": barcode
    }

    # print(data)

    html = render_template("template.html", **data)
    return html
