from django.urls import path

from shop.views import main_page, register_page, login_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('register_page/', register_page, name='register_page'),
    path('login_page/', login_page, name='login_page')
]
