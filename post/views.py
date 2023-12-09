from django.shortcuts import render
from django.shortcuts import HttpResponse, render
import datetime

from post.models import Product, Category


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


def products_list(request):
    product = Product.objects.all()
    return render(request, 'products/product.html', {'products': product})


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'categories': categories})
