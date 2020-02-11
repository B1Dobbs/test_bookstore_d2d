from .models import OnixFile

def onix_file(request):
    return {'onix_file': OnixFile.load()}