from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html, status=200)

def login(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html, status=201)
