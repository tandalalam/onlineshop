from django.urls import path

from shop.views import main_page, register_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register/', register_page, name='register_page' )
]
