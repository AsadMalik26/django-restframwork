from webbrowser import get
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def getData(request):
    person = {"name": "Asad", "age": "21"}
    print(person)
    return HttpResponse(person)
