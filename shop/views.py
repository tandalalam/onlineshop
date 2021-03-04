from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.


def main_page(request):
    return render(request, 'shop/main_page.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password1,
                                        first_name=first_name,
                                        last_name=last_name
                                        )
        user.save()
        return HttpResponseRedirect('/register_page')
    return render(request, 'shop/register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(context={"errors": "no user found"}, request=request, template_name='shop/login.html')
        else:
            login(request, user)
            return render(request, 'shop/main_page.html')
    return render(request, 'shop/login.html')
