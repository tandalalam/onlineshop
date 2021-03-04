from django.urls import path

from shop.views import main_page

urlpatterns = [
    path('mainpage/', main_page, name='main_page')
]
