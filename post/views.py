from django.shortcuts import render
from django.shortcuts import HttpResponse, render
import datetime

def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project ")


def current_date_view(request):
    if request.method == 'GET':
        current_date = datetime.datetime.now()
        return HttpResponse(f"Current date: {current_date}")


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
