from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


def platform_view(request):
    return render(request, 'platform.html')

def cart_view(request):
    return render(request, 'cart.html')

def games_view(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'games.html', context=context)

def menu_view(request):
    return render(request, 'menu.html')

def sign_up_by_html(request):
    users = Buyer.objects.all()
    users_list = [user.name for user in users]
    context = {
        'Buyer': users
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            return render(request, 'registration_page.html', {'error': 'Пароли не совпадают'})
        elif int(age) < 18:
            return render(request, 'registration_page.html', {'error': 'Вы должны быть старше 18'})
        elif username in users_list:
            return render(request, 'registration_page.html', {'error': 'Пользователь уже существует'})
        else:
            return HttpResponse(f'Приветствуем {username}')
    return render(request, 'registration_page.html',context)

def sign_up_by_django(request):
    users = Buyer.objects.all()
    users_list = [user.name for user in users]
    context = {
        'Buyer': users
    }
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info['username'] = username
            info['age'] = age

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users_list:
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username,balance=10000, age=age)
                return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', context=info)