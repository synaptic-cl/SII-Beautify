from app import api


def sii_beautify(request):
    if request.method == "POST":
        return api.index()
