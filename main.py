from flask import Response

from app import api


def sii_beautify(request):
    if request.method == "POST":
        return api.index()
    return Response(None, status=404)
