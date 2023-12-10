from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, render
import datetime

from post.forms import ProductForms, ReviewForms, CategoryForms
from post.models import Product, Category, Review
PAGINATION_LIMIT = 3


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
    if request.method == 'GET':
        posts = Product.objects.all().order_by('-title', 'created_at')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        ''' start_with, ends_with, icontains '''
        '''and | or'''
        if search:
            posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)
        max_page = posts.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)
        ''' posts splice'''
        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        context = {
            'posts': posts,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/product.html', context=context)



def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'categories': categories})


def products_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.reviews.all(),
            'form': ReviewForms
        }
        return render(request, 'products/product_detail.html', context=context)
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        form = ReviewForms(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product_id=id
            )

        context = {
            'product': product,
            'review': product.reviews.all(),
            'form': ReviewForms
        }
        return render(request, 'products/product_detail.html', context=context)


def product_create(request):
    if request.method == "GET":
        context = {
            'form': ProductForms
        }
        return render(request, 'products/product_create.html', context)
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)

        context = {
            'form': form
        }
        return render(request, 'products/product_create.html', context)


def category_create(request):
    if request.method == "GET":
        context = {
            'form': CategoryForms
        }
        return render(request, 'products/category_create.html', context)
    if request.method == 'POST':
        form = CategoryForms(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)

        context = {
            'form': form
        }
        return render(request, 'products/category_create.html', context)
