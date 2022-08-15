from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<html><title>To-Do lists</title></html>')
