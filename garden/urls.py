
from django.contrib import admin
from django.urls import path, include
from pizza import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('order', views.order, name='order')
]
