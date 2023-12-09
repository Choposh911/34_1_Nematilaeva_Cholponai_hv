from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import settings
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.hello_view),
    path('current_date/', views.current_date_view),
    path('goodbye/', views.goodbye_view),
    path('products/', views.products_list),
    path('products/<int:id>/', views.products_detail_view),
    path('', views.main_view),
    path('category/', views.categories_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)