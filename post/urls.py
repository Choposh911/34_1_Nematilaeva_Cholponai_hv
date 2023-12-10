from django.urls import path

from post import views

urlpatterns = [
    path('hello', views.hello_view),
    path('current_date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_list),
    path('products/<int:id>/', views.products_detail_view),
    path('', views.main_view),
    path('category/', views.categories_list),
    path('product/create/', views.product_create),
    path('category/create/', views.category_create), ]
